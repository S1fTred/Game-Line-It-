
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.line = []
        self.score_stack = []
        self.tokens = []

    def take_card_from_market(self, market, card_index):
        if len(self.hand) < 2:  # Проверка, что у игрока есть место в руке
            if 0 <= card_index < len(market.cards):
                card = market.cards.pop(card_index)  # Убираем карту с рынка
                self.hand.append(card)  # Добавляем карту в руку игрока
                return True  # Взятие карты прошло успешно
            else:
                print("Недопустимый индекс карты на рынке.")
        else:
            print("У вас нет места в руке для еще одной карты.")
        return False  # Взятие карты не удалось

    def play_card_from_hand(self, hand_index):
        if 0 <= hand_index < len(self.hand):
            card = self.hand.pop(hand_index)
            self.line.append(card)
            return True
        else:
            print("У вас нет такой карты в руке.")
        return False

    def complete_line(self):
        if self.line:
            if self.tokens:
                token = self.tokens[0]
                num_cards = sum(1 for card in self.line if card.card_type == 'number')

                if num_cards == token.number - 3:
                    if token.number > 0:
                        self.tokens.remove(token)
                        self.score_stack.extend(self.line)
                        self.line = []
                        print(f"{self.name} выполнил условия для получения бонусного жетона +{token.number}")
                    else:
                        self.tokens.remove(token)
                        self.score_stack.extend(self.line)
                        self.line = []
                        print(f"{self.name} выполнил условия для получения бонусного жетона -{-token.number}")
                else:
                    self.tokens.remove(token)
                    self.score_stack.extend(self.line)
                    self.line = []
                    print(f"{self.name} не выполнил условия для получения жетона")
            else:
                self.score_stack.extend(self.line)
                self.line = []
                print(f"{self.name} завершил линию без ставки")
        else:
            print(f"{self.name} не имеет карт в линии для завершения")