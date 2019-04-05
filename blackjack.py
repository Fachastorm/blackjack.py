import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " +self.suit

class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits: 
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has:"+deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0 
        self.aces = 0 
    
    def add_card(self, card):
        #card passed in 
        #from Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank] #dictionary lookup of values

        #track aces 
        if card.rank == 'Ace':
            self.aces += 1
         
    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self, total=100):
        self.total = total #Has a default and can be set by user
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet