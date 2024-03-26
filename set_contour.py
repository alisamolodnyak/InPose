from PIL import Image


logo = "contours_all/00001_contour.png"
with Image.open(logo) as img_logo:
    img_logo.load()




filename_monastery = "all/00001.png"
with Image.open(filename_monastery) as img_monastery:
    img_monastery.load()

img_monastery.paste(img_logo, (50, 50), img_logo)
img_monastery.show()
