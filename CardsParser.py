class CardsParser:
    def __init__(self,player_cards,community_cards):
        self.player_cards=player_cards
        self.community_cards=community_cards
    def Playing_Cards_Parse(self):
        players=[]
        groups=self.player_cards.split(",")
        for card in groups:
            card1=self.convert_card(card[:2])
            card2=self.convert_card(card[2:])
            players.append([card1,card2])
        return players
    def Community_Cards_Parse(self):
        comm_cards=[]
        if self.community_cards == "":
            return comm_cards
        groups=self.community_cards.split(",")
        for card in groups:
            curr_card=self.convert_card(card)
            comm_cards.append(curr_card)
        return comm_cards
    def convert_card(self,card):
        RANK_MAP = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 1
       }

        SUIT_MAP = {
            "c": 0,
            "d": 1,
            "h": 2,
            "s": 3
        }
        rank=RANK_MAP[card[0]]
        suit=SUIT_MAP[card[1]]
        val=rank*10+suit
        return val
