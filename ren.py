from PIL import Image




im = Image.open(f'./1024.png').convert('RGBA')

color, x, y = 0, 0, 0

# print("x: "+str(x)+", y: "+str(y)+", color: "+str(color))

while y < 16:

    while x < 16:

        for i in range(x*64, x*64+64):
            for j in range(y*64, y*64+64):
                im.putpixel((i, j), (255, color, 255))

        color += 1
        x += 1

    x = 0
    y += 1

im.save("./pink.png")