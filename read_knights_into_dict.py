from pprint import pprint

FILE_PATH = "DATA/knights.txt"

def main():
    data = read_data()
    pretty_print(data)
    print()
    print_name_and_color(data)

def read_data():
    data = {}

    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            data[name] = title, color, quest, comment
    return data

def pretty_print(knight_data):
    pprint(knight_data, sort_dicts=False)

def print_name_and_color(knight_data):
    for name, data in knight_data.items():
        print(name, data[1])

main()