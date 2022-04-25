from tkinter.font import Font
from PIL import Image, ImageDraw, ImageFont
from click import getchar



def makeBlackWhite(path):
    im = Image.open(path).convert('RGBA')
    color, x, y = 0, 0, 0

    while y < im.height:
        while x < im.width:
            pix = im.getpixel((x, y))
            c = int((pix[0] * 0.2126 + pix[1] * 0.7152 + pix[2] * 0.0722))
            im.putpixel((x, y), (c, c, c))

            color += 1
            x += 1

        x = 0
        y += 1
    
    return im



def calcCharBrightness(char):
    img = Image.new("RGB",(50,50))
    ImageDraw.Draw(img).text((0,0), char, (255,255,255), font=ImageFont.truetype("Symbol.ttf", size=50))

    wp = 0
    for x in range(50):
        for y in range(50):
            p = img.getpixel((x,y))[0]
            wp += p/255
            
    return wp/(50*50)



def getChars(min,max):
    chars = []
    for i in range(min,max):
        chars.append((calcCharBrightness(chr(i)), chr(i)))
    chars.sort(key = lambda c: c[0])
    return chars




img = makeBlackWhite("exit2.png")
newImg = Image.new("RGB",(10*img.width,10*img.height))
chars = getChars(90,106)



for x in range(img.width):
    for y in range(img.height):
        p = img.getpixel((x,y))[0]
        c = chars[int(p/16)][1]

        ImageDraw.Draw(newImg).text((x*10,y*10), c, (255,255,255), font=ImageFont.truetype("Keyboard.ttf", size=10))


newImg.save("greatestImageOfAllTime.png")
        





