from CardsGenerator import CardsGen
from CardsParser import CardsParser
from MCTS import MCTSNode
class ProbabilityController:
    def __init__(self,player_cards,comm_cards,total_players):
        self.player_cards=player_cards
        self.comm_cards=comm_cards
        self.total_players=total_players
    def calculate_probability(self):
        parseCards=CardsParser(player_cards=self.player_cards,community_cards=self.comm_cards)
        players=parseCards.Playing_Cards_Parse()
        comm_cards=parseCards.Community_Cards_Parse()
        tot_cards=[]
        for card in players:
            tot_cards.extend(card)
        tot_cards.extend(comm_cards)
        CardsGene=CardsGen(cards=tot_cards)
        remaining_cards=CardsGene.generate()
        result=MCTSNode().mcts_search(remaining_cards=remaining_cards,player=players,comm_card=comm_cards,tot_players=self.total_players)
        return result
    
