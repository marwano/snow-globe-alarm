from adafruit_circuitplayground.express import cpx
import time

TONES = dict(low=800, high=960)
RGB = dict(black=[0, 0, 0], blue=[0, 0, 255], green=[0, 255, 0],
           cyan=[0, 255, 255], red=[255, 0, 0], magenta=[255, 0, 255],
           yellow=[255, 255, 0], white=[255, 255, 255])
CYCLE = ['cyan', 'blue', 'magenta', 'red', 'green', 'yellow']


def beep(frequency=TONES['high']):
    cpx.play_tone(frequency, 0.4)


def alarm():
    for i in range(3):
        cpx.pixels.fill(RGB['red'])
        beep(TONES['high'])
        cpx.pixels.fill(RGB['black'])
        beep(TONES['low'])


def detect():
    colors = ['green'] * 10 + ['black'] * 10
    for color in colors:
        if cpx.touch_A2:
            alarm()
        cpx.pixels.fill(RGB[color])
        time.sleep(0.05)


def rainbow():
    for color in CYCLE:
        for i in range(10):
            cpx.pixels[i] = RGB[color]
            time.sleep(0.3)


def main():
    cpx.pixels.brightness = 1.0
    beep()
    while True:
        if cpx.switch:
            rainbow()
        else:
            detect()


main()
