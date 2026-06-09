class CardsGen:

    def __init__(self,cards):
        self.cards=cards

    def generate(self):

        tot_cards=[]

        for i in range(4):
            for j in range(1,14):
                curr_card=j*10+i
                tot_cards.append(curr_card)

        for i in self.cards:
            tot_cards.remove(i)

        return tot_cards
    
# We convert the cards to integers
# A value of 0-3 (inclusive) represents the suits of poker
# A value of 1-13 (inclusive) represents the cards of a suit