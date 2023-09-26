import json
from pprint import pprint

with open('DATA/presidents.json') as pres_in:
    pres_data = json.load(pres_in)
    pprint(pres_data)
print('-' * 60)

george = pres_data['presidents'][0]
print(george)
print(f"george['firstname']: {george['firstname']}")
print(f"george['lastname']: {george['lastname']}")
print('-' * 60)

with open('DATA/meteorite_events.json') as meteorites_in:
    met_data = json.load(meteorites_in)
    for record in met_data:
        if 'mass' in record:          
            mass = round(float(record['mass']), 1)
            print(f"{record['name']:30} {mass:10.1f}")


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

with open('people.json', 'w') as people_out:
    json.dump(people, people_out, indent=4)

