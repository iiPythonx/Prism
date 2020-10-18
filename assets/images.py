# Modules
import io
from requests import get
from PIL import Image, ImageOps

# Begin functions
def compile(data):

    """Compiles raw data into an image array"""

    arr = io.BytesIO()

    data.save(arr, format = "PNG")

    arr.seek(0)

    return arr

def imagefromURL(url):

    """Returns raw image data from an URL"""

    r = get(url, timeout = 2)

    image = Image.open(io.BytesIO(r.content))

    return image

def compileGIF(images, duration):

    """Compiles raw data into a GIF array"""
        
    arr = io.BytesIO()
    
    images[0].save(arr, "GIF", save_all = True, append_images = images[1:], optimize = False, duration = duration, loop = 0)
    
    arr.seek(0)

    return arr

def imagetoascii(url):

    """Pretty damn self explanatory"""

    im = ImageOps.flip(imagefromURL(url).resize((300, 300)).rotate(90).convert("RGB"))

    im = im.resize((int(list(im.size)[0] / 3) - 60, int(list(im.size)[1] / 3)))

    total_str = ""

    for i in range(im.width):

        for j in range(im.height):

            br = round(sum(im.getpixel((i, j))) / 3)

            if br in range(0, 50): total_str += "."
            elif br in range(50, 100): total_str += "/"
            elif br in range(100, 150): total_str += "$"
            elif br in range(150, 200): total_str += "#"
            else: total_str += '@'

            total_str += "\n"

    return total_str
