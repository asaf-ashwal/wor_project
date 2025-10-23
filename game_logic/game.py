from utils.deck import create_deck, compare_cards

def create_player(name = 'AI'):
    player_card = {'name': name, 'hand':[],'won_pile':[]}    
    return player_card
# print(create_player('asaf'))

def init_game():
    player_1 = 'asaf'
    player_1 =create_player(player_1)
    player_2 =create_player()
    deck = create_deck()
    player_1['hand'] = deck[0:26]
    player_2['hand'] = deck[26:]
    return {'the game dict': {
        # 'deck':deck,
        'player_1': player_1,
        'player_2': player_2
        }}


def play_round(game):
    
    player_1_card = game['player_1']['hand'].pop()
    player_2_card = game['player_2']['hand'].pop()
    winner = compare_cards(player_1_card,player_2_card)
    if winner == 'p1':
        # print('player won with: ', player_1_card)
        # print('AI lost with: ', player_2_card)
        game['player_1']['won_pile'].append(player_1_card)
        game['player_1']['won_pile'].append(player_2_card)
    elif winner == 'p2':
        # print('AI  won with: ', player_2_card)
        # print('player lost with: ', player_1_card)
        game['player_2']['won_pile'].append(player_1_card)
        game['player_2']['won_pile'].append(player_2_card)
    else:    game['player_1']['hand'].insert(0, player_1_card)
    game['player_2']['hand'].insert(0, player_2_card)
    # print('player : ',game['player_1']['won_pile'])
    # print('AI: ',game['player_2']['won_pile'])


def victory(game):
    flag = True
    for i in range(26):
        play_round(game)
    if len(game['player_1']['won_pile']) > len(game['player_2']['won_pile']):
        print('player won with',len(game['player_1']['won_pile']),'cards', 'player with: ',len(game['player_2']['won_pile']))
    else:         print('AI won with',len(game['player_2']['won_pile']),'cards','player with:',len(game['player_1']['won_pile']))

    

        