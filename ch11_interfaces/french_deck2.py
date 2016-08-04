import collections

Card = collections.namedtuple('Card', 'rank suit')

class FrenchDeck(object):
    ranks = list('23456789') + ['10'] + list('JQKA')
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
        >>> [card.rank for card in deck[8:14]]
        ['10', 'J', 'Q', 'K', 'A', '2']
        '''
        return self._cards[position]

    def __setitem__(self, key, value):
        '''
        Allows swapping cards and shuffling.
        '''
        self._cards[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
