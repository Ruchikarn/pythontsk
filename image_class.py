from PIL import Image, ImageEnhance

im = Image.open('a.jpg')

cropped_image = im.crop((100, 150, 300, 600))

# cropped_image.show()

cropped_image.save('cropped_image.jpg', 'JPEG')

resize_image = im.resize((400, 400))

# resize_image.show()

rotate_image = im.rotate(90)

# rotate_image.show()
enh = ImageEnhance.Brightness(im)
enh.enhance(1.3).show("30% more brightness")