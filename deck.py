import random  # For shuffling the deck

class Card:
    """
    Represents a single playing card with a specific suit and rank.

    The Card class encapsulates the characteristics of a standard playing card,
    including its suit (♤, ♡, ♢, ♧) and rank (2 through Ace). Cards are comparable
    based on their rank values only, allowing equality and greater-than comparisons.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♤", "♡", "♢", "♧"]

    def __init__(self, suit, rank):
        """
        Initialize a Card instance with the specified suit and rank after validating them.

        :param suit: str - the suit symbol of the card; must be one of ♤, ♡, ♢, ♧
        :param rank: str - the rank of the card; must be one of 2-10, J, Q, K, A
        :return: None
        :raises ValueError: if the suit or rank is invalid
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank buddy")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        """
        Determine if this card has the same rank as another card.

        :param other: Card - the other Card object to compare against
        :return: bool - True if ranks are equal; False otherwise
        """
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Determine if this card's rank is higher than another card's rank.

        :param other: Card - the other Card object to compare against
        :return: bool - True if this card's rank is higher; False otherwise
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        """
        Provide a human-readable string representation of the card.

        :param: None
        :return: str - string combining rank and suit, e.g. "Q♡"
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Provide the official string representation of the card, suitable for lists.

        :param: None
        :return: str - same as __str__ representation
        """
        return self.__str__()

    @property
    def suit(self):
        """
        Get the suit of this card.

        :param: None
        :return: str - the suit symbol of the card
        """
        return self._suit

    @property
    def rank(self):
        """
        Get the rank of this card.

        :param: None
        :return: str - the rank value of the card
        """
        return self._rank


class Deck:
    """
    Represents a complete standard deck of 52 playing cards.

    The Deck class initializes all 52 unique cards in a fixed order,
    supports shuffling the cards randomly, and dealing cards one by one
    from the top of the deck.
    """

    def __init__(self):
        """
        Initialize the deck by creating all 52 Card objects in standard order.

        :param: None
        :return: None
        """
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        """
        Provide a string representation of the full deck showing all cards.

        :param: None
        :return: str - string representation of the list of Card objects
        """
        return str(self._deck)

    def shuffle(self):
        """
        Randomly shuffle the order of cards in the deck in place.

        :param: None
        :return: None
        """
        random.shuffle(self._deck)

    def deal(self):
        """
        Remove and return the top card from the deck.

        :param: None
        :return: Card - the top Card object from the deck
        :raises IndexError: if the deck is empty when attempting to deal
        """
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()          # Create a new deck
    print(deck)            # Print the ordered deck
    deck.shuffle()         # Shuffle the deck
    print(deck)            # Print the shuffled deck
    print(deck.deal())     # Deal the top card