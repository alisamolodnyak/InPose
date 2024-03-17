import os


if __name__ == '__main__':
    os.chdir('all')
    for num, i in enumerate(sorted(os.listdir()), start=1):
        os.rename(i, f'{str(num).rjust(5, "0")}.jpg')
    print(os.listdir())