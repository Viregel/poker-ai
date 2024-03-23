from random import shuffle


class Card():

    suite = ""
    value = ""

    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.name = self.cardType()
        pass

    def cardType(self):
        return str(self.value) + "_" + self.suite

    def __str__(self):
        return str(self.value) + "_" + self.suite


class CardDeck():

    card_suits = ["hearts", "diamonds", "spades", "clubs"]
    card_values = [i for i in range(1, 14)]

    cards = []

    def __init__(self):

        for suite in self.card_suits:
            for value in self.card_values:
                newCard = Card(suite, value)
                self.cards.append(newCard)

        self.cards_in_pack = self.cards[:]
        self.cards_dealt = []
        self.community_cards = []

        self.shuffleDeck()

        pass

    def shuffleDeck(self):
        return shuffle(self.cards_in_pack)

    def dealToPlayer(self, player, n=2):
        toDeal = self.cards_in_pack[0:n]
        player.setCards(toDeal)
        for c in toDeal:
            self.deal(c)
        pass

    def dealToCommunity(self, n=1):
        toDeal = self.cards_in_pack[0:n]
        for c in toDeal:
            self.addCommunityCard(c)
        pass

    def deal(self, card):
        self.cards_dealt.append(card)
        self.cards_in_pack.remove(card)
        pass

    def addCommunityCard(self, card):
        self.community_cards.append(card)
        self.cards_in_pack.remove(card)
        pass

    def cardsDealt(self):
        return self.cards_dealt

    def cardsInPack(self):
        return self.cards_in_pack

    def getCards(self):
        return self.cards

    def getCommunityCards(self):
        return self.community_cards

    def resetCommunityCards(self):
        for c in self.community_cards:
            self.cards_in_pack.append(c)
        self.community_cards = []
