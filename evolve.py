#!/Library/Python/2.7/site-packages
import pip
import random
import time
import operator
import math
import sys
import colormath
from colormath.color_objects import LabColor, LCHabColor, SpectralColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976, delta_e_cie1994, delta_e_cie2000, delta_e_cmc
from PIL import Image

def checkDiff(h1, h2):
    rms = math.sqrt(reduce(operator.add,
        map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

def colorCloseEnough(color1, color2):
    rgb1 = sRGBColor(color1[0], color1[1], color1[2])
    rgb2 = sRGBColor(color2[0], color2[1], color2[2])
    lab1 = convert_color(rgb1, LabColor)
    lab2 = convert_color(rgb2, LabColor)

    return delta_e_cie1976(lab1, lab2) < 5000

lowestDiff = 100
img = Image.new('RGB', (100, 100), "white")
pixels = img.load() # create the pixel map
monalisa = Image.open('examples/guernica.png')
monalisapixels = monalisa.load()
found = 0
x = 0
closeEnough = 0


while found == 0:
    x += 1
    xpos = random.randint(0, img.size[0] - 1)
    ypos = random.randint(0, img.size[1] - 1)

    newPixels = pixels
    newColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    if colorCloseEnough(newColor, monalisapixels[xpos, ypos]):
        closeEnough += 1
        print closeEnough
        pixels[xpos, ypos] = newColor

    if closeEnough >= 100000:
        img.save('results/best_5000.png')
        sys.exit()


