def getHandRanking(hand):
        for rankedHand in hand_ranking_functions:
            if rankedHand(hand):
                #Get equivalent class
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
   #TODO: This should be updated by HandRankings.getHandRanking
   
   hand = []

   

   def __init__(self, hand):
      self.hand = hand
      pass

    
   #TODO: Function that returns name of hand

   #TODO: Function that returns value of hand


#Calculate hand values

#Define each hand

#TODO: Lots of code repeated here. Look at how to make it more efficient.
#TODO: Replace functions with classes?

"""
Royal Flush: value_x_1, value_x_10, value_x_11, value_x_12, value_x_13
Straight Flush: suit_x, suit_x+1, suit_x+2, suit_x+3, suit_x+4
Four of a Kind: value_x, value_x, value_x, value_x
Full House: value_x, value_x, value_x, value_y, value_y
Flush: suit_x, suit_x, suit_x, suit_x, suit_x
Straight: x, x+1, x+2, x+3, x+4
Three of a Kind: value_x, value_x, value_x
Two Pair: value_x, value_x, value_y, value_y
Pair: value_x, value_x
High Card: At least one of 1, 10, 11, 12, 13
"""

"""
Want to create a method that acts on a hand
-> Hand should be a class
-> When hand is created, assign it to an object
-> Each player should have a hand object created 

Method should return:
-> Name of hand
-> Value of hand

In pseudocode, player.handRank() should return the hand ranking
-> Assume that hand is an instance variable of player - handRank() can access it
So handRank() must be a method of player
-> Ignore exact values for the time being - JUST want the ranking
handRank() returns a class (?)
-> Each hand ranking is a class
handRank() needs to check which class the hand belongs to
-> Each hand ranking class has a method to check whether or not a hand is a memebr
-> handRank() goes through each hand ranking class in order of value and invokes the appropiate method.
   If the player's hand fits the class method, then  handRank() invokes the hand ranking class's name method and returns this.
"""

#TODO: Make more rigerous
#Where a certain number of cards are required, ensure those cards ALL exist
   
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
    #TODO: Problem with how this executes.
    #Needs to be more specific in how it's executing.

    if len(getSuites(hand)) > 1:
        return False
    
    royal_flush_values = [1,10,11,12,13]
    card_values = []

    for card in hand:
        card_values.append(card.value)
    card_values.sort()

    #TODO: Do they need to be same suite?
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

    #Create virtual hand
    our_hand = hand[:]

    #Check we have three of a kind
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

    #If so, remove from virtual hand
    if our_value != 0:
        for card in our_hand:
            if card.value == our_value:
                our_hand.remove(card)

        if isPair(our_hand):
            return True

    return False

def isFlush(hand):

    card_suites = ["hearts", "diamonds", "spades", "clubs"]
    suiteCount = [0,0,0,0]

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
    #Sort numbers, check if consecutive

    sorted_hand = []

    for card in hand:
        sorted_hand.append(card.value)

    sorted_hand.sort()

    #TODO: Remove duplicates

    def removeDuplicates(ourList):
        newList = []
        for i in range(len(ourList)):
            if ourList[i] not in newList:
                newList.append(ourList[i])
        return newList
    
    #TODO: Add back in
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

    #for card in hand:
    #    if card.value in [1, 10, 11, 12, 13]:
    #        return True
    return True

    
#List them in order of precedence

#TODO: Can I make these global?

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

#TODO: Get exact values of cards
#TODO: Define tiebreak conditions - consider function output. Might be best to have a class that returns both the truth value and the specific card value/suite?