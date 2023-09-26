d1 = dict()  # empty dict
d2 = {'m': 9, 'b': 8, 'x': 44}
d3 = {}   # empty dict
d4 = dict(name="Bob", city="Topeka")

data = [('color', 'blue'), ('size', 'L'), ('style', 158383)]
d5 = dict(data)
print(f"d4: {d4}\n")
print(f"d5: {d5}\n")

d5['animal'] = 'wombat'
d5['planet'] = 'Neptune'
print(f"d5: {d5}\n")

d5['animal'] = 'coatimundi'
print(f"d5: {d5}\n")

del d5['style']
print(f"d5: {d5}\n")

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
airports['DIA'] = "Denver"

print(f"airports['YCC']: {airports['YCC']}")
print(f"airports['RDU']: {airports['RDU']}")

code = 'ATL'
if code in airports:
    print(f"airports[code]: {airports[code]}")
else:
    print(f"{code} not in dictionary")

print(f"airports.get('ATL', 'Not in dictionary'): {airports.get('ATL', 'Not in dictionary')}")
print(f"airports.get('ATL', 0): {airports.get('ATL', 0)}")
print(f"airports.get('ATL'): {airports.get('ATL')}")

print(f"airports.setdefault('ATL', 'Atlanta'): {airports.setdefault('ATL', 'Atlanta')}")
print(f"airports: {airports}\n")


for code, city in airports.items():
    print(code, city)
print('-' * 60)

print(f"airports.items(): {airports.items()}")
print('-' * 60)

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(code, city)
print('-' * 60)

#  airports.keys()
#  airports.values()
