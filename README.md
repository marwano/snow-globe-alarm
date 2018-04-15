# snow-globe-alarm
a snow globe that detects intruders


![snow globe](https://user-images.githubusercontent.com/3801994/38782300-e093ab0c-40f9-11e8-926f-66f29d3467af.jpg)

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


## Video
[![intruder alert](http://img.youtube.com/vi/brG66K89dW0/0.jpg)](http://www.youtube.com/watch?v=brG66K89dW0)


## Microscope
The photo below shows the NeoPixel under a digital microscope with a magnification of 200x. The separate red, green and 
blue LEDs are clearly visible.

![NeoPixel microscope](https://user-images.githubusercontent.com/3801994/38782344-b7b28f2c-40fa-11e8-84e3-360b638302b3.jpg)


