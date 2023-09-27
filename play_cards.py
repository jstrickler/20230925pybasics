from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nellie")
print(f"d1: {d1}")
d2 = CardDeck("Andy")
print(f"d2: {d2}")

print(f"d1.dealer: {d1.dealer}")
print(f"d2.dealer: {d2.dealer}")

d1.dealer = "Rosie"
print(f"d1.dealer: {d1.dealer}")

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)
else:
    print(f"d1.dealer: {d1.dealer}")

d1.shuffle()

print(f"d1.cards: {d1.cards}")

print(repr(d1))

for i in range(5):
    print(d1.draw())
print()

j1 = JokerDeck("Albert")
print(f"j1: {j1}")
j1.shuffle()

print(f"j1.cards: {j1.cards}")


for i in range(5):
    print(f"j1.draw(): {j1.draw()}")
