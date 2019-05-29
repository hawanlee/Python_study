from PIL import Image


def dill_crop(image, x, y, w, h):
    crop_image = image.crop((x, y, x+w, y+h))
    return crop_image


def fill_image(image):
    width, height = image.size
    new_image_length = width if width > height else height
    new_image=Image.new(image.mode, (new_image_length))

