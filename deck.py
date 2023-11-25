import random


class Deck:
    def __init__(self):
        self.cards = []

    def update_deck(self, new_cards):
        self.cards = new_cards

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_cards(self, num_cards):
        # Проверка, что в колоде достаточно карт для вытягивания
        if len(self.cards) >= num_cards:
            # Вытягивание указанного количества карт из колоды
            drawn_cards = self.cards[:num_cards]
            # Удаление вытянутых карт из колоды
            self.cards = self.cards[num_cards:]
            return drawn_cards
        else:
            print("В колоде недостаточно карт.")
            return []