#Emily Murphy
#2017-09-22
#name.py - input name and an RGB color code --> print name in middle and background color is RGB input

from ggame import *
blue = Color(0x0000FF,1)
name = input('Enter your name: ')
background = Color(input('Enter RGB code color: '), 1)
outline = LineStyle(10, background)

rectangle = RectangleAsset(1000, 1000, outline, background)
text = TextAsset(name, fill= blue, style= '40pt Times')


Sprite(rectangle)
Sprite(text,(450,250))

App().run()
