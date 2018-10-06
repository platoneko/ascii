from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

def get_char(r, g, b):
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    return ascii_char[gray * len(ascii_char) // 255]

def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-o', '--output')
    parser.add_argument('--width', type=int, default=80)
    parser.add_argument('--height', type=int, default=80)

    args = parser.parse_args()
    img = args.file
    output = args.output
    width = args.width
    height = args.height
    return img, output, width, height

def make_pic(img, output, width, height):
    im = Image.open(img)
    im = im.resize((width, height), Image.NEAREST)
    txt = []
    for i in range(height):
        for j in range(width):
            txt.append(get_char(*im.getpixel((j, i))))
        txt.append('\n')
    txt = "".join(txt)
    if output:
        with open(output, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)


if __name__ == '__main__':
    img, output, width, height = parse_commandline()
    make_pic(img, output, width, height)