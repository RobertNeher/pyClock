import random
from PIL import Image

def random_Color(tuple: bool = False) -> str:
  rgb = random.sample(range(255), 3)
  if tuple:
    return (rgb[2], rgb[1], rgb[0])
  else:
    return f"#{rgb[2]:02x}{rgb[1]:02x}{rgb[0]:02x}"
  
def recolorMoon(randomColor: bool) -> Image:
    if not randomColor:
      return Image.open("./assets/FullMoon.png")

    picture = Image.open("./assets/FullMoon.png")
    width, height = picture.size

    for pictX in range(0, width):
        for pictY in range(0, height):
            picture.putpixel((pictX, pictY), random_Color(tuple=True))

    return picture
