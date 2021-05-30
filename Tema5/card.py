import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display_card(self):
        return self.value + ' of ' + self.suit

    def get_card_suit(self):
        return self.suit

    def get_card_value(self):
        return self.value


class Deck:

    def __init__(self):
        # create deck
        value_list = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        suit_list = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
        cards_list = []
        for i in value_list:
            for j in suit_list:
                cards_list.append(Card(j, i))
        print(len(cards_list))
        self.cards_list = cards_list

    def deal_remove_card(self, suit, value):

        found = 0
        for i in range(len(self.cards_list)):
            if self.cards_list[i].get_card_suit() == suit:
                if self.cards_list[i].get_card_value() == value:
                    self.cards_list.remove(self.cards_list[i])
                    found = 1
                    break
        if found == 0:
            raise Exception("Card was not found")

    def print_elements(self):
        for i in range(len(self.cards_list)):
            print(self.cards_list[i].display_card())

    def shuffle_cards(self):
        random.shuffle(self.cards_list)
        if len(self.cards_list) != 52:
            raise Exception("Cards cannot be shuffled")


deck = Deck()
print(len(deck.cards_list))
deck.deal_remove_card('Diamonds', 'A')
print(len(deck.cards_list))
deck.shuffle_cards()
deck.print_elements()
