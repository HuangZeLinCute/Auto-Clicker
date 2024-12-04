# Auto Clicker（连点器）

This is a computer auto clicker.

operation interface:

![](D:\TBD\AutoClicker\1.png)

## Features

**Auto Click Function**: Automatically clicks on the screen around a specified center point within a defined radius, simulating random click positions.

**Customizable Radius & Frequency**:

- Set the click radius (default: 10 pixels).
- Adjust the click frequency (default: 0.1 seconds).

**Real-Time Mouse Position Display**: The current mouse position is updated and displayed in the GUI.

**Start/Stop Toggle**:

- Toggle the auto clicker on/off using the **F8** hotkey.
- The status is displayed in the GUI (e.g., "Clicker Running" or "Stopped").

**Always on Top**: Option to keep the application window always on top using the "Set Always on Top" button.

**Error Handling**: If the user enters an invalid radius, an error dialog will be shown.

**Randomized Click & Pause**:

- Click intervals are randomized for more natural behavior.
- Random pauses are added every 10 to 30 clicks (1-3 seconds).

## Run wizard

```
# Install package
pip install -r requirements.txt

# Package into executable files
Pyinstaller -F -w -n AutoClicker AutoClicker.py
```
