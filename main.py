from adafruit_circuitplayground.express import cpx
import time
import random

STEPS = 50
TONES = dict(low=800, high=960)
COLORS = dict(
    black=[0, 0, 0], blue=[0, 0, 255], green=[0, 255, 0],
    cyan=[0, 255, 255], red=[255, 0, 0], magenta=[255, 0, 255],
    yellow=[255, 255, 0], white=[255, 255, 255])
CHOICES = list(set(COLORS.keys()) - {'white', 'black'})


def beep(frequency=TONES['high']):
    cpx.play_tone(frequency, 0.4)


def alarm():
    for i in range(3):
        cpx.pixels.fill(COLORS['red'])
        beep(TONES['high'])
        cpx.pixels.fill(COLORS['black'])
        beep(TONES['low'])


def watch():
    beep()
    while True:
        colors = ['green'] * 10 + ['black'] * 10
        for color in colors:
            if cpx.touch_A2:
                alarm()
            cpx.pixels.fill(COLORS[color])
            time.sleep(0.05)
            if cpx.tapped:
                return


def rainbow():
    beep()
    levels = [i / STEPS for i in range(STEPS)]
    levels += [i / STEPS for i in range(STEPS, 0, -1)]
    while True:
        base_color = COLORS[random.choice(CHOICES)]
        for level in levels:
            adjusted_color = [int(i * level) for i in base_color]
            cpx.pixels.fill(adjusted_color)
            time.sleep(0.05)
            if cpx.tapped:
                return


def init():
    cpx.detect_taps = 1             # enable single-tap detection
    cpx.pixels.brightness = 1.0     # set maximum brightness


def main():
    init()
    while True:
        rainbow()
        watch()


main()
