def getHandRanking(hand):
    for rankedHand in hand_ranking_functions:
        if rankedHand(hand):
            i = hand_ranking_functions.index(rankedHand)
            return hand_ranking_classes[i]


def getPlayerHand(player, deck):

    player_cards = player.getCards()
    community_cards = deck.getCommunityCards()

    return player_cards + community_cards


def getPlayerHandRanking(player, deck):
    player_hand = getPlayerHand(player, deck)
    return getHandRanking(player_hand)


class PokerHand():

    handRanking = "Nothing"
    hand = []

    def __init__(self, hand):
        self.hand = hand
        pass


class RoyalFlush():

    def __init__(self):
        pass

    def __name__(self):
        return "Royal Flush"


class StraightFlush():

    def __init__(self):
        pass

    def __name__(self):
        return "Straight Flush"


class FourOfAKind():

    def __init__(self):
        pass

    def __name__(self):
        return "Four of a Kind"


class FullHouse():

    def __init__(self):
        pass

    def __name__(self):
        return "Full House"


class Flush():

    def __init__(self):
        pass

    def __name__(self):
        return "Flush"


class Straight():

    def __init__(self):
        pass

    def __name__(self):
        return "Straight"


class ThreeOfAKind():

    def __init__(self):
        pass

    def __name__(self):
        return "Three of a Kind"


class TwoPair():

    def __init__(self):
        pass

    def __name__(self):
        return "Two Pair"


class Pair():

    def __init__(self):
        pass

    def __name__(self):
        return "Pair"


class HighCard():

    def __init__(self):
        pass

    def __name__(self):
        return "High Card"


class HandRanking():

    def __init__(self, hand):
        pass


def getSuites(hand):
    suites = []
    for card in hand:
        if card.suite not in suites:
            suites.append(card.suite)
    return suites


def isRoyalFlush(hand):

    if len(getSuites(hand)) > 1:
        return False

    royal_flush_values = [1, 10, 11, 12, 13]
    card_values = []

    for card in hand:
        card_values.append(card.value)
    card_values.sort()

    for r in royal_flush_values:
        if r not in card_values:
            return False
    return True


def isStraightFlush(hand):
    if isStraight(hand) and isFlush(hand):
        return True
    return False


def isFourOfAKind(hand):

    unique_values = []
    for card in hand:
        if card.value not in unique_values:
            unique_values.append(card.value)

    for v in unique_values:
        count = 0
        for card in hand:
            if v == card.value:
                count += 1
            if count == 4:
                return True

    return False


def isFullHouse(hand):

    our_hand = hand[:]

    unique_values = []
    for card in our_hand:
        if card.value not in unique_values:
            unique_values.append(card.value)

    our_value = 0
    for v in unique_values:
        count = 0
        for card in our_hand:
            if v == card.value:
                count += 1
            if count == 3:
                our_value = v
                pass

    if our_value != 0:
        for card in our_hand:
            if card.value == our_value:
                our_hand.remove(card)

        if isPair(our_hand):
            return True

    return False


def isFlush(hand):

    card_suites = ["hearts", "diamonds", "spades", "clubs"]
    suiteCount = [0, 0, 0, 0]

    def changeSuiteCount(suite):
        i = card_suites.index(suite)
        suiteCount[i] += 1

    for card in hand:
        changeSuiteCount(card.suite)

    for s in suiteCount:
        if s >= 5:
            return True
    return False


def isStraight(hand):

    sorted_hand = []

    for card in hand:
        sorted_hand.append(card.value)

    sorted_hand.sort()

    def removeDuplicates(ourList):
        newList = []
        for i in range(len(ourList)):
            if ourList[i] not in newList:
                newList.append(ourList[i])
        return newList

# TODO: Deal with duplicates
    sorted_hand = removeDuplicates(sorted_hand)

    def isConsecutive(ourList):
        for i in range(len(ourList)):
            if ourList[i] != ourList[i-1] + 1:
                return False
        return True

    for c in range(len(sorted_hand)-5):
        if isConsecutive(sorted_hand[c:c+5]):
            return True

    return False


def isThreeOfAKind(hand):

    unique_values = []
    for card in hand:
        if card.value not in unique_values:
            unique_values.append(card.value)

    for v in unique_values:
        count = 0
        for card in hand:
            if v == card.value:
                count += 1
            if count == 3:
                return True

    return False


def isTwoPair(hand):

    unique_values = []
    count_pairs = 0
    for card in hand:
        if card.value not in unique_values:
            unique_values.append(card.value)
        else:
            count_pairs += 1

    if count_pairs == 2:
        return True

    return False


def isPair(hand):

    unique_values = []
    for card in hand:
        if card.value not in unique_values:
            unique_values.append(card.value)
        else:
            return True
    return False


def isHighCard(hand):
    return True


hand_ranking_functions = [isRoyalFlush,
                          isStraightFlush,
                          isFourOfAKind,
                          isFullHouse,
                          isFlush,
                          isStraight,
                          isThreeOfAKind,
                          isTwoPair,
                          isPair,
                          isHighCard]

hand_ranking_classes = [RoyalFlush,
                        StraightFlush,
                        FourOfAKind,
                        FullHouse,
                        Flush,
                        Straight,
                        ThreeOfAKind,
                        TwoPair,
                        Pair,
                        HighCard]
