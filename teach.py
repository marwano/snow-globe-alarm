from adafruit_circuitplayground.express import cpx


def beep(frequency=900):
    cpx.play_tone(frequency, 0.2)


def lookup_color(name):
    for line in open('rgb.txt'):
        rgb, line_name = line.strip().split('\t\t')
        if line_name == name:
            return [int(i) for i in rgb.split()]
    raise ValueError('color %r not found' % name)


def light(color='white', position=0):
    cpx.pixels[position] = lookup_color(color)
