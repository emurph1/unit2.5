#Emily Murphy
#2017-09-22
#yield.py - make a yield sign

from ggame import *

red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)

whiteOutline = LineStyle(5, white)
yieldTri = PolygonAsset([(6,0),(100,-150), (293, 0)], whiteOutline, white)
yieldTri2 = PolygonAsset([(6,0),(150,250), (293, 0)], whiteOutline, red)


Sprite(yieldTri2, (200, 200))
Sprite(yieldfTri, (200,200))

App().run()

