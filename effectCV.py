import cv2 as cv
import numpy as np



def calcCharBrightnessCV(char):
    img = np.zeros((50,50,3), np.uint8)
    img = cv.putText(img, char, (0,0), cv.FONT_HERSHEY_SIMPLEX, 50, (255,255,255), 1)

    brightnessLevel = 0
    for x in range(50):
        for y in range(50):
            p = img[x][y][0]
            brightnessLevel += p/255
            
    return brightnessLevel/(50*50)


def chooseChars(min,max):
    chars = []
    for i in range(min,max):
        chars.append((calcCharBrightnessCV(chr(i)), chr(i)))
    chars.sort(key = lambda c: c[0])
    return chars


def interpolate(x, sourceRange, targetRange):
    return ( ((x-sourceRange[0])*(targetRange[1]-targetRange[0])) / (sourceRange[1]-sourceRange[0]) ) + targetRange[0]



def applyEffect(img, fontSize, charCount):

    newImg = np.zeros((img.shape[1], img.shape[0],3), np.uint8)
    imgResized = cv.resize(img,(int(img.shape[1]/fontSize), int(img.shape[0]/fontSize)))
    imgResized = cv.cvtColor(imgResized, cv.COLOR_BGR2GRAY)

    chars = chooseChars(90, 90+charCount)

    for x in range(imgResized.shape[1]):
        for y in range(imgResized.shape[0]):
            p = imgResized.shape[x][y][0]
            charIndex = int( interpolate(p, (0,255), (0,charCount)) )
            c = chars[charIndex][1]

            cv.putText(newImg, c, (x*fontSize, y*fontSize), cv.FONT_HERSHEY_SIMPLEX, fontSize, (255,255,255), 1)
    
    return newImg


def applyAndSave(path, fontSize, charCount):
    img = cv.imread(path)
    img = applyEffect(img, fontSize, charCount)
    cv.imwrite("effectCV.png", img)


applyAndSave("images/test.png",12,8)