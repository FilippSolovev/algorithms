import sys
from power import power_binary_expansion


def main():
    if len(sys.argv) > 2:
        num = float(sys.argv[1])
        exp = int(sys.argv[2])
    else:
        sys.exit()

    output = float(power_binary_expansion(num, exp))
    print(output)


if __name__ == '__main__':
    main()
