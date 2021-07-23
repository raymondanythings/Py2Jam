
from PIL import Image

n = 1

while True:
    try:
        image1 = Image.open(f'src/music/Pictures/image{n}.jpg')

        image1 = image1.resize((800, 600))

        image1.save(f"src/music/images/image{n}.png")

        n += 1

        print(n)
    except:
        break


# y = 67.5
# x = 213
