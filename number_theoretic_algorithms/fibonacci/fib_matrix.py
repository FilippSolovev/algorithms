import sys
from fibonacci import fibonacci_through_matrices


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = fibonacci_through_matrices(num)
    print(output)


if __name__ == '__main__':
    main()
