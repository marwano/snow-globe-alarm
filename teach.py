from adafruit_circuitplayground.express import cpx

RGB = dict(black=[0, 0, 0], blue=[0, 0, 255], green=[0, 255, 0],
           cyan=[0, 255, 255], red=[255, 0, 0], magenta=[255, 0, 255],
           yellow=[255, 255, 0], white=[255, 255, 255])


def beep(frequency=900):
    cpx.play_tone(frequency, 0.2)


def get_color(val):
    if val in RGB:
        return RGB[val]
    elif val.isdigit() and len(val) == 3:
        return [int(val[0]) * 255, int(val[1]) * 255, int(val[2]) * 255]
    elif len(val) == 6:
        return [int(val[0:2], 16), int(val[2:4], 16), int(val[4:6], 16)]
    else:
        raise ValueError('invalid color %r' % val)


def led(val='white', position=0):
    cpx.pixels[position] = get_color(val)
