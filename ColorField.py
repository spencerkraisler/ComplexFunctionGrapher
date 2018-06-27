# ColorField.py
# Spencer Kraisler 6/13/2018

from graphics import *
from Fields import *
from cmath import *
import colorsys

class ColorField(VectorField):
    dim = 3
    def __init__(self, xLength, yLength):
        self.xLength = xLength
        self.yLength = yLength
        self.pos = {} 
        self.screen = GraphWin('Screen', self.xLength, self.yLength, autoflush = False)
    
    def initIdentMap(self, x0, y0):
        for x in range(0, self.xLength):
            for y in range(0, self.yLength):
                s = (x - x0) + (y - y0) * 1j
                self.pos[x, y] = complexToRGB(s)

    def initIdentMap(self):
        x0 = self.xLength / 2
        y0 = self.yLength / 2
        for x in range(0, self.xLength):
            for y in range(0, self.yLength):
                s = (x - x0) + (y - y0) * 1j
                self.pos[x, y] = complexToRGB(s)

    def draw(self, fast):
        if fast == False:
            for x in range(0, self.xLength):
                for y in range(0, self.yLength):
                    self.screen.plot(x, y, self.pos[x, y])
        else:
            mortor = 20
            self.screen.setBackground('black')
            for x in range(0, self.xLength):
                for y in range(0, self.yLength):
                    if ((x % mortor >= 0 and x % mortor <= mortor / 2 - 1) and (y % mortor >= 0 and y % mortor <= mortor / 2 - 1)) or ((x % mortor >= mortor / 2 and x % mortor <= mortor - 1) and (y % mortor >= mortor / 2 and y % mortor <= mortor - 1)):
                        self.screen.plot(x, y, self.pos[x, y])
        self.screen.flush()

def complexToRGB(s):
    hue = phase(s) / 2.0 / pi
    lightness = (1 - 2.0 ** -(10 * abs(s))) * 0.5
    r, g, b = colorsys.hls_to_rgb(hue, lightness, 1)
    r = int(255 * r)
    g = int(255 * g)
    b = int(255 * b)
    return color_rgb(r,g,b)
