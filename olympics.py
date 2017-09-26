#Emily Murphy
#2017-09-26
#olympics.py -olympic rings

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,0)
yellow = Color(0xFFFF00,1)

blueOutline = LineStyle(15, blue)
yellowOutline = LineStyle(15, yellow)
blackOutline = LineStyle(15, black)
redOutline = LineStyle(15, red)
greenOutline = LineStyle(15, green)
yellowOutline = LineStyle(15, yellow)

whiteC1 = CircleAsset(100, blueOutline, white)
whiteC2 = CircleAsset(100, yellowOutline, white)
whiteC3 = CircleAsset(100, blackOutline, white)
whiteC4 = CircleAsset(100, greenOutline, white)
whiteC5 = CircleAsset(100, redOutline, white)

Sprite(whiteC1, (200,200))
Sprite(whiteC2, (300,300))
Sprite(whiteC3, (430,200))
Sprite(whiteC4, (550,300))
Sprite(whiteC5, (670,200))



App().run()