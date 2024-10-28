from game.game import *
from game.constants import *

def main():
    game = Game(GAME_NAME, (SCREEN_WIDTH, SCREEN_HEIGHT))
    game.run()

if __name__ == "__main__":
    main()