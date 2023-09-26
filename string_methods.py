actor = "Chris Hemsworth"

a2 = actor + " (Thor)"
print(f"a2: {a2}")
print(f"'ems' in actor: {'ems' in actor}")
print(f"'xyz' in actor: {'xyz' in actor}")
print(f"len(actor): {len(actor)}")

print(f"actor.upper(): {actor.upper()}")
a3 = actor.upper()
print(f"a3: {a3}")
print(f"actor.count('h'): {actor.count('h')}")
print(f"actor.count('wor'): {actor.count('wor')}")
print(f"actor.count('spam'): {actor.count('spam')}")
print(f"actor.lower().count('h'): {actor.lower().count('h')}")

x = "foo"
x = "bar"
print(f"x: {x}")
x = x + "room"
print(f"x: {x}")

x = x.upper()
print(f"x: {x}")

print(f"actor.startswith('Chris'): {actor.startswith('Chris')}")
print(f"actor.startswith('Liam'): {actor.startswith('Liam')}")
#  .endswith()

print(f"actor.find('is'): {actor.find('is')}")
print(f"actor.find('Chris'): {actor.find('Chris')}")
print(f"actor.find('Liam'): {actor.find('Liam')}")


bytes = ['192', '168', '1', '47']
dot = "."
ip_address = dot.join(bytes)
print(f"ip_address: {ip_address}")

s = "     All my exes live in Texas      "
print(f"s: |{s}|")
print(f"s.lstrip(): |{s.lstrip()}|")
print(f"s.rstrip(): |{s.rstrip()}|")
print(f"s.strip(): |{s.strip()}|")
print()
raw_value = "$57.93"
value = raw_value.lstrip('$')
print(f"raw_value: {raw_value}")
print(f"value: {value}")

file_name = "wombat.py"
trimmed_name = file_name.removesuffix('.py')
print(f"trimmed_name: {trimmed_name}")

names = "John Paul George Ringo"
beatles = names.split()
print(f"beatles: {beatles}")

names = "Manny:Moe:Jack"
pep_boys = names.split(':')
print(f"pep_boys: {pep_boys}")



