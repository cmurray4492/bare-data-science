"""This is the Python Adventure Game with Trevor Sawler on Udemy"""
import game


def main():
    # print a welcome screen
    game.welcome()

    # play the game until game over or player quits
    while True:
        game.play_game()




if __name__ == '__main__':
    main()
