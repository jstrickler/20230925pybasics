
colors = ['red', 'green', 'purple', 'orange', 'brown',
          'black', 'olive', 'navy', 'white', 'black',
          'pink', 'chartreuse']

rcolors = reversed(colors)
print(f"rcolors: {rcolors}")
# print(f"rcolors[0]: {rcolors[0]}")  INVALID
# print(f"len(rcolors): {len(rcolors)}") INVALID
for color in rcolors:
    print(color)
print('-' * 60)

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)

for i, color in enumerate(reversed(colors)):
    print(i, color)
print('-' * 60)

for i, color in enumerate(colors, 1):
    print(i, color)
print('-' * 60)

for i in range(5):
    print(i)
print()

for i in range(1, 11):
    print(i)
print()

for i in range(5, 101, 5):
    print(i, end=" ")
print('\n')





