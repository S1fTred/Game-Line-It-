from deck import Deck
from player import Player
from game import Game

# Создаем колоду и игроков
deck = Deck()
player1 = Player("Игрок 1")
player2 = Player("Игрок 2")
players = [player1, player2]

# Создаем и запускаем игру
game = Game(players, deck)
game.play_game()