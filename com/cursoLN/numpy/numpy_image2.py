from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("plantas.png")
        width, height = img.size
        print(width, height)
        img = img.resize((int(width / 2), int(height / 2)))

        # Saved in the same relative location
        img.save("resized_plantas.png")
    except IOError:
        pass


if __name__ == "__main__":
    main()