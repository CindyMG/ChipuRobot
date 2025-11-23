from vosk import Model, KaldiRecognizer
import pyaudio
import time
import json
import sys
from gpiozero import Motor, PWMOutputDevice

# -----------------------
# MOTOR SETUP 
# -----------------------

motor_left = Motor(forward=17, backward=27)
motor_right = Motor(forward=22, backward=23)

# Enable pins required for motor power
enable_left = PWMOutputDevice(24)
enable_right = PWMOutputDevice(25)

# Set both enables HIGH (full power)
enable_left.value = 1
enable_right.value = 1

SPEED = 0.35   # 35% speed for all movements

def stop():
    motor_left.stop()
    motor_right.stop()
    print("STOP")

def forward():
    motor_left.forward(SPEED)
    motor_right.forward(SPEED)
    print("FORWARD")

def backward():
    motor_left.backward(SPEED)
    motor_right.backward(SPEED)
    print("BACKWARD")

def left():
    motor_left.backward(SPEED)
    motor_right.forward(SPEED)
    print("LEFT")

def right():
    motor_left.forward(SPEED)
    motor_right.backward(SPEED)
    print("RIGHT")


# -----------------------
# LOAD VOSK MODEL
# -----------------------

MODEL_PATH = "/home/mainairungu/Desktop/cindy/vosk-model-small-en-us-0.15"

try:
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, 48000)   # using supported rate
except Exception as e:
    print(f"Error loading Vosk model: {e}")
    sys.exit(1)


# -----------------------
# MICROPHONE SETUP
# -----------------------

audio = pyaudio.PyAudio()

mic_index = 0
print("Using microphone device index:", mic_index)

stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=48000,
    input=True,
    input_device_index=mic_index,
    frames_per_buffer=4000
)
stream.start_stream()

print("\nVoice control ready.")
print("Say commands such as: 'forward', 'back', 'left', 'right', 'stop'\n")

last_command_time = time.time()
quiet_timeout = 10     # seconds


# -----------------------
# MAIN LISTEN LOOP
# -----------------------

try:
    while True:
        data = stream.read(4000, exception_on_overflow=False)

        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").lower().strip()

            if text:
                print(f"Heard: {text}")

                last_command_time = time.time()  # reset timer when speech detected

                if "forward" in text:
                    forward()
                elif "back" in text:
                    backward()
                elif "left" in text:
                    left()
                elif "right" in text:
                    right()
                elif "stop" in text:
                    stop()

        # Quiet timeout → auto-stop, but NO SPAM
        if time.time() - last_command_time > quiet_timeout:
            stop()
            last_command_time = time.time()  # reset after one stop output

except KeyboardInterrupt:
    print("\nExiting voice control...")

finally:
    stop()
    stream.stop_stream()
    stream.close()
    audio.terminate()
