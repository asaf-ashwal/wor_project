import random
def create_card(rank:str,suite:str):
    """gets: rank:str,suite:str
    return: 
    {"rank": "10", "suite": "H", "value":10}
    """
    # H, C, D, S.
    card = {'rank':rank, 'suite':suite, 'value':1}
    return card
    
# print(create_card('A','S'))
    
    
    
    


def compare_cards(p1_card:dict, p2_card:dict):
    """gets 2 players dicts
    and return palyer name as str
    """
    if p1_card['value'] > p2_card['value']:
        return 'p1'
    else: return 'p2'
# print(compare_cards({"rank": "10", "suite": "H", "value":13}, {"rank": "10", "suite": "H", "value":12})) 

def card_rank(num):
    if num == 11:
        return 'J'
    if num == 12:
        return 'Q'
    if num == 13:
        return 'K'
    else: return num
    
    
def shuffle(deck:list[dict]):
    new_deck = deck 
    flag = 1000
    while flag >= 0:
        random1 = random.randrange(0,52)    
        random2 = random.randrange(0,52)
        temp = new_deck[random1]
        if random1 == random2:
            continue
        new_deck[random1] = new_deck[random2]
        new_deck[random2] = temp
        flag -=1
    return new_deck
# print(,shuffle(create_deck())) 


def create_deck():
    """Returns shuffled cards
    {'rank': 'K', 'su+1te': 'S', 'value': 13}
    """
    cards_deck = []
    card_suite = ['H','C','D','S']
    
    for i in range(13):
        for j in range(4):
           cards_deck.append({"rank":card_rank(i+1) , 'suite': card_suite[j], "value":i+1})
    return shuffle(cards_deck)
# print(create_deck())


    



