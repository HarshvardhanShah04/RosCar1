# ROSCar1

A basic ROS2 beginner friendly project demonstrating teleoperation, publisher–subscriber communication using custom messages, and WiFi-based control of an ESP32-powered car.

---

## 📌 Overview

This project implements a simple ROS 2 system that runs entirely on a ground station laptop. It is designed as an introductory project to understand how ROS 2 nodes communicate and how to interface ROS with external hardware.

The system uses a teleoperation node to capture user input and publish commands, which are then received by another node and transmitted to an ESP32 over WiFi using socket communication.

---

## 🧠 Key Concepts Demonstrated

* ROS 2 publisher–subscriber communication
* Custom message creation and usage
* Teleoperation using user input
* Decoupled node architecture
* Bridging ROS 2 with external hardware (ESP32)
* Socket-based communication over WiFi

---

## 🏗️ System Architecture

```
[ User Input (Teleop Node) ]
            ↓
[ ROS 2 Topic (Custom Message) ]
            ↓
[ Receiver Node ]
            ↓
[ WiFi Socket Communication ]
            ↓
[ ESP32 Car ]
```

---

## ⚙️ How It Works

1. The teleoperation node captures user input (keyboard or interface).
2. It publishes commands as a custom ROS 2 message.
3. The receiver node subscribes to this topic.
4. The received commands are processed and converted into a format suitable for the ESP32.
5. Commands are sent over WiFi using sockets.
6. The ESP32 receives these commands and drives the car accordingly.

---

## 📡 Design Choice: No ROS on Embedded Side

ROS 2 is not deployed on the ESP32. Instead, a lightweight socket-based communication approach is used.

This keeps the system simple and avoids the complexity of micro-ROS or DDS configuration, making it easier to focus on core ROS 2 concepts.

---

## 🚀 Getting Started

### Prerequisites

* ROS 2 (Humble or compatible)
* Python 3
* ESP32 with WiFi capability

### Steps

1. Clone the repository:

```
git clone <your-repo-url>
cd <repo-name>
```

2. Build the workspace:

```
colcon build
```

3. Source the workspace:

```
source install/setup.bash
```

4. Run the nodes:

```
ros2 run <package_name> <teleop_node>
ros2 run <package_name> <receiver_node>
```

5. Ensure ESP32 is connected to the same WiFi network and listening for socket commands.

---

## 📁 Repository Structure

* `my_robot_controller/` – Core ROS 2 package
* `my_py_node/` – Python nodes for teleop and communication
* Custom message definitions
* Supporting scripts and configurations

---

## 🎯 Purpose

This project was built as an introductory step into ROS 2 to understand:

* How nodes communicate
* How to connect ROS with real hardware

It focuses on clarity and simplicity rather than completeness.

---

## 🧑‍💻 Note

This was one of my early ROS 2 projects. Since then, I have continued improving my understanding and building more advanced systems.

---

## 📄 License

Add your license here.

