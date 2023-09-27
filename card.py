
#  rank + suit

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # human-friendly
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    # code-friendly
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')
    c2 = Card('A', 'Clubs')

#    print(f"c1._rank: {c1._rank}")
    print(f"c1.rank: {c1.rank}")
       
