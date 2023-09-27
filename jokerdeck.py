from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def __init__(self, dealer):
        super().__init__(dealer)
        self._make_deck("spam", "ham")

    def _make_deck(self, thing1, thing2):
        super()._make_deck()
        for i in range(2):
            joker = Card('JOKER', None)
            self._cards.append(joker)


