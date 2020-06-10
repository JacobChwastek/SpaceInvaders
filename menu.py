import pygame
from colors import Color
from button import button


class Menu(pygame.sprite.Sprite):
    game_state = "menu"

    def __init__(self, win=None):
        super(Menu, self).__init__()
        self.win = win

    def display(self):
        button("START", 200, 100, 200, 50, Color.GAINSBORO, Color.GREEN, self.win, self.start_game)
        button("SCORE", 200, 200, 200, 50, Color.GAINSBORO, Color.GREEN, self.win, self.score_board)
        button("EXIT", 200, 300, 200, 50, Color.GAINSBORO, Color.RED, self.win, self.exit)

    def start_game(self):
        self.game_state = "game"

    def menu(self):
        self.game_state = "menu"

    def exit(self):
        self.game_state = "exit"

    def score_board(self):
        # self.game_state = "score"
        pass
