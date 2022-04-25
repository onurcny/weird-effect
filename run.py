from PIL import Image




im = Image.open(f'./grey.png').convert('RGBA')

color, x, y = 0, 0, 0

while y < 16:

    while x < 16:
        print("x: "+str(x)+", y: "+str(y)+", color: "+str(color))
        im.putpixel((x, y), (color, 255, 255))

        color += 1
        x += 1

    x = 0
    y += 1

im.save("./aquatowhite.png")