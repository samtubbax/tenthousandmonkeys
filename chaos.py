#!/Library/Python/2.7/site-packages
import pip
import random
import time
import operator
import math
import sys
from PIL import Image

def checkDiff(h1, h2):
    rms = math.sqrt(reduce(operator.add,
        map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

lowestDiff = 100
img = Image.new('RGB', (100, 100), "white")
pixels = img.load() # create the pixel map
monalisa = Image.open('examples/mona-lisa.png')
monalisapixels = img.load()
found = 0
x = 0

while found == 0:
    x += 1
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) # set the colour randomly

    diff = checkDiff(img.histogram(), monalisa.histogram())

    if(diff < lowestDiff):
        print diff
        img.save('results/' + str(x) + '.png')
        lowestDiff = diff

