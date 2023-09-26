list1 = list()   # empty list
list2 = [1, 2, 3]  # initialized list
list3 = []  # empty list with less typing 
list4 = list(list2)   # initialize with some other **iterable**

print(f"list2[0]: {list2[0]}")

cities = []  # new list
cities.append('New Orleans')
print(f"cities: {cities}")
cities.append('Seattle')
print(f"cities: {cities}")
cities.insert(0, "Durham")
print(f"cities: {cities}")
cities.insert(2, "Cincinnati")
print(f"cities: {cities}")
cities.append('Portland')
cities.insert(1, "Poughkeepsie")
print(f"cities: {cities}")

more_cities = ['Des Moines', 'Springfield', 'Metropolis']
print(f"len(cities): {len(cities)}")
cities.extend(more_cities)  
print(f"len(cities): {len(cities)}")
print(f"cities: {cities}")

#  LIST.append(obj)  LIST.insert(pos, obj)    LIST.extend(iterable)

cities[0] = "Raleigh"
print(f"cities: {cities}")
# cities[99] = "Los Angeles"   INVALID

del cities[0]
print(f"cities: {cities}")

city = cities.pop()  # copy last element to city and then remove last element
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(2)
print(f"city: {city}")
print(f"cities: {cities}")

import sys
del sys.argv[0]   # remove script name
#  or script_name = sys.argv.pop(0)

cities.remove('Springfield')
print(f"cities: {cities}")

#  def LIST[pos]    value = LIST.pop()  value = LIST.pop(pos)  LIST.remove(value)

print(f"cities.index('Seattle'): {cities.index('Seattle')}")
print()

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[13]: {fruits[13]}")
print(f"len(fruits): {len(fruits)}")
# print(f"fruits[21]: {fruits[21]}")
# print(f"fruits[len(fruits)-1]: {fruits[len(fruits)-1]}")
print(f"fruits[-1]: {fruits[-1]}")

#  LIST[START:SENTINEL]
#  LIST[START=0:STOP=len(list)]
#  LIST[START:STOP:STEP]
print(f"fruits[0:4]: {fruits[0:4]}")

f1 = fruits  # not a new list, just another reference
f2 = fruits[::]  # new list
f3 = list(fruits)  # new list

print(f"fruits[:4]: {fruits[:4]}")   # first 4
print(f"fruits[15:]: {fruits[15:]}")
print(f"fruits[-5:]: {fruits[-5:]}")
print(f"fruits[::2]: {fruits[::2]}")
print(f"fruits[1::2]: {fruits[1::2]}")
print()
print(f"cities: {cities}\n")
for city in cities:
    # city = next-element-of-cities
    if city.startswith('P'):
        continue
    print(city.upper())
print(f"city: {city}")
print()

























