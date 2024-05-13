# This is supposed to be a wallpaper creator, I will finish it later

from PIL import Image, ImageDraw

def create(bgcolor, imagepath, outputpath):
    width, height = 1920, 1080
    bg = Image.new("RGB", (width, height), bgcolor)

    image = Image.open(imagepath)
    image = image.resize((500, 500))

    # Calculate the position to center the image on the background
    x = (width - image.width) // 2
    y = (height - image.height) // 2
  
    bg.paste(image, (x, y))

    bg.save(outputpath)

bgcolor = (0, 0, 0)  # Black
imagepath = "./tg.png"
outputpath = "wp.png"

create(bgcolor, imagepath, outputpath)
