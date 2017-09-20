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
blackline2 = LineAsset(100, 100, blackOutline2)
blackline3 = LineAsset(-100, 100, blackOutline2)
blackline4 = LineAsset(103, 0, blackOutline2)
blackline5 = LineAsset(103, 0, blackOutline2)
doorLine1 =  LineAsset(0, 100, blackOutline2)
doorline2 = LineAsset(0, 100, blackOutline2)
doorline3 = LineAsset(103, 0, blackOutline2)
doorknob = CircleAsset(3, blackOutline, black)

blackOutline = LineStyle(1, black)

Sprite(paintRectangle, (400, 200))
Sprite(purpleTri, (400, 190))
Sprite(blackline1, (500, 250))
Sprite(blackline2, (499,250))
Sprite(blackline1, (599, 250))
Sprite(blackline3, (599,250))
Sprite(blackline4, (499, 250))
Sprite(blackline5, (499, 350))
Sprite(doorLine1, (500, 400))
Sprite(doorline2, (600, 400))
Sprite(doorline3, (499, 400))
Sprite(doorknob, (580, 450))

App().run()