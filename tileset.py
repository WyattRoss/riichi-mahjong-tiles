import os

baseurl = "/home/wross/Desktop/riichi-mahjong-tiles/tiles/"
suits = ["Man", "Pin", "Sou"]

for file in os.listdir(baseurl):
    print(f"{baseurl}{file}")
