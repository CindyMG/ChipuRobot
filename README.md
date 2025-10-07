# ChipuRobot: A Raspberry-Pi Based Educational Robotics Kit for Public Secondary Schools in Kenya

## Project Description
The **Raspberry Pi Educational Robot** is a hands-on learning platform designed to introduce high school students to **robotics, AI, and STEM concepts**. The project focuses on developing a modular robot that can perform basic navigation tasks, respond to its surroundings, and eventually interact with users through voice commands.

This robot demonstrates key robotics principles such as:
- Sensor integration and obstacle detection  
- Motion control and path planning  
- Real-time data processing  
- Voice interaction and AI integration (planned)  

The project aims to bridge the gap between theoretical STEM education and practical robotics experience by offering a tangible system students can learn from, modify, and experiment with.

---

## 🗂️ Project Structure

```
.
├── main.py          # Core control logic for movement and sensors
├── requirements.txt # Python dependencies (to be updated)
├── README.md        # Project documentation
└── .github/         # GitHub configurations and workflows
```


As development progresses, additional folders (e.g., `/modules`, `/voice`, `/tests`) will be added for better organisation.

---

## Features

### Implemented
- **Basic Motor Control:**  
  Controls DC motors using an L298N motor driver via Raspberry Pi GPIO pins.  
- **Hardware Assembly:**  
  Robot chassis, motor driver, picamera2 and Raspberry Pi setup completed and tested.  

### In Progress 
- **LiDAR Integration:**  
  Preparing to include LiDAR for accurate distance sensing and mapping.  

### Upcoming Features
- **Voice Command Interface:**  
  Integration of microphone and speech recognition to control robot movement.   

---

## Hardware Components
| Component | Purpose |
|------------|----------|
| **Raspberry Pi 4 / 5** | Main processing unit controlling sensors and motors |
| **L298N Motor Driver** | Controls direction and speed of DC motors |
| **DC Motors (x2)** | Enable robot movement |
| **LiDAR Sensor (Planned)** | For precise environmental mapping |
| **USB Microphone (Planned)** | Captures user voice commands |
| **Lipo Battery Pack** | Powers the system |

---

## Software and Tools
- **Programming Language:** Python 3  
- **Libraries Used:**  
  - `RPi.GPIO` – Controls Raspberry Pi GPIO pins  
- **Operating System:** Raspberry Pi OS (Bullseye)  

---

## Project Setup Walkthrough

### 1. Clone the Repository
```
git clone https://github.com/yourusername/raspberry-pi-educational-robot.git
cd raspberry-pi-educational-robot
```

### 2: Install Dependencies

Make sure you have Python 3 and pip installed. Then run:
```
pip install -r requirements.txt
```

This installs all necessary Python libraries, including opencv-python, gpiozero, and others used for camera streaming, motor control, and connectivity.

### 3: Hardware Assembly
- Components Required:

Raspberry Pi 5 – The main controller running the robot’s code.

PiCamera 2 – Captures video for object tracking and AI extensions.

Motor Driver (L298N or similar) – Interfaces between the Pi and DC motors.

DC Motors (x2) – Drive the left and right wheels.

Robot Chassis – Holds all components together.

Wheels (x2) – Mounted on the motor shafts.

Caster Wheel (x1) – For balance and free movement.

LiPo Battery (7.4V or similar) – Powers the motors.

Power Bank (5V, 2A or higher) – Powers the Raspberry Pi independently.

- Wiring Overview

Connect the motor driver input pins to the designated GPIO pins on the Pi (as defined in your code).

Attach the motors to the driver outputs.

Power the driver module using the LiPo battery.

Use a separate power bank for the Pi to prevent current fluctuations.

Plug in the PiCamera 2 ribbon cable to the CSI port.

* Ensure common ground between the Raspberry Pi and the motor driver for proper signal communication.

### 4: Software Configuration
1. Enable Camera and GPIO Access

Run the Raspberry Pi configuration tool:
```
sudo raspi-config
```

- Enable Camera Interface

- Enable GPIO/I2C/SPI

- Reboot the Pi after changes

2. Connect Raspberry Pi Remotely

Install and configure Raspberry Pi Connect (for remote access and testing):
```
sudo apt update
sudo apt install raspberrypi-connect
```

Once installed, you can view and control the Pi remotely from your browser.

### 5: Running the Robot Program

To start the robot’s control script:
```
computer_vision.py
```

This initializes the motor driver, camera feed, and GPIO pins.
Currently, the robot supports basic movement controls (forward, backward, left, right, stop) via code execution.

Obstacle detection and avoidance using LIDAR will be integrated in future updates.

### 6: Testing & Troubleshooting

Verify motor polarity — reverse GPIO assignments if direction is incorrect.

If the camera doesn’t initialise, check ribbon seating and libcamera permissions.

Always test each subsystem (motors, camera, connectivity) separately before combining them.

## Educational Impact

The robot serves as a practical teaching tool for:

- Understanding **embedded systems** and **sensor integration**.  
- Learning **robotics fundamentals** such as motion control and feedback loops.  
- Introducing students to **AI and automation principles** through voice-based interaction.  

This aligns with the broader goal of **enhancing hands-on STEM learning** across Kenyan schools and innovation spaces.

---

## Author

**Cindy Mugure**  
Final Year Project – BSc. Computer Science  
2025 

