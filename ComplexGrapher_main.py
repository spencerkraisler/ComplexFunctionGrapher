# main.py

from ComplexField import *
from ColorField import *

screenLength = 800
source = ComplexField(screenLength, screenLength)
source.initIdentMap()
source.zoom(80)

map1 = ComplexField(screenLength, screenLength)
map1.equals(source)
map2 = ComplexField(screenLength, screenLength)
map2.equals(source)
map3 = ComplexField(screenLength, screenLength)
map3.equals(source)


target = map1.raisedTo(2).minus(1).times(map2.plus(-2-1j).raisedTo(2)).dividedBy(map3.raisedTo(2).plus(2+2j))

print('Computed final mapping values')
image = target.colorize(fast=False)
print('Created color field')
image.draw(fast=False)
print('Drew color field')
image.screen.getMouse()
print(0)
