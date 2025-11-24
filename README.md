# ChipuRobot: A Raspberry Pi–Based Educational Robotics Kit for Public Secondary Schools in Kenya

## Background

As Kenya transitions into the Competency-Based Curriculum (CBC), education at the senior secondary level is becoming increasingly oriented towards specialization and career readiness. Pathways such as Science, Technology, Engineering, and Mathematics (STEM) are being emphasized, with learning outcomes designed to foster pre-career practical exposure.

However, public secondary schools often lack access to modern tools, digital labs, or practical robotics resources that can fulfill these learning objectives. Most STEM teaching in such institutions is either theoretical or delivered via static demonstrations. Interactive, hands-on learning, critical for fostering innovation, curiosity, and technical skills, is limited.

This project addresses this gap by introducing a practical robotics kit that students and teachers can use in diverse ways: in class for technical demonstrations, in clubs or competitions for extracurricular exploration, or during independent tinkering. The kit is adaptable, modular, and scalable.

## Problem Statement

Despite the increasing demand for robotics and automation skills globally, most Kenyan public secondary schools lack the infrastructure, tools, or technical expertise required to introduce students to robotics in a meaningful way. While private schools and international curricula increasingly integrate robotics, public schools are often left behind due to high costs of kits, limited digital resources, or insufficient training.

## Project Objective

To develop a modular, open-ended educational robotics kit that empowers students in public Kenyan secondary schools to explore and learn robotics through hands-on, interactive experimentation; independent of internet connectivity or high-maintenance components.

## Justification

This kit is designed not just as a static teaching tool but as a flexible, student-driven learning aid. Its use of Raspberry Pi, camera-based vision, and offline-capable models ensures functionality even in low-resource environments. Unlike traditional kits, it includes:

- Interactive modules (voice, vision, navigation)
- Locally crafted materials (laser-cut chassis, 3D-printed mounts)
- Replaceable and maintainable parts
- Scalable architecture for further projects

The robot serves as both an introduction to robotics and a launchpad for creative innovation among learners.

---

## Project Structure

```bash
.
├── .github/                # GitHub classroom configuration
├── README.md               # Project documentation
├── autonomous_navigation.py # Module 2: Autonomous Navigation
├── user_detection.py       # Module 1: User Detection
├── voice_control.py        # Module 3: Voice-Controlled Movement
├── requirements.txt        # Project dependencies
```

---

## Component Overview

### Hardware

| Component          | Function                                      |
| ------------------ | --------------------------------------------- |
| Raspberry Pi 5     | Primary microcontroller and compute board     |
| DC Motors          | Movement and locomotion                       |
| L298N Motor Driver | Interfaces motor with Raspberry Pi PWM output |
| Pi Camera 2        | Vision for user detection and navigation      |
| USB Microphone     | Captures voice commands                       |
| LiPo Battery Pack  | Power source for motors                       |
| Power Bank         | Power for the Raspberry Pi                    |
| Laser-Cut Chassis  | Mounting frame for all components             |
| 3D-Printed Mounts  | Modular component holders (camera, Pi, etc.)  |

### Software Tools

- Python 3
- Raspberry Pi OS 
- OpenCV
- gpiozero
- picamera2
- PyAudio
- Vosk (speech recognition engine)

---

## Architecture Overview

The robot consists of three main learning modules:

1. **User Detection**  
   Uses the Raspberry Pi camera and AI models for person detection. The robot follows a detected person using bounding-box logic, steering and adjusting based on their position.

2. **Autonomous Navigation**  
   Applies grayscale image processing to detect obstacles using only a camera. Upon detecting an obstacle, the robot dynamically alters its path through timed motor turns.

3. **Voice Control**  
   Implements voice-activated movement using the Vosk speech recognition engine. Recognizes keywords like "forward", "left", "right", and translates them into motor actions.

Each module is independently executable and introduces key robotics concepts: vision, control logic, speech processing, and automation.

---

## Comparative Analysis of Robotics Kits

| Kit               | Learning Curve    | Local Maintenance | Interactivity | Cost     | Offline Use | Modularity |
| ----------------- | ----------------- | ----------------- | ------------- | -------- | ----------- | ---------- |
| LEGO Mindstorms   | Moderate          | Low               | High          | High     | Limited     | High       |
| Arduino Kits      | High              | Moderate          | Low           | Moderate | Yes         | Moderate   |
| VEX Robotics      | Moderate          | Low               | High          | High     | No          | High       |
| **ChipuRobot**    | Beginner–Friendly | High              | High          | Moderate | Yes         | High       |

> Note: ChipuRobot prioritizes offline, customizable interaction using lightweight, pretrained models, designed to work without cloud APIs or advanced infrastructure.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/CindyMG/chipurobot.git
cd chipurobot
```

### 2. Install Python Dependencies

Ensure Python 3.9+ and pip are installed. Then run:

```bash
pip install -r requirements.txt
```

### 3. Enable Interfaces

Run Raspberry Pi configuration:

```bash
sudo raspi-config
```

Enable:

- Camera
- I2C
- SPI
- GPIO
- SSH (optional)

Reboot afterward.

### 4. Run Any Module

Each module has a standalone script:

```bash
python3 user_detection.py         # Module 1: Person Following
python3 autonomous_navigation.py  # Module 2: Obstacle Avoidance
python3 voice_control.py          # Module 3: Voice Commands
```

Make sure connected peripherals (motors, camera, mic) are properly wired.

---

## Project Demonstration

Kindly access this link to view the project demo: https://drive.google.com/file/d/1ZYVDbMH3jkDoCxLr-mEOJyrBzP6gV0bF/view?usp=sharing

## Educational Value

The kit allows learners to:

- Build, test, and iterate real-world automation systems
- Understand core robotics principles (e.g., motion planning, control logic)
- Explore AI concepts through vision and voice interfaces
- Engage in creative problem-solving and tinkering

This reinforces CBC competencies in computational thinking, innovation, and applied science.

---

## Author

**Cindy Mugure**  
Final Year Project – BSc. Computer Science  
2025
