person  = "Andy Griffith"
town = "Mayberry"
value = 39.342685

print(person)   #  sys.stdout.write(str(person) + '\n')
print(town)
print(person, town)  # sys.stdout.write(str(person) + ' ' + str(town) + '\n')

print(person, town, value)
print(person, town, value, sep="#")
print(person, town, value, sep=" // ")
print(person, town, value, sep="")
print(person)
print(town)
print(value)
print(town, end=" ")
print(person, end=" ==> ")
print(value)

#  town: person(value)
print(town + ": " + person + "(" + str(value) + ")")

print(f"{town}: {person}({value})")
print(f"2 + 2 is {2 + 2}")

print("{}: {}({:.3f})".format(town, person, value))

print(f"{town}: {person}({value:.3f})")

pi = 22/7
print(pi)
print(f"{pi:.4f}")

start_value = 1_000_000

print("%s: %s(%.3f)" % (town, person, value))





