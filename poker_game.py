from deck import Deck, Card  # Import Deck and Card classes

class PokerHand:
    """
    Represents a poker hand consisting of 5 cards drawn from a deck.

    The PokerHand class deals 5 cards from a given Deck object and provides
    various properties to identify common poker hands such as flush, full house,
    pairs, trips, quads, and straights based on the cards held.
    """

    def __init__(self, deck):
        """
        Initialize a PokerHand by dealing 5 cards from the provided deck.

        :param deck: Deck - a Deck object to draw cards from
        :return: None
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())  # Deal 5 cards from the deck
        self._cards = cards

    @property
    def cards(self):
        """
        Get the list of 5 cards currently in the poker hand.

        :param: None
        :return: list of Card - the 5 Card objects comprising the hand
        """
        return self._cards

    def __str__(self):
        """
        Provide a string representation of the poker hand's cards.

        :param: None
        :return: str - string representation of the list of Card objects in the hand
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Determine if the hand is a flush (all cards share the same suit).

        :param: None
        :return: bool - True if all cards have the same suit, False otherwise
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        Determine if the hand is a full house (three cards of one rank and two of another).

        The classification relies on the total count of matching pairs in the hand.

        :param: None
        :return: bool - True if the hand is a full house, False otherwise
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        Calculate the total number of matching rank pairs in the hand.

        Each matching pair increments the count; this helps in classifying pairs, trips, quads, etc.

        :param: None
        :return: int - the total count of matching rank pairs in the hand
        """
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Determine if the hand contains exactly one pair.

        :param: None
        :return: bool - True if exactly one pair exists, False otherwise
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        Determine if the hand contains exactly two pairs.

        :param: None
        :return: bool - True if exactly two pairs exist, False otherwise
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        Determine if the hand contains three cards of the same rank (three-of-a-kind).

        :param: None
        :return: bool - True if three cards share the same rank, False otherwise
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        Determine if the hand contains four cards of the same rank (four-of-a-kind).

        :param: None
        :return: bool - True if four cards share the same rank, False otherwise
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        Determine if the hand contains five cards with consecutive ranks.

        The hand is sorted by rank, then checks the difference between the highest
        and lowest rank indices, ensuring no duplicate ranks (number_matches == 0).

        :param: None
        :return: bool - True if the hand is a straight, False otherwise
        """
        self.cards.sort()  # Uses __gt__ from Card to sort by rank
        distance = Card.RANKS.index(self.cards[4].rank) - Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4

# Estimate the probability of being dealt a straight in 5 cards
count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
        # print(hand)
    count += 1

print(f"probability of a straight is {100 * matches / count}%")