from deck import Deck, Card  # Import Deck and Card classes

class PokerHand:
    def __init__(self, deck):
        """
        :param deck: a Deck object to draw cards from
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())  # Deal 5 cards from the deck
        self._cards = cards

    @property
    def cards(self):
        """
        :return: list of 5 Card objects in the hand
        """
        return self._cards

    def __str__(self):
        """
        :return: string representation of the hand
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        :return: True if all cards have the same suit
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        """
        :return: True if the hand is a full house (3 of one rank, 2 of another)
        """
        return self.number_matches == 8

    @property
    def number_matches(self):
        """
        :return: total number of matching pairs (used internally to classify hands)
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
        :return: True if the hand contains exactly one pair
        """
        return self.number_matches == 2

    @property
    def is_two_pair(self):
        """
        :return: True if the hand contains exactly two pairs
        """
        return self.number_matches == 4

    @property
    def is_trips(self):
        """
        :return: True if the hand contains three cards of the same rank
        """
        return self.number_matches == 6

    @property
    def is_quads(self):
        """
        :return: True if the hand contains four cards of the same rank
        """
        return self.number_matches == 12

    @property
    def is_straight(self):
        """
        :return: True if the hand contains five consecutive ranks
        """
        self.cards.sort()  # Uses __gt__ from Card
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

print(f"probability of a straight is {100*matches/count}%")