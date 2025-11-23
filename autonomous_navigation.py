from picamera2 import Picamera2
import cv2
import numpy as np
from gpiozero import Motor, PWMOutputDevice
from time import time
import threading

# Initialize camera
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"size": (640, 480), "format": "BGR888"})
picam2.configure(preview_config)
picam2.start()

# Initialize motors with proper PWM control
motor_left = Motor(forward=17, backward=27)
motor_right = Motor(forward=22, backward=23)
enable_left = PWMOutputDevice(24, frequency=1000)
enable_right = PWMOutputDevice(25, frequency=1000)

# Motor control variables
current_left_speed = 0
current_right_speed = 0
motor_lock = threading.Lock()

def stop():
    global current_left_speed, current_right_speed
    with motor_lock:
        enable_left.value = 0
        enable_right.value = 0
        motor_left.stop()
        motor_right.stop()
        current_left_speed = 0
        current_right_speed = 0
    print("[MOTORS] Stopped")

def set_motors(left_speed, right_speed, left_direction='forward', right_direction='forward'):
    global current_left_speed, current_right_speed
    with motor_lock:
        # Set left motor
        if left_direction == 'forward':
            motor_left.forward()
        else:
            motor_left.backward()
        enable_left.value = abs(left_speed)
        
        # Set right motor
        if right_direction == 'forward':
            motor_right.forward()
        else:
            motor_right.backward()
        enable_right.value = abs(right_speed)
        
        current_left_speed = left_speed
        current_right_speed = right_speed
    print(f"[MOTORS] L:{left_speed:.2f}({left_direction}), R:{right_speed:.2f}({right_direction})")

def forward(speed=0.7):
    set_motors(speed, speed, 'forward', 'forward')

def turn_left(speed=0.6):
    set_motors(speed * 0.5, speed, 'backward', 'forward')

def turn_right(speed=0.6):
    set_motors(speed, speed * 0.5, 'forward', 'backward')

# Parameters
FORWARD_SPEED = 0.75
TURN_SPEED = 0.65
AVOID_THRESHOLD = 5000

# State management
last_obstacle_time = 0
turn_duration = 0.6  # seconds

try:
    print("AI camera loitering started...")
    stop()  # Ensure motors start stopped
    
    while True:
        # Capture and process frame
        frame = picam2.capture_array()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        _, thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY_INV)

        # Focus on front region
        roi = thresh[200:480, 160:480]
        obstacle_pixels = np.sum(roi == 255)

        current_time = time()
        
        # Check if we're currently in a turning maneuver
        if current_time - last_obstacle_time < turn_duration:
            # Still in turning phase, don't process new commands
            cv2.putText(frame, f"Turning...", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            # Process obstacle detection
            if obstacle_pixels > AVOID_THRESHOLD:
                print(f"Obstacle detected ({obstacle_pixels}) → turning")
                stop()
                
                # Choose random turn direction
                if np.random.rand() > 0.5:
                    turn_left(TURN_SPEED)
                    cv2.putText(frame, "Turning LEFT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    turn_right(TURN_SPEED)
                    cv2.putText(frame, "Turning RIGHT", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                last_obstacle_time = current_time
            else:
                print("Clear path → moving forward")
                forward(FORWARD_SPEED)
                cv2.putText(frame, "Moving FORWARD", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Display obstacle info on frame
        cv2.putText(frame, f"Obstacle pixels: {obstacle_pixels}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.rectangle(frame, (160, 200), (480, 480), (0, 255, 255), 2)  # ROI visualization
        
        cv2.imshow("View", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stopped by user.")
except Exception as e:
    print(f"Error: {e}")
finally:
    stop()
    picam2.stop()
    cv2.destroyAllWindows()