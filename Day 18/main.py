import colorgram


colors = colorgram.extract("Day 18\image.jpg", 30)

cs = []

for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    cs.append((r, g, b))

print(cs)
