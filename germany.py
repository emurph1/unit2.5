#Emily Murphy
#2017-09-22
#germany.py - German flag

from ggame import *

black = Color(0x000000, 1)
red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(5, black)

blackRect = RectangleAsset(500, 100, blackOutline, black)
redRect = RectangleAsset(500, 100, blackOutline, red)
yellowRect= RectangleAsset(500, 100, blackOutline, yellow)

Sprite(blackRect,(300,0))
Sprite(redRect,(300,100))
Sprite(yellowRect,(300,200))

App().run()

