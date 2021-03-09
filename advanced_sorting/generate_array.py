import os
from random import randint
import struct
import sys


def main():
    if len(sys.argv) > 2:
        array_length = int(sys.argv[1])
        file_name = sys.argv[2]
    else:
        sys.exit()

    with open(file_name, 'wb') as file:
        for i in range(array_length):
            num = randint(0, 65535)
            binary_num = struct.pack('H', num)
            file.seek(0, os.SEEK_END)
            file.write(binary_num)


if __name__ == '__main__':
    main()
