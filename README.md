# snow-globe-alarm
a snow globe that detects intruders


## Installation
Plug in the Circuit Playground Express into your USB port. Then copy over the main.py file.


## Usage
Tap the Circuit Playground to switch between rainbow and alarm mode. When in alarm mode if the A2 sensor detects a 
touch an alarm will sound with flashing red LED lights.


## Teach
The teach.py and rgb.txt files can be copied over to the Circuit Playground to make it easier for students to control
the speaker and leds from the REPL. Below is an example session.

```
>>> from teach import beep, light
>>> beep()
>>> beep(500)
>>> beep(2000)
>>> 
>>> light()
>>> light('red')
>>> light('green', 2)
>>> 
>>> 

```

