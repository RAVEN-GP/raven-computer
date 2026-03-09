# BFMC - Computer Project

The project contains all the provided code that will run on the PC, and it's made of 4 parts:
- carsAndSemaphoresStreamSIM: The simulated stream. Sends random, simulated data about the semaphores and the cars on the track, just as our servers at the Bosch location.
- trafficCommunicationServer: The simulated server of the challenge. The car can get from this server the IP of the localization device and send to it information during the run (Speed, position, rotation and encountered obstacles.)

## 🌍 Global System Architecture

```mermaid
graph TD
    %% Styling
    classDef infra fill:#2d3748,stroke:#4a5568,color:#fff
    classDef web fill:#2b6cb0,stroke:#63b3ed,color:#fff
    classDef computer fill:#1A4024,stroke:#3D9955,color:#fff
    classDef brain fill:#6b46c1,stroke:#b794f4,color:#fff
    classDef perception fill:#805ad5,stroke:#b794f4,color:#fff
    classDef embedded fill:#744210,stroke:#d69e2e,color:#fff
    classDef sim fill:#2c7a7b,stroke:#4fd1c5,color:#fff
    classDef docs fill:#4a5568,stroke:#a0aec0,color:#fff

    subgraph "Infrastructure & Tools"
        CLI[raven-infrastructure CLI]:::infra
        DOCS[raven-documentation Sphinx]:::docs
    end

    subgraph "Presentation & User Interfaces"
        FUTURA[axel-launch-futura<br>React/Vite Official Web]:::web
        DASH[raven-computer<br>Remote Dashboard / Telemetry]:::computer
    end

    subgraph "High-Level Control (Raspberry Pi)"
        BRAIN[raven-brain-stack<br>Python Multiprocessing]:::brain
        
        subgraph "Perception Pipeline"
            CAMERA[Camera / Frame Receiver]:::perception
            LANEDET[Lane Detection<br>OpenCV IPM & Polyfit]:::perception
            SIGNDET[Sign Detection<br>YOLOv8 + Filters]:::perception
            LOCALIZATION[Localization<br>Odometry & Map Graph]:::perception
            CAMERA --> LANEDET
            CAMERA --> SIGNDET
        end
        
        PLANNER[Planner / FSM<br>Decision Logic]:::brain
        SERIAL[Serial Communication<br>Asynchronous UART]:::brain

        LANEDET -->|Lateral Offset| PLANNER
        SIGNDET -->|Sign Labels| PLANNER
        LOCALIZATION <-->|Pose & Drift Correct| PLANNER
        PLANNER -->|Speed & Steer Commands| SERIAL
    end

    subgraph "Low-Level Control (STM32/RP2040)"
        EMBEDDED[raven-embedded-control C++]:::embedded
        PID[Speed PID & Steering MPC]:::embedded
        SAFETY[Dead Man Switch]:::embedded

        EMBEDDED --- PID
        EMBEDDED --- SAFETY
    end

    subgraph "Simulation"
        SIM[raven-sim Gazebo ROS1]:::sim
    end

    %% Connections
    CLI -.->|"Deploys/Manages"| BRAIN
    CLI -.->|"Flashes"| EMBEDDED
    DASH <-->|"Socket.IO / Telemetry"| BRAIN
    SERIAL <-->|"USB Serial (#cmds / @telemetry)"| EMBEDDED
    SIM -.->|"Provides Camera / ROS / Telemetry"| BRAIN
    SIM <-->|"Simulated Server"| DASH
```

## 🎮 Remote Control Dashboard

A new web-based dashboard has been added to control the car manually.

### Features
- **Real-time Control**: Drive the car using keyboard inputs.
- **Telemetry**: View Speed, Steering Angle, Battery, and IMU data.
- **Connection Status**: visual indicator for Brain connectivity.

### Controls
- **W / Up Arrow**: Accelerate
- **S / Down Arrow**: Brake / Reverse
- **A / Left Arrow**: Steer Left
- **D / Right Arrow**: Steer Right
- **SPACE**: Emergency Brake

### Usage
The dashboard is automatically launched on **Port 5000** when you run:
```bash
raven start manual
```

## The documentation is available in more details here:
[Documentation](https://boschfuturemobility.com/brain/)
