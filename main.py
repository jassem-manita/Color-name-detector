import webcolors
import matplotlib.pyplot as plt

def closest_color(rgb):
    differences = {}
    for color_hex, color_name, in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                         (g - rgb[1]) ** 2,
                         (b - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]



print('Enter a valid color HEX code ')
print('Exemple : 255, 0, 0 => RED ')
r=int(input("r : "))
g=int(input("g : "))
b=int(input("b : "))
color =(r,g,b)
try:
    cname=webcolors.rgb_to_name(color)
    print(f"The color is exactly {cname}")
except:
    cname= closest_color(color)
    print(f"The color is closest to {cname}")

plt.imshow([[color]])
plt.show()