from PIL import Image, ImageFilter
img = Image.open("Без названия.jpeg")

size = (101, 63)
img.thumbnail(size)
img.save("1.jpg")
print(img.size)
img.show()
img = img.filter(ImageFilter.CONTOUR)
img.save("hehey.jpg")
img.show()
