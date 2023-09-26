
person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(f"type(person): {type(person)}")
print(f"person[0]: {person[0]}")
print(f"person[1]: {person[1]}")

#   namedtuple  dataclass

first_name, last_name, product, dob = person   # iterable unpacking

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print(f"people[0][0][0]: {people[0][0][0]}")

values = 5, 9
x, y = values    # not x = values[0]; y = values[1]
print(f"x: {x}")
print(f"y: {y}")
print()

data = [('a', 5), ('m', 32), ('c', 8)]
for letter, number in data:
    print(letter, number)
print()
print('-' * 60)

for first_name, last_name, product, dob in people:
    print(first_name, last_name, dob)
print()










