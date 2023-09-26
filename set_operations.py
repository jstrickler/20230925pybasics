c1 = ['red', 'green', 'blue', 'red', 'red', 'red', 'purple', 'black']
c2 = ['black', 'red', 'pink', 'mauve', 'orange', 'yellow', 'blue']

set1 = set(c1)
set2 = set(c2)
set2.add('green')
set1.add('red')
set1.add('navy blue')

print(f"set1: {set1}\n")
print(f"set2: {set2}\n")

print(f"set1 & set2: {set1 & set2}")  # intersection
print(f"set1 ^ set2: {set1 ^ set2}")  # xor  
print(f"set1 | set2: {set1 | set2}")  # union
print(f"set1 - set2: {set1 - set2}")
print(f"set2 - set1: {set2 - set1}")

for color in 'red', 'scarlet', 'indigo', 'magenta', 'black':
    print(color, color in set1)



