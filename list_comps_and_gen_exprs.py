fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"f0: {f0}\n")

#    [ value  for var in iterable]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [len(f) for f in fruits if f.startswith('a')]
print(f"f3: {f3}\n")

f4 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 5]
print(f"f4: {f4}\n")

f5 = [(f, len(f)) for f in fruits]
print(f"f5: {f5}\n")

word = "wombat"
letters = [x.upper() for x in word]
print(f"letters: {letters}\n")

fgen = (f.upper() for f in fruits)
print(f"fgen: {fgen}")

fgen2 = (f for f in fgen if len(f) > 8)

for fruit in fgen2:
    print(fruit)






