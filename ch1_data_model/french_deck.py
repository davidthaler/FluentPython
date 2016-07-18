import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    
    def __len__(self):
        '''
        Get number of cards in deck.

        >>> len(FrenchDeck())
        52
        '''
        return len(self._cards)

    def __getitem__(self, position):
        '''
        Get a card at a position in the deck.

        >>> deck = FrenchDeck()
        >>> deck[0]
        Card(rank='2', suit='spades')
        >>> deck[:3]
        [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
        '''
        return self._cards[position]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
