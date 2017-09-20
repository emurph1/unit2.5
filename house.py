#Emily Murphy
#2017-09-20
#house.py - create a picture of a house

from ggame import *

paint = Color(0x3399FF,1)
black = Color(0x000000,1)
purple = Color(0x9933FF,1)

blackOutline = LineStyle(10, black)
blackOutline2 = LineStyle(5, black)

paintRectangle = RectangleAsset(300, 300, blackOutline, paint)
purpleTri = PolygonAsset([(6,0), (150,-150), (293, 0)], blackOutline, purple)
blackline1 = LineAsset(0, 100, blackOutline2)
blackline2 = LineAsset(900, 100, blackOutline2)


blackOutline = LineStyle(1, black)

Sprite(paintRectangle, (400, 200))
Sprite(purpleTri, (400, 190))
Sprite(blackline1, (500, 250))
Sprite(blackline2, (900,250))


App().run()