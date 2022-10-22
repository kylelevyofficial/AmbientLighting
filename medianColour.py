from PIL import Image, ImageStat, ImageEnhance

def find_median_colour(imgpath):

    #Obtaining the median colour
    imgpath = imgpath
    img = Image.open(imgpath)

    median = ImageStat.Stat(img).median

    new_Image = Image.new("RGB", img.size, tuple(median))

    #Getting the RGB Values of the median Image

    # Increase saturation for LED to be more clear
    img = new_Image
    filter = ImageEnhance.Color(img)
    new_image2 = filter.enhance(5)
    filter2 = ImageEnhance.Brightness(new_image2)
    new_image3 = filter2.enhance(3)
    new_Image = new_image3

    new_Image = new_Image.convert('RGB')
    r, g, b = new_Image.getpixel((5,5))
    RGB_values = r,g,b

    # new_Image.show()

    print(RGB_values)

    return RGB_values
