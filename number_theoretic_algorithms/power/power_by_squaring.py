import sys
from power import power_by_squaring


def main():
    if len(sys.argv) > 2:
        num = float(sys.argv[1])
        exp = int(sys.argv[2])
    else:
        sys.exit()

    output = float(power_by_squaring(num, exp))
    print(output)


if __name__ == '__main__':
    main()
