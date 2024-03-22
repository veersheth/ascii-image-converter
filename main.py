from PIL import Image

ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = old_height/old_width
    new_height = int(aspect_ratio * new_width * 0.55) 
    
    #
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value//range_width]
    return ascii_str

def main(new_width=100):
    path = input("Enter the image path: ")
    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = map_pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_image = "\n".join([ascii_str[i:(i+new_width)] for i in range(0, pixel_count, new_width)])
    print(ascii_image)

    f = open("output.txt", "w")
    f.write(ascii_image)
    print("\n\nwritten to output.txt")

main()