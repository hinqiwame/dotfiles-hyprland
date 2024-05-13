from sys import exc_info, argv

helptext = f"""My own wallpaper generator lol

List of arguments required:
    - Background color (e.g. "#000000")
    - Dimension X      (e.g. 1920)
    - Dimension Y      (e.g. 1080)
    - Input picture    (e.g. takizava.png)
    - Output name      (e.g. wp.png)

Example usage:
    {argv[0]} "#000000" 1920 1080 tg.png wp.png
"""

def hextorgb(color):
    color = color.lstrip('#')
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def main(bgcolor, w, h, imagepath, outputpath):
    from PIL import Image, ImageDraw
    width, height = w, h
    bg = Image.new("RGB", (width, height), bgcolor)

    image = Image.open(imagepath)
    image = image.resize((500, 500))

    # Calculate the position to center the image on the background
    x = (width - image.width) // 2
    y = (height - image.height) // 2
  
    bg.paste(image, (x, y))

    bg.save(outputpath)

if __name__ == "__main__":
        try:
            if argv[1] == "--help":
                print(helptext)
            else:
                bgcolor = hextorgb(argv[1])
                main(bgcolor, int(argv[2]), int(argv[3]), argv[4], argv[5])
        except IndexError:
            print(f"You didn't provide enough arguments!\nUse {argv[0]} --help to get info about how to use this tool.")
        except:
            print("Error:", exc_info())
