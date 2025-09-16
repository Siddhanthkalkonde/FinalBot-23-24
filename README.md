# FinalBot-23-24

## Overview

FinalBot-23-24 is a comprehensive bot application repo developed during the 2023-24 academic year. This project represents the culmination of learning and development in autonomous bot technologies and autonomous navigation. 

## Features

- ABU Robocon Theme-Based Bot 
- Autonomous Navigation 
-Object detection and Tracking 
- smart Distance Measurement 

## Technology Stack

- **Programming Language**: Python 3.9 +
- **Computer Vision**: OpenCV, YOLOv8 (Ultralytics)
- **Depth Sensing**: Intel RealSense Camera
- **Hardware Control**: Arduino integration (Cytron motor driver)
- **Machine Learning**: Custom trained YOLO model
- **Libraries:
  - `supervision` - Detection visualization
  - `numpy` - Mathematical operations
  - `argparse` - Command line interface

## Prerequisites

Before running this project, make sure you have the following installed:

- **Python 3.9+**
- **Intel RealSense SDK** (for depth camera support)
- **Arduino IDE** (for motor controller firmware)
- **CUDA-compatible GPU** (recommended for YOLOv8 performance)

### Hardware Requirements

- Intel RealSense Depth Camera
- Arduino-compatible microcontroller
- Cytron motor driver board
- Motors and wheels for mobility - Mainly $ wheel Mechannum / 4-wheel omni 
- IR sensors for proximity detection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Siddhanthkalkonde/FinalBot-23-24.git
cd FinalBot-23-24
```

2. Install Python dependencies:
```bash

# for windows use pip / for linux global env use pip3 (recommended)
pip install opencv-python
pip install ultralytics
pip install supervision
pip install numpy
pip install pyrealsense2

#upgrade pip after installation
pip install --upgrade pip
```

3. Install Intel RealSense SDK:
```bash
# For Ubuntu/Debian
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main"
sudo apt-get update
sudo apt-get install librealsense2-dkms librealsense2-utils librealsense2-dev
```

4. Set up the trained model:
```bash
# Place your trained YOLOv8 model in the appropriate directory
# Update the model path in the main script:
# model = YOLO("/path/to/your/trained_model.pt")
```

5. Configure Arduino:
```bash
# Use arduino Serial python File to communicate woth arduino via serial 

```



## Usage

### Running the Bot

```bash
# Start the detection and tracking system
python main.py

# Run with custom webcam resolution
python main.py --webcam-resolution 640 480

# Run with default high resolution
python main.py --webcam-resolution 700 700
```

### Core Functionality

The bot provides real-time object detection and tracking with the following capabilities:

#### Object Detection and Tracking
```python
# Initialize the detection system
dc = DepthCamera()
model = YOLO("/path/to/your/trained_model.pt")

# Main detection loop
ret, depth_frame, color_frame = dc.get_frame()
frame = track_closest_object(color_frame, model, box_annotator, depth_frame)
```

#### Motor Control Commands
```python
# Initialize motor controller
motor_controller = Cytron_driver()

# Movement commands
motor_controller.forward(0.3)           # Move forward at 30% speed
motor_controller.angle_M(0, 0.3)        # Rotate right at 30% speed  
motor_controller.angle_M(1, 0.3)        # Rotate left at 30% speed
motor_controller.stop(0)                # Stop all movement
motor_controller.ir_in()                # Activate IR sensor input
motor_controller.move_trigno(0.3, 0, angle) # Trigonometric movement
```

### Key Features in Action

#### Real-time Detection
- **Object tracking**: Automatically tracks the closest detected object
- **Color region detection**: Identifies objects in Blue, Green, or Red regions
- **Distance calculation**: Uses depth camera for precise distance measurements
- **Angle calculation**: Computes angles for precise navigation

#### Navigation Logic
```python
# Automatic turning based on object position
if angle > 15:
    motor_controller.angle_M(0, 0.3)    # Turn right
elif angle < -15:
    motor_controller.angle_M(1, 0.3)    # Turn left  
elif -15 <= angle <= 15:
    motor_controller.forward(0.3)       # Move forward
```

#### Proximity Actions
```python
# Close object detection (< 650mm)
if distance < 650:
    motor_controller.ir_in()            # Activate collection mechanism

# Stop when very close (< 400 pixels)
if distance_to_midpoint < 400:
    motor_controller.stop(0)            # Emergency stop
```

### Command Line Arguments

| Argument | Description | Default | Example |
|----------|-------------|---------|---------|
| `--webcam-resolution` | Set camera resolution (width height) | [700, 700] | `--webcam-resolution 640 480` |

### Runtime Controls

- **ESC key**: Exit the application safely
- **Real-time display**: Live video feed with detection overlays
- **Automatic control**: Bot operates autonomously once started```


### Core Functions

#### `initialize_bot()`
Initializes the bot with configured settings.

**Parameters:**
- `config` (dict): Configuration dictionary
- `debug` (bool): Enable debug mode

**Returns:**
- `Bot`: Initialized bot instance

#### `process_command(command, args)`
Processes incoming bot commands.

**Parameters:**
- `command` (str): Command name
- `args` (list): Command arguments

**Returns:**
- `Response`: Command response object

## Testing

Run the test suite:

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_bot.py

# Run with coverage
python -m pytest --cov=src tests/
```

## Deployment

### Local Development

1. Follow the installation steps above
2. Configure your development environment
3. Run the bot locally for testing

### Production Deployment

1. **Heroku Deployment:**
```bash
heroku create your-bot-name
git push heroku main
heroku config:set BOT_TOKEN=your_token
```

2. **Docker Deployment:**
```bash
docker build -t finalbot .
docker run -d --name finalbot-container finalbot
```

## Performance Monitoring

The bot includes built-in monitoring features:

- Response time tracking
- Error rate monitoring
- Resource usage analytics
- Command usage statistics

Access monitoring dashboard at: `http://localhost:8080/dashboard` (if web interface is enabled)

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature`
6. Submit a pull request

### Development Guidelines

- Follow PEP 8 style guide (for Python) or appropriate style guide for your language
- Write comprehensive tests for new features
- Update documentation for any new functionality
- Ensure all tests pass before submitting PR

## Troubleshooting

### Common Issues

**Bot not responding to commands:*
- Verify env variables and weights of models , and  realsense depth connectivvity 
- Check connectivity

**Database connection errors:**
- Verify database URL is correct
- Ensure database server is running
- Check connection permissions

**High memory usage:**
- Review logging levels
- Check for memory leaks in custom code
- Monitor background processes

### Debug Mode

Enable debug mode for detailed logging:

```bash
python main.py --debug
```

Check logs in the `logs/` directory for detailed error information.



---

**Developed with ❤️ by Siddhanth Kalkonde**

*Last updated: September 2025*
