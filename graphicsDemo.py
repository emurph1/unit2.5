#Emily Murphy
#2017-09-20
#graphicsDemo.py -

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(10, black) #pixels, color

blueRectangle = RectangleAsset(500, 200, blackOutline, blue) #width, height, outline color, inside color
greenCircle = CircleAsset(100, blackOutline, green) #radius, outline, inside color
redEllipse = EllipseAsset(100, 50, blackOutline, red) #horiz_radius, vertical_radius, outline, inside color
blackLine = LineAsset(50, 100, blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(0,0), (120, 180), (60,300)], blackOutline, red) #list of endpoints
text = TextAsset('Murph', fill=blue, style= 'bold 80pt Times')

Sprite(blueRectangle, (50, 50))
Sprite(greenCircle, (900, 200)) #shape, right, left
Sprite(redEllipse, (900, 400))
Sprite(blackLine, (700, 100))
Sprite(redTriangle, (600, 150))
Sprite(text,(150, 350))

App().run()