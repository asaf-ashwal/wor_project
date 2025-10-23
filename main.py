from game_logic.game import init_game, victory

if __name__ == "__main__": 
    game = init_game()
    if 'the game dict' in game: 
        victory(game['the game dict'])