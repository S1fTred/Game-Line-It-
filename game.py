from deck import Deck
from player import Player
from card import Card


class Game:
    def __init__(self, players, deck):
        self.players = players
        self.market = Deck()
        self.current_player = 0
        self.round = 1
        self.deck = deck

    def start_round(self):
        cards_for_market = self.deck.draw_cards(2)
        for player in self.players:
            player.hand.extend(self.deck.draw_cards(2))
        self.market.update_deck(cards_for_market)

        self.current_player = 0

        print(f"Начало раунда {self.round}")
        print(f"Рынок: {[str(card) for card in self.market.cards]}")
        print(f"Ход игрока {self.players[self.current_player].name}")

    def end_round(self):
        for player in self.players:
            player.score_stack.extend(player.line)
            player.line = []

        remaining_cards = self.deck.draw_cards(len(self.market.cards))
        self.market.update_deck(remaining_cards)

        for player in self.players:
            player_score = sum(card.number for card in player.score_stack)
            for card in player.score_stack:
                if card.card_type == 'number':
                    player_score += 1

            jackpot_tokens = {}
            for card in player.score_stack:
                if card.card_type == 'number':
                    if card.color not in jackpot_tokens:
                        jackpot_tokens[card.color] = [card]
                    else:
                        jackpot_tokens[card.color].append(card)
                    if len(jackpot_tokens[card.color]) == 3:
                        player_score += sum(card.number for card in jackpot_tokens[card.color])
                        jackpot_tokens[card.color] = []

            player.tokens.append(jackpot_tokens)
            player.score_stack = []
            print(f"{player.name}: {player_score} очков")

        self.round += 1
        self.current_player = 0

    def next_turn(self):
        # Переход к следующему игроку по кругу
        self.current_player = (self.current_player + 1) % len(self.players)

    def play_game(self):
        for round_num in range(1, 4):
            self.start_round()

            while True:
                current_player = self.players[self.current_player]
                print(f"\nХод игрока {current_player.name}")
                print(f"Рука игрока: {[str(card) for card in current_player.hand]}")

                market_index = int(input("Выберите индекс карты для взятия с рынка: "))
                current_player.take_card_from_market(self.market, market_index)

                hand_index = int(input("Выберите индекс карты для разыгрывания: "))
                current_player.play_card_from_hand(hand_index)

                complete_line_choice = input("Хотите завершить линию? (y/n): ")
                if complete_line_choice.lower() == 'y':
                    current_player.complete_line()

                self.next_turn()

                if len(self.deck.cards) == 0:
                    break

            self.end_round()

        print("\nИгра завершена.")
        for player in self.players:
            print(f"{player.name}: {sum(card.number for card in player.score_stack)} очков")


