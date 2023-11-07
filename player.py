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

    def play_card_from_hand(self, card):
        if card in self.hand:
            self.hand.remove(card)  # Убираем карту из руки игрока
            self.line.append(card)  # Добавляем карту в линию игрока
            return True  # Разыгрывание карты прошло успешно
        else:
            print("У вас нет такой карты в руке.")
        return False  # Разыгрывание карты не удалось

    def complete_line(self):
        if self.line:  # Проверка, что у игрока есть карты в линии
            if self.tokens:  # Проверка, что у игрока есть жетоны ставок
                token = self.tokens[0]  # Предполагается, что игрок может иметь только один жетон ставки
                num_cards = 0
                for card in self.line:
                    if card.card_type == 'number':
                        num_cards += 1

                if num_cards == token.number - 3:
                    # Игрок выполнил условия для получения бонусного жетона
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
                    # Игрок не выполнил условия для получения жетона
                    self.tokens.remove(token)
                    self.score_stack.extend(self.line)
                    self.line = []
                    print(f"{self.name} не выполнил условия для получения жетона")
            else:
                # Игрок завершает линию без жетонов ставок
                self.score_stack.extend(self.line)
                self.line = []
                print(f"{self.name} завершил линию без ставки")
        else:
            print(f"{self.name} не имеет карт в линии для завершения")