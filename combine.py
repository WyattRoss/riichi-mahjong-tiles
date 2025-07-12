import os
from PIL import Image

path = "./Export/Regular/"

exclude = ["Blank.png", "Pin5-Dora.png", "Man5-Dora.png", "Sou5-Dora.png", "Back.png", "Front.png"]

front = Image.open(f"{path}Front.png")
for file in os.listdir(path):
    if file in exclude:
        continue
    art = Image.open(f"{path}{file}")
    image = Image.alpha_composite(front, art)
    image.save(f"{file}")
