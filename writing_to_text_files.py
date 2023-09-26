fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(f"{fruit.upper()}:{len(fruit)}\n")   #  fruit + '\n'

with open('fruits.txt') as fruits_in:
    with open('fruits2.txt', 'w') as fruits_out:
        for raw_line in fruits_in:
            line = raw_line.rstrip()
            fruit, length = line.split(':')
            fruits_out.write(fruit.title() + '\n')
