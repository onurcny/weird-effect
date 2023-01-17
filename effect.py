from PIL import Image, ImageDraw, ImageFont
import cv2 as cv
import numpy as np


def calcCharBrightness(char):
    img = Image.new("RGB",(50,50))
    ImageDraw.Draw(img).text((0,0), char, (255,255,255), font=ImageFont.truetype("Lato-Black.ttf", size=50))

    brightnessLevel = 0
    for x in range(50):
        for y in range(50):
            p = img.getpixel((x,y))[0]
            brightnessLevel += p/255
            
    return brightnessLevel/(50*50)



def chooseChars(min,max):
    chars = []
    for i in range(min,max):
        chars.append((calcCharBrightness(chr(i)), chr(i)))
    chars.sort(key = lambda c: c[0])
    return chars


def interpolate(x, sourceRange, targetRange):
    return ( ((x-sourceRange[0])*(targetRange[1]-targetRange[0])) / (sourceRange[1]-sourceRange[0]) ) + targetRange[0]





def applyEffect(img: Image.Image, fontSize: int, charCount: int):

    newImg = Image.new("RGB",(img.width, img.height))
    imgResized = img.resize((int(img.width/fontSize), int(img.height/fontSize))).convert("L")
    chars = chooseChars(90,90+charCount)

    for x in range(imgResized.width):
        for y in range(imgResized.height):
            p = imgResized.getpixel((x,y))
            charIndex = int( interpolate(p, (0,255), (0,charCount)) )
            c = chars[charIndex][1]

            ImageDraw.Draw(newImg).text((x*fontSize,y*fontSize), c, (255,255,255), font=ImageFont.truetype("./Lato-Black.ttf", size=fontSize))

    return newImg

def applyAndSave(path, fontSize, charCount):
    img = Image.open(path)
    img = applyEffect(img, fontSize, charCount)
    img.save("effect.png")


applyAndSave("images/test.png", 12, 8)
