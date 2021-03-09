import struct
import os


def write_num(num, file):
    binary_num = struct.pack('H', num)
    file.seek(0, os.SEEK_END)
    file.write(binary_num)


def external_merge(left, right):
    with open('tape.bin', 'bw') as array:
        with open(left, 'rb') as tape_b, open(right, 'rb') as tape_c:
            while True:
                left_head = tape_b.read(2)
                if not left_head:
                    break
                left_head = struct.unpack('H', left_head)[0]

                right_head = tape_c.read(2)
                if not right_head:
                    tape_b.seek(-2, os.SEEK_CUR)
                    break
                right_head = struct.unpack('H', right_head)[0]

                if left_head < right_head:
                    write_num(left_head, array)
                    tape_c.seek(-2, os.SEEK_CUR)
                else:
                    write_num(right_head, array)
                    tape_b.seek(-2, os.SEEK_CUR)

            # Checking if any element was left
            while True:
                left_head = tape_b.read(2)
                if not left_head:
                    break
                left_head = struct.unpack('H', left_head)[0]
                write_num(left_head, array)

            while True:
                right_head = tape_c.read(2)
                if not right_head:
                    break
                right_head = struct.unpack('H', right_head)[0]
                write_num(right_head, array)


def external_merge_sort(array):
    # return tape_d -> tape_a
    pass


def main():
    # test for external_merge
    external_merge('tape_a.bin', 'tape_b.bin')


if __name__ == '__main__':
    main()
