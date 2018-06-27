# ComplexField.py
#
#
# Spencer Kraisler 6/13/2018
#
# This file contains a class for a scalar field of complex numbers. This is not a 2D vector field, however 
# complex scalar fields are perfectly symmetric to them. Furthermore, complex numbers are uch easier to 
# handle in Python than 2-element arrays.
#
# Mathematically, there is a region U of a continuous 2D vector space and the set of all complex numbers C. A complex 
# scalar field is a function S(x,y) that maps every vector in U (addresses of the pos dict) to a single element of 
# C (values of the pos dict) e.g. S(3,6) = 9+3j
#
# All methods are made with this mathematical aesthetic in mind.
#

from cmath import *
from ColorField import *
from Fields import *

class ComplexField(ScalarField):

    dim = 1
    def __init__ (self, xlength, ylength):
        self.xlength = xlength
        self.ylength = ylength
        self.pos = {}

    def initIdentMap(self, x0, y0):
        for x in range(0, self.xlength):
            for y in range(0, self.ylength):
                self.pos[x, y] = (x - x0) - (y - y0) * 1j

    def initIdentMap(self):
        x0 = self.xlength / 2
        y0 = self.ylength / 2
        for x in range(0, self.xlength):
            for y in range(0, self.ylength):
                self.pos[x, y] = (x - x0) - (y - y0) * 1j

    def zoom(self, mag):
        self.times(1.0 / mag)

    def colorize(self, fast):
        image = ColorField(self.xlength, self.ylength)
        if fast == True:
            mortor = 20
            image.screen.setBackground('black')
            for x in range(0, self.xlength):
                for y in range(0, self.ylength):
                    if ((x % mortor >= 0 and x % mortor <= mortor / 2 - 1) and (y % mortor >= 0 and y % mortor <= mortor / 2 - 1)) or ((x % mortor >= mortor / 2 and x % mortor <= mortor - 1) and (y % mortor >= mortor / 2 and y % mortor <= mortor - 1)):
                        image.pos[x, y] = complexToRGB(self.pos[x, y])   
        else:
            for x in range(0, self.xlength):
                for y in range(0, self.ylength):
                    image.pos[x, y] = complexToRGB(self.pos[x, y])
        return image
