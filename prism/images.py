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
