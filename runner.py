from PIL import Image




im = Image.open(f'./black.png').convert('RGBA')
im = im.resize((1024, 1024))
im.save("./aquatowhite.png")