class Winner:

    def __init__(self,player_cards,comm_cards):
        self.player_cards=player_cards
        self.comm_cards=comm_cards

    def check_roy_flush(self): 
        wins=0
        flag=False
        for i in range(len(self.player_cards)):
            tot_cards=[]
            tot_cards.extend(self.player_cards[i])
            tot_cards.extend(self.comm_cards)
            for j in range (4):
                king=13*10+j
                queen=12*10+j
                jack=11*10+j
                ten=10*10+j
                ace=1*10+j
                if king in tot_cards and queen in tot_cards and jack in tot_cards and ten in tot_cards and ace in tot_cards:
                    wins+=1
                    if(i==0):
                        flag=True
        if (wins>=1):
            if flag:
                return (True,1/wins)
            else:
                return (True,0)
        else:
            return (False,0)
                    
    def check_four_of_kind(self):
        flag=False
        present=False
        for i in range(len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            if self.Has_4_Kind(all_cards) and i==0:
                flag=True
                present=True
            elif self.Has_4_Kind(all_cards) and flag!=True:
                return (True,0)
            elif self.Has_4_Kind(all_cards):
                present=True
        if present!=True:
            return (False,0)
        
        all_cards1=[]
        all_cards1.extend(self.player_cards[0])
        all_cards1.extend(self.comm_cards)
        wins=0
        strength1=self.get_4_kind_strength(all_cards1)
        for i in range(1,len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            if self.Has_4_Kind(all_cards):
                strength_curr=self.get_4_kind_strength(all_cards)
                if (strength_curr > strength1):
                    return (True,0)
                elif (strength_curr==strength1):
                    wins+=1
        if (wins>=1):
            return (True,1/(wins+1))
        else:
            return (True,1)
               
    def Has_4_Kind(self,all_cards):
        cards={}
        for i in range(len(all_cards)):
            card=all_cards[i]//10
            cards[card]=cards.get(card,0)+1
        for i in cards:
            if(cards[i]==4):
                return True
        return False
    def get_4_kind_strength(self, all_cards):
        freq = {}

        for card in all_cards:
            rank = card // 10
            freq[rank] = freq.get(rank, 0) + 1

        quad_rank = -1
        for rank, cnt in freq.items():
            if cnt == 4:
                quad_rank = rank
                break
        kicker = -1
        for rank in freq:
            if rank != quad_rank:
                kicker = max(kicker, rank)

        return [quad_rank, kicker]
    
    def check_full_house(self):
        strength1=None
        for i in range(len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            strength=self.Has_full_House(all_cards)
            if (strength[0]!=-1 and strength[1]!=-1):
                if(i==0):
                   strength1=self.Has_full_House(all_cards)
                else:
                    if strength1 is None:
                        return (True,0)
                    elif (strength>strength1):
                        return (True,0)
        wins=1
        for i in range(1,len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            strength=self.Has_full_House(all_cards)
            if(strength==strength1):
                wins+=1
        if strength1 is None:
            return (False,0)
        else:
            return (True,1/wins)
       
    def Has_full_House(self, all_cards):
        freq = {}

        for card in all_cards:
            rank = card // 10
            freq[rank] = freq.get(rank, 0) + 1

        trips = []
        pairs = []

        for rank, cnt in freq.items():
            if cnt >= 3:
                trips.append(rank)
            elif cnt >= 2:
                pairs.append(rank)

        trips.sort(reverse=True)
        pairs.sort(reverse=True)

        if len(trips) >= 2:
            return [trips[0], trips[1]]

        if len(trips) == 1 and len(pairs) >= 1:
            return [trips[0], pairs[0]]

        return [-1, -1]
    def check_flush(self):
        strength1=None
        for i in range(len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            strength=self.Has_Flush(all_cards)
            if (strength!=None):
                if (i==0):
                    strength1=strength
                else:
                    if(strength1 is None):
                        return (True,0)
                    elif (strength> strength1):
                        return (True,0)
        if strength1 is None:
            return (False,0)
        else:
            wins=1
            for i in range(1,len(self.player_cards)):
                 all_cards=[]
                 all_cards.extend(self.player_cards[i])
                 all_cards.extend(self.comm_cards)
                 strength=self.Has_Flush(all_cards)
                 if( strength==strength1):
                     wins+=1
            return (True,1/wins)
       
    def Has_Flush(self,all_cards):

        suits_freq = {}

        for i in range(len(all_cards)):

            suit = all_cards[i] % 10

            suits_freq[suit] = suits_freq.get(suit,0) + 1

        best_suit = -1

        for i in suits_freq:

            if suits_freq[i] >= 5:
                best_suit = i

        if best_suit == -1:
            return None

        else:

            cards = []

            for i in range(len(all_cards)):

                card = all_cards[i] // 10

                if card == 1:
                    card = 14

                suit = all_cards[i] % 10

                if suit == best_suit:
                    cards.append(card)

            cards.sort(reverse=True)

            return cards[:5]
    def check_high_card(self):

        cards1 = []

        cards1.extend(self.player_cards[0])
        cards1.extend(self.comm_cards)

        strength1 = self.high_card_strength(cards1)

        ties = 0

        for i in range(1, len(self.player_cards)):

            cards = []

            cards.extend(self.player_cards[i])
            cards.extend(self.comm_cards)

            strength = self.high_card_strength(cards)

            if strength > strength1:
                return 0

            elif strength == strength1:
                ties += 1

        return 1/(ties+1)

    def high_card_strength(self, all_cards):

        ranks = []

        for card in all_cards:

            rank = card // 10

            if rank == 1:
                rank = 14

            ranks.append(rank)

        ranks = sorted(ranks, reverse=True)

        return ranks[:5]
    def check_one_pair(self):
        strength1 = None

        for i in range(len(self.player_cards)):
            all_cards = []
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)

            strength = self.one_pair_strength(all_cards)

            if strength[0] != -1:
                if i == 0:
                    strength1 = strength
                else:
                    if strength1 is None:
                        return (True, 0)
                    elif strength > strength1:
                        return (True, 0)

        if strength1 is None:
            return (False, 0)
        wins=1
        for i in range(1, len(self.player_cards)):
            all_cards = []
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)

            strength = self.one_pair_strength(all_cards)

            if strength[0] != -1:
                if strength == strength1:
                    wins+=1

        return (True, 1/wins)

    def one_pair_strength(self, all_cards):
        freq = {}

        for c in all_cards:
            rank = c // 10

            if rank == 1:
                rank = 14

            freq[rank] = freq.get(rank, 0) + 1

        pair = -1
        kickers = []

        for rank in sorted(freq.keys(), reverse=True):
            if freq[rank] == 2 and pair == -1:
                pair = rank
            else:
                kickers.append(rank)

        return (pair, kickers[:3])
    def two_pair_strength(self,all_cards):

        freq={}

        for c in all_cards:
            rank=c//10
            if rank==1:
                rank=14
            freq[rank]=freq.get(rank,0)+1
        
        high_pair=-1
        low_pair=-1
        kickers=[]

        for rank in sorted(freq.keys(),reverse=True):
            if freq[rank]==2:
                if high_pair==-1:
                    high_pair=rank
                elif low_pair==-1:
                    temp=high_pair
                    high_pair=max(temp,rank)
                    low_pair=min(temp,rank)
            else:
                    kickers.append(rank)
        kickers.sort(reverse=True)  
        return (high_pair,low_pair,kickers[:1])
    def check_two_pair(self):
       strength1=None
       for i in range(len(self.player_cards)):
           all_cards=[]
           all_cards.extend(self.player_cards[i])
           all_cards.extend(self.comm_cards)
           strength=self.two_pair_strength(all_cards)
           if(strength[0]!=-1 and strength[1]!=-1):
               if(i==0):
                   strength1=strength
               else:
                   if strength1 is None:
                       return (True,0)
                   elif (strength1<strength):
                       return (True,0)
       if strength1 is None:
           return (False,0)
       else:
           wins=1
           for i in range(1,len(self.player_cards)):
               all_cards=[]
               all_cards.extend(self.player_cards[i])
               all_cards.extend(self.comm_cards)
               strength=self.two_pair_strength(all_cards)
               if(strength==strength1):
                   wins+=1
           return (True,1/wins)        
    def three_kind_strength(self, all_cards):
        freq = {}

        for c in all_cards:
            rank = c // 10
            if rank == 1:
                rank = 14
            freq[rank] = freq.get(rank, 0) + 1

        three_kind = -1

        for rank in sorted(freq.keys(), reverse=True):
            if freq[rank] >= 3:
                three_kind = rank
                break

        if three_kind == -1:
            return (-1, [])

        kickers = []

        for rank in sorted(freq.keys(), reverse=True):
            if rank != three_kind:
                kickers.append(rank)

        return (three_kind, kickers[:2])
    def check_three_kind(self):
        strength1=None
        for i in range(len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            strength=self.three_kind_strength(all_cards)
            if(strength[0]!=-1):
                if(i==0):
                    strength1=strength
                else:
                    if strength1 is None:
                        return (True,0)
                    elif (strength>strength1):
                        return (True,0)
        if strength1 is None:
            return (False,0)
        else:
            wins=1
            for i in range(1,len(self.player_cards)):
                all_cards=[]
                all_cards.extend(self.player_cards[i])
                all_cards.extend(self.comm_cards)
                strength=self.three_kind_strength(all_cards)
                if (strength==strength1):
                    wins+=1
            return (True,1/wins)

    def strait_strength(self, all_cards):
        cards = []

        for c in all_cards:
            rank = c // 10

            if rank == 1:
                rank = 14

            cards.append(rank)

        cards = sorted(list(set(cards)))

        if 14 in cards:
            cards.insert(0, 1)

        cnt = 1
        best = -1

        for i in range(1, len(cards)):
            if cards[i] == cards[i - 1] + 1:
                cnt += 1

                if cnt >= 5:
                    best = max(best, cards[i])

            else:
                cnt = 1

        if best != -1:
            return (True, best)

        return (False, -1)
    def check_strait(self):
       strength1=None
       for i in range(len(self.player_cards)):
           all_cards=[]
           all_cards.extend(self.player_cards[i])
           all_cards.extend(self.comm_cards)
           strength=self.strait_strength(all_cards)
           if strength[0]==True:
               if i==0:
                   strength1=strength[1]
               else:
                   if strength1 is None:
                       return (True,0)
                   elif strength[1]>strength1:
                       return (True,0)
       if strength1 is None:
           return (False,0)
       else:
           wins=1
           for i in range(1,len(self.player_cards)):
               all_cards=[]
               all_cards.extend(self.player_cards[i])
               all_cards.extend(self.comm_cards)
               strength=self.strait_strength(all_cards)
               if(strength[0]==True):
                   if(strength[1]==strength1):
                       wins+=1
           return (True,1/wins)
               
    def straight_flush_strength(self, all_cards):
        suit_groups = {}

        for card in all_cards:
            suit = card % 10
            rank = card // 10

            if rank == 1:
                rank = 14

            if suit not in suit_groups:
                suit_groups[suit] = []

            suit_groups[suit].append(rank)

        best = -1

        for suit in suit_groups:
            cards = sorted(list(set(suit_groups[suit])))

            if 14 in cards:
                cards.insert(0, 1)

            cnt = 1

            for i in range(1, len(cards)):
                if cards[i] == cards[i - 1] + 1:
                    cnt += 1

                    if cnt >= 5:
                        best = max(best, cards[i])

                else:
                    cnt = 1

        if best != -1:
            return (True, best)

        return (False, -1)
    def check_strait_flush(self):
       strength1=None
       for i in range(0,len(self.player_cards)):
           all_cards=[]
           all_cards.extend(self.player_cards[i])
           all_cards.extend(self.comm_cards)
           strength=self.straight_flush_strength(all_cards)
           if strength[0]:
               if i==0:
                   strength1=strength[1]
               else:
                   if strength1 is None:
                       return (True,0)
                   elif (strength[1]>strength1):
                       return (True,0)
       if strength1 is None:
           return (False,0)
       else:
           wins=1
           for i in range(1,len(self.player_cards)):
            all_cards=[]
            all_cards.extend(self.player_cards[i])
            all_cards.extend(self.comm_cards)
            strength=self.straight_flush_strength(all_cards)
            if strength[0]:
                if(strength[1]==strength1):
                    wins+=1
           return (True,1/wins)
    def prob_search(self):
        result_roy_flush=self.check_roy_flush()
        if result_roy_flush[0]:
            return result_roy_flush[1]
        result_strait_flush=self.check_strait_flush()

        if result_strait_flush[0]:
            return result_strait_flush[1]
        result_four_kind=self.check_four_of_kind()

        if result_four_kind[0]:
            return result_four_kind[1]
        result_full_house=self.check_full_house()

        if result_full_house[0]:
            return result_full_house[1]
        result_check_flush=self.check_flush()

        if result_check_flush[0]:
            return result_check_flush[1]
        result_strait=self.check_strait()

        if result_strait[0]:
            return result_strait[1]
        result_three_kind=self.check_three_kind()

        if result_three_kind[0]:
            return result_three_kind[1]
        result_two_pair=self.check_two_pair()

        if result_two_pair[0]:
            return result_two_pair[1]
        result_one_pair=self.check_one_pair()

        if result_one_pair[0]:
            return result_one_pair[1]
        else:
            return self.check_high_card()
           

    
        

           
        
    


   