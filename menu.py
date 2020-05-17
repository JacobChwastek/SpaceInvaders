import pygame
from colors import Color
from button import button


class Menu(pygame.sprite.Sprite):

    def __init__(self, game_state, win=None):
        super(Menu, self).__init__()
        self.win = win
        self.game_state = game_state

    def display(self):
        button("START", 200, 100, 200, 50, Color.Gainsboro(), Color.Green(), self.win, self.start_game)
        button("SCORE", 200, 200, 200, 50, Color.Gainsboro(), Color.Green(), self.win, self.score_board)
        button("EXIT", 200, 300, 200, 50, Color.Gainsboro(), Color.Red(), self.win, self.exit)

    def start_game(self):
        self.game_state = "game"

    def exit(self):
        self.game_state = "exit"

    def score_board(self):
        # self.game_state = "score"
        pass