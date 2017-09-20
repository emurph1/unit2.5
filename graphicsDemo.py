#Emily Murphy
#2017-09-20
#graphicsDemo.py -

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1, black) #pixels, color

redRectangle = RectangleAsset(200, 100, blackOutline, blue) #width, height, outline color, inside color

Sprite(redRectangle)

App().run()