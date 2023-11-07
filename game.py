import market

class Game:
    def __init__(self, players, deck):
        self.players = players
        self.market = market.Market()
        self.current_player = 0
        self.round = 1
        self.deck = deck

    def start_round(self):
        # 1. Извлекаем 2 карты для каждого игрока и 2 дополнительные для рынка.
        cards_for_market = self.deck.draw_cards(2)
        for player in self.players:
            player.hand.extend(self.deck.draw_cards(2))
        self.market.update_market(cards_for_market)

        # 2. Назначаем первого игрока для начала раунда.
        self.current_player = 0

        print(f"Начало раунда {self.round}")
        print(f"Рынок: {[str(card) for card in self.market.cards]}")
        print(f"Ход игрока {self.players[self.current_player].name}")

    def end_round(self):
        # Сброс карт из линий всех игроков в стопки очков
        for player in self.players:
            player.score_stack.extend(player.line)
            player.line = []

        # Обновление рынка, добавляем оставшиеся карты из колоды
        remaining_cards = self.deck.draw_cards(len(self.market.cards))
        self.market.update_market(remaining_cards)

        # Подсчет очков и обработка жетонов джекпота
        for player in self.players:
            player_score = sum(card.number for card in player.score_stack)
            for card in player.score_stack:
                if card.card_type == 'number':
                    player_score += 1  # Дополнительное очко за каждую числовую карту
            # Подсчет жетонов джекпота
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

            # Добавление полученных очков
            player.tokens.append(jackpot_tokens)  # Возвращение неполученных жетонов
            player.score_stack = []
            print(f"{player.name}: {player_score} очков")

        # Переход к следующему раунду
        self.round += 1
        self.current_player = 0

    def next_turn(self):
        # Переход к следующему игроку по кругу
        self.current_player = (self.current_player + 1) % len(self.players)
