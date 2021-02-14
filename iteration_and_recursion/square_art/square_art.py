import sys


def func_01(i):
    return ''.join('# ' if j > i else '. ' for j in range(25))


def func_02(i):
    return ''.join('# ' if i == j else '. ' for j in range(25))


def func_03(i):
    return ''.join('# ' if i == (24 - j) else '. ' for j in range(25))


def func_06(i):
    return ''.join('# ' if ((i < 10) | (j < 10)) else '. ' for j in range(25))


def func_07(i):
    return ''.join('# ' if ((i > 15) & (j > 15)) else '. ' for j in range(25))


def func_08(i):
    return ''.join('# ' if ((i == 0) | (j == 0)) else '. ' for j in range(25))


def func_09(i):
    return ''.join('# ' if ((j > i + 10) |
                            (i > j + 10)) else '. ' for j in range(25))


def func_15(i):
    return ''.join('# ' if (((i - j > 9) & (i - j < 21)) |
                            ((j - i > 9) & (j - i < 21))) else '. '
                   for j in range(25))


def func_19(i):
    return ''.join('# ' if ((i in (0, 24)) |
                            (j in (0, 24))) else '. ' for j in range(25))


def func_20(i):
    return ''.join('# ' if ((i + j) % 2 == 0) else '. ' for j in range(25))


def func_23(i):
    return ''.join('# ' if ((i % 3 == 0) &
                            (j % 2 == 0)) else '. ' for j in range(25))


def func_24(i):
    return ''.join('# ' if (((i - j) == 0) |
                            (24 - j == i)) else '. ' for j in range(25))


figure = {1: func_01,
          2: func_02,
          3: func_03,
          6: func_06,
          7: func_07,
          8: func_08,
          9: func_09,
          15: func_15,
          19: func_19,
          20: func_20,
          23: func_23,
          24: func_24}


def draw(func):
    for i in range(25):
        print(func(i))
    print('\n')


if __name__ == '__main__':

    if len(sys.argv) > 1:
        func_number = int(sys.argv[1])
    else:
        sys.exit()

    if func_number in figure.keys():
        draw(figure[func_number])
    else:
        print('Sorry figure {} is unavailable'.format(func_number))
