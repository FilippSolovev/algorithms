def cast_to_numeric(string):
    if string.find('.') == -1:
        return int(string)
    return float(string)


def read_data(file_name):
    with open(file_name, 'r') as file:
        file.readline()
        content = file.readline().strip()
        array = content.split()
    return [*map(cast_to_numeric, array)]
