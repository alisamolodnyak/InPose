import cv2
import difflib
from PIL import Image
import numpy as np
import csv

def resize_image(image_path, result_name):
    img = Image.open(image_path)
    fixed_width = 500
    width_percent = (fixed_width / float(img.size[0]))
    height_size = int((float(img.size[0]) * float(width_percent)))
    new_image = img.resize((fixed_width, height_size))
    new_image.show()
    new_image.save(result_name)


def calc_image_hash(file_name):
    image = cv2.imread(file_name)  # Прочитаем картинку
    resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
    gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
    avg = gray_image.mean()  # Среднее значение пикселя
    ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

    # Рассчитаем хэш
    _hash = ""
    for x in range(8):
        for y in range(8):
            val = threshold_image[x, y]
            if val == 255:
                _hash = _hash + "1"
            else:
                _hash = _hash + "0"

    return _hash


def compare_hash(hash1, hash2):
    l = len(hash1)
    i = 0
    count = 0
    while i < l:
        if hash1[i] != hash2[i]:
            count = count + 1
        i = i + 1
    return count


def compare_image_with_others(filename, number_of_offered=50):
    with open('allhash.csv') as csvfile:
        hashes = list(csv.reader(csvfile, delimiter=';', quotechar='|'))
    hash1 = calc_image_hash(filename)
    filename_hash = sorted(hashes, key=lambda row: compare_hash(hash1, row[1]))[:number_of_offered]
    return list(map(lambda f: f[0], filename_hash))


if __name__ == "__main__":
    x = compare_image_with_others("photo.jpg")
    print(x)
