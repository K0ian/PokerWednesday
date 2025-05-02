import random  # For shuffling the deck

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♤", "♡", "♢", "♧"]

    def __init__(self, suit, rank):
        """
        :param suit: one of the valid suit symbols
        :param rank: one of the valid rank values
        :raises ValueError: if rank or suit is invalid
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank buddy")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        :param other: another Card object
        :return: True if ranks are equal
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        :param other: another Card object
        :return: True if self has higher rank than other
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        :return: string representation of card (e.g. "Q♡")
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        :return: same as __str__ for display in lists
        """
        return self.__str__()

    @property
    def suit(self):
        """
        :return: suit of the card
        """
        return self._suit

    @property
    def rank(self):
        """
        :return: rank of the card
        """
        return self._rank

class Deck:
    def __init__(self):
        """
        :return: a full deck of 52 Card objects
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        :return: string representation of the full deck
        """
        return str(self._deck)

    def shuffle(self):
        """
        :return: None; shuffles the deck in place
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        :return: Card object dealt from top of the deck
        :raises IndexError: if deck is empty
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()          # Create a new deck
    print(deck)            # Print the ordered deck
    deck.shuffle()         # Shuffle the deck
    print(deck)            # Print the shuffled deck
    print(deck.deal())     # Deal the top card