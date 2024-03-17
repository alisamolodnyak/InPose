import os
import numpy as np
from PIL import Image
from resize import mid_color
from comparing import calc_image_hash


def main():
    mypath = os.path.dirname(os.path.realpath(__file__))
    folder = 'all'
    mypath = os.path.join(mypath, folder)
    #onlyfiles = [(f, *mid_color(Image.open(os.path.join(mypath, f)))) for f in os.listdir(mypath) if
    #             os.path.isfile(os.path.join(mypath, f))]
    mypath = folder
    onlyfiles = [(f, calc_image_hash(os.path.join(mypath, f))) for f in os.listdir(mypath) if
                 os.path.isfile(os.path.join(mypath, f))]
    for ans in onlyfiles:
        print(*ans, sep='\t')
    #for ans in sorted(onlyfiles):
    #    print(ans[0], *map(lambda x: str(x).replace(".", ","), np.round(ans[1], 1)),
    #          *map(lambda x: str(x).replace(".", ","), np.round(ans[2], 1)), sep='\t')


if __name__ == '__main__':
    main()
