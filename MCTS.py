import random
from copy import deepcopy
import math
from WinnerDecide import Winner
class MCTSNode:
    def __init__(self,parent=None,action=None,remaining_cards=None,player=None,comm_card=None,tot_players=None):
        self.parent=parent
        self.action=action
        self.children=[]
        self.remaining_cards=remaining_cards
        self.player=player
        self.comm_card=comm_card
        self.tot_players=tot_players
    
    def cards_distributed(self):
        tot_comm_cards=5
        if len(self.player)==self.tot_players and len(self.comm_card)==tot_comm_cards:
            return True
        else:
            return False
        
    def expand(self):

        if len(self.player)<self.tot_players:
             new_remaining_cards=deepcopy(self.remaining_cards)
             rand1=random.choice(new_remaining_cards)
             new_remaining_cards.remove(rand1)
             rand2=random.choice(new_remaining_cards)
             new_remaining_cards.remove(rand2)
             new_player=[rand1,rand2]
             new_player_list=deepcopy(self.player)
             new_player_list.append(new_player)
             child=MCTSNode(parent=self,action=(rand1,rand2),remaining_cards=new_remaining_cards,player=new_player_list,comm_card=deepcopy(self.comm_card),tot_players=self.tot_players)
             self.children.append(child)
             return child
        else:
            new_remaining_cards=deepcopy(self.remaining_cards)
            rand_comm_card=random.choice(new_remaining_cards)
            new_remaining_cards.remove(rand_comm_card)
            new_comm_card=deepcopy(self.comm_card)
            new_comm_card.append(rand_comm_card)
            child=MCTSNode(parent=self,action=rand_comm_card,remaining_cards=new_remaining_cards,player=deepcopy(self.player),comm_card=new_comm_card,tot_players=self.tot_players)
            self.children.append(child)
            return child
        
    def rollout(self):
        node = MCTSNode(
            remaining_cards=deepcopy(self.remaining_cards),
            player=deepcopy(self.player),
            comm_card=deepcopy(self.comm_card),
            tot_players=self.tot_players
        )

        while not node.cards_distributed():
            node=node.expand()

        result = Winner(node.player,node.comm_card).prob_search()

        return result
    
    def mcts_search(self,remaining_cards,player,comm_card,tot_players,iterations=100000):
           wins = 0

           for _ in range(iterations):

                node = MCTSNode(
                    remaining_cards=deepcopy(remaining_cards),
                    player=deepcopy(player),
                    comm_card=deepcopy(comm_card),
                    tot_players=tot_players
                )

                result = node.rollout()

                wins += result

           return wins / iterations



    
   


    
        
    