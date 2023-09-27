fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits)
print(f"f1: {f1}\n")

# str.lower

f2 = sorted(fruits, key=str.lower)   #  str.lower is a *callback*
print(f"f2: {f2}\n")

def ignore_case(e):
    return e.lower()

f3 = sorted(fruits, key=ignore_case)
print(f"f3: {f3}\n")

f4 = sorted(fruits, key=len)
print(f"f4: {f4}\n")

def custom_sort1(fruit):
    return_value = len(fruit), fruit.lower()
    print(f"Sorting {fruit} as {return_value}")
    return return_value

f5 = sorted(fruits, key=custom_sort1)
print(f"f5: {f5}\n")








