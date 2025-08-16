[![PyPI version](https://badge.fury.io/py/vrcosc.svg)](https://pypi.org/project/vrcosc/)
![Python](https://img.shields.io/pypi/pyversions/vrcosc.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# VRCOSC

**A project that aims to simplify OSC communication to VRChat in Python.**

This package provides a minimal and easy-to-use client for sending OSC messages to VRChat.
Currently it supports sending text to the chatbox and toggling the chatbox typing indicator, with more features planned soon!

## Requirements
- Python 3.12.*

## Installation
You can install VRCOSC using pip:
```bash
pip install vrcosc
```

## Usage
An example of how you can use VRCOSC:
```python
import vrcosc

# Create a client (default: host=127.0.0.1, port=9000)
vrc = vrcosc.VRCOSC()

# Send a message to the chatbox (default: immediate=True, sound=False)
vrc.chatbox_input("Hello, world!")

# Clear the chatbox contents
vrc.chatbox_input()

# Show/hide the typing indicator
vrc.chatbox_typing(True)
vrc.chatbox_typing(False)
```

## License
This project is licensed under the **GPLv3-only** license.
