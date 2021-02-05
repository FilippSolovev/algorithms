import sys
from functools import reduce
from itertools import groupby


def get_sum_of_digits(number):
    """Calculates sum of digits in a given number"""
    return sum(map(int, str(number)))


def get_num_of_lucky_tickets(num):
    """Get the number of 'lucky' tickets with Map Reduce flavor.

    Get the count of 2N numbers which have sum of digits in the left part
    equal to ones in the right, i.e. '100001', '157904', '97142289' etc.

    Parameters
    ----------
    num : int
        N in 2N, the number of digits in a half of the ticket number, i.e.
        for tickets like '0000' or '1010' it is 2, for '000000' or '111112'
        it is 3 and so on.

    Returns
    -------
    int
        Count of 'lucky' ticket numbers.
    """

    numbers = range(10**(num))

    # Mapping phase
    sums_of_digits = map(get_sum_of_digits, numbers)
    sum_number_pairs = zip(sums_of_digits, (1 for x in numbers))

    # Sortng phase
    sorted_pairs = sorted(sum_number_pairs, key=lambda row: row[0])

    # Reducing phase
    collected = (reduce(lambda x, y: (x[0], x[1] + y[1]), group)
                 for _, group in groupby(sorted_pairs, key=lambda row: row[0]))

    output = sum((cnt**2 for summ, cnt in collected))

    return output


def main():
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
    else:
        sys.exit()

    output = get_num_of_lucky_tickets(num)
    print(output)


if __name__ == '__main__':
    main()
