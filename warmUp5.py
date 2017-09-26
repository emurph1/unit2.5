#Emily Murphy
#2017-09-26
#warmUp5.py - make yellow diamond with name inside (blue)

from ggame import *

yellow = Color(0xFFFF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1, black)
yellowD = PolygonAsset([(200, 0,), (100,100), (200,200), (300,100)], blackOutline, yellow)
name = TextAsset('Emily', fill=blue, style= ' 40pt Times')



Sprite(yellowD,(300, 200))
Sprite(name,(440,270))
App().run()
