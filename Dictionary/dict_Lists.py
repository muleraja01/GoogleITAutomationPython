wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for types,colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color,types))