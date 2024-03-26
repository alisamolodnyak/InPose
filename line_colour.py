from PIL import Image, ImageDraw

# Open the image
image = Image.open("contours_all/00001_contour.png")

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Get the pixel at coordinates (x, y)
x = 100
y = 200
pixel = image.getpixel((x, y))

# Change the color of the pixel
new_color = (255, 255, 255)  # Red color
draw.point((x, y), fill=new_color)

# Save the modified image
image.save("00001_changed_contour.png")