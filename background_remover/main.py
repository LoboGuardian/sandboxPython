import sys
import os


def read_args(argv):
    output = {}
    i = 1
    while i < len(argv):
        if argv[i] == '-f' and len(argv) > i + 1:
            output['filepath'] = argv[i + 1]
            i += 2
        else:
            i += 1
    return output


def process_path(path):
    if not os.path.exists(path):
        return None
    
    binary_data = None
    
    try:
        with open(path, 'rb') as f:
            binary_data = f.read()
    except Exception as e:
        print("Error reading file: {0}".format(e))
    finally:
        return binary_data


def read_type_file(data):
    if len(data) >= 8 and data[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    else:
        return None


def binary_to_png(data):
    width = int.from_bytes(data[16:20], 'big')
    height = int.from_bytes(data[20:24], 'big')
    color_depth = data[24]

    offset = 33
    img = bytearray{}

    while offset < len(data):
        length = int.from_bytes(data[offset:offset + 4], 'big')
        chunk_type = data[offset + 4:offset + 8]
        if chunk_type == b'IDAT':
            img.extend(data[offset + 8:offset + 8 + length])
        offset += 12 + length

    img_matrix = []
    offset = 0
    for row in range(height):
        row_pixel = []
        for col in range(width):
            if color_depth == 8 and len(img) >= offset + 3:
                r = img[offset]
                g = img[offset + 1 ]
                b = img[offset + 2]
                row_pixel.append(r, g, b)
                offset += 3
        img_matrix.append(row_pixel)
    
    return img_matrix



def main():
    args = read_args(sys.argv)
    if 'filepath' not in args:
        filepath = None
        print("Not filepath found")
        sys.exit(1)
    else:
        binary_data = process_path(args['filepath'])
        if binary_data is None:
            sys.exit(1)

        filetype = read_type_file(binary_data)
        # if(filetype)
5

if __name__ == '__main__':
    main()