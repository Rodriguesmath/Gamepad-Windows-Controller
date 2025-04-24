# Gamepad Controller

This project is a gamepad controller application that allows users to control their computer using an Xbox 360 controller. It maps joystick inputs to keyboard actions and mouse movements, as well as providing volume control functionality.

## Features

- Maps D-Pad movements to keyboard arrow keys.
- Maps controller buttons to keyboard actions (e.g., Enter, Escape, Alt+Tab).
- Controls mouse cursor movement using the right analog stick.
- Adjusts system volume using the triggers on the controller.

## Project Structure

```
gamepad-controller
├── src
│   ├── __init__.py
│   ├── main.py                # Entry point for the application
│   ├── joystick
│   │   ├── __init__.py
│   │   ├── connection.py      # Functions for connecting and verifying the joystick
│   │   ├── events.py          # Handles joystick events and mappings
│   │   └── mapping.py         # Maps joystick triggers to volume control and mouse movement
│   ├── audio
│   │   ├── __init__.py
│   │   └── volume_control.py   # Functions for controlling audio volume
│   └── utils
│       ├── __init__.py
│       └── mouse_control.py    # Functions for mouse control using joystick input
├── requirements.txt            # Lists project dependencies
└── README.md                   # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gamepad-controller.git
   cd gamepad-controller
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Connect your Xbox 360 controller to your computer.
2. Run the application:
   ```
   python src/main.py
   ```

3. Use the controller to navigate and control your computer.

## Dependencies

- `pygame`: For handling gamepad input and graphics.
- `pyautogui`: For simulating keyboard and mouse actions.
- `pulsectl`: For controlling audio volume.
