# from scipy.misc import imread, imsave, imresize
from PIL import Image


def main():
    try:
        filename = "cat.jpg"
        with Image.open(filename) as image:
            width, height = image.size
        print(width, height)
        # Image.size gives a 2-tuple and the width, height can be obtained

        # Relative Path
        img = Image.open(filename)

        # Angle given
        img = img.rotate(180)

        # Saved in the same relative location
        img.save("rotated_cat.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()