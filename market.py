
class Market:
    def __init__(self):
        self.cards = []

    def update_market(self, new_cards):
        self.cards = new_cards

    def draw_cards(self, num_cards):
        # Проверка, что в рынке достаточно карт для вытягивания
        if len(self.cards) >= num_cards:
            # Вытягивание указанного количества карт из рынка
            drawn_cards = self.cards[:num_cards]
            # Удаление вытянутых карт из рынка
            self.cards = self.cards[num_cards:]
            return drawn_cards
        else:
            print("В рынке недостаточно карт.")
            return []