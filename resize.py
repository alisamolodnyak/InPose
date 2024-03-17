from PIL import Image
import numpy as np


def resize_image(image_path, fixed_width=500):
    img = Image.open(image_path)
    width_percent = (fixed_width / float(img.size[0]))
    height_size = int((float(img.size[0]) * float(width_percent)))
    new_image = img.resize((fixed_width, height_size))
    return new_image


def mid_color(image):
    width, height = image.size
    pixels = np.asarray(image)
    top_part = pixels[:height // 2]
    bot_part = pixels[height // 2:]
    mean_top = np.mean(np.mean(top_part, axis=0), axis=0)
    mean_bot = np.mean(np.mean(bot_part, axis=0), axis=0)
    return mean_top, mean_bot


if __name__ == '__main__':
    image = Image.open('image.jpg')
    image.show()
    new_image = resize_image("image.jpg")
    new_image.show()
    print(mid_color(image))