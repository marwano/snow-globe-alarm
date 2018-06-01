# snow-globe-alarm
a snow globe that detects intruders


![snow globe](https://user-images.githubusercontent.com/3801994/38782300-e093ab0c-40f9-11e8-926f-66f29d3467af.jpg)

## Installation
Plug in the Circuit Playground Express into your USB port. Then copy over the main.py file.


## Usage
Use the Slide switch to change between rainbow and alarm mode. When in alarm mode if the A2 sensor detects a 
touch an alarm will sound with flashing red LED lights.


## Teach
Copy over teach.py to the Circuit Playground to make it easier for students to control
the speaker and leds from the REPL. Below is an example session.

```
>>> from teach import cpx, beep, led
>>> 
>>> # make speaker beep
>>> beep()
>>> 
>>> # make speaker beep at 800Hz 
>>> beep(800)
>>> 
>>> # reduce brightness to a lower more comfortable level
>>> cpx.pixels.brightness = 0.02
>>> 
>>> # set first LED to white
>>> led()
>>> 
>>> # set second LED to red
>>> led('red', 1)
>>> 
>>> # set first LED to blue with hex color code
>>> led('0000ff')
>>> 
>>> # set first LED to Magenta(red on, green off, blue on)
>>> led('101')
```


## Video
[![intruder alert](http://img.youtube.com/vi/brG66K89dW0/0.jpg)](http://www.youtube.com/watch?v=brG66K89dW0)


## Microscope
The photo below shows the NeoPixel under a digital microscope with a magnification of 200x. The separate red, green and 
blue LEDs are clearly visible.

![NeoPixel microscope](https://user-images.githubusercontent.com/3801994/38782400-82a3b5d0-40fb-11e8-976f-27e3399da4cf.jpg)


