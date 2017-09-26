#Emily Murphy
#2017-09-22
#yield.py - make a yield sign

from ggame import *

red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

whiteOutline = LineStyle(5, white)
blackOutline = LineStyle(10, black)
yieldTri = PolygonAsset([(55,50),(150,190), (245, 50)], whiteOutline, white)
yieldTri2 = PolygonAsset([(5,10),(150,250), (295, 10)], whiteOutline, red)
text = TextAsset('YIELD', fill=red, style= 'bold 20pt Times')


Sprite(yieldTri2, (200, 200))
Sprite(yieldTri, (200,200))
Sprite(text, (310,250))

App().run()

