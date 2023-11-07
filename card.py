class Card:
    def __init__(self, number, color, card_type):
        self.number = number
        self.color = color
        self.card_type = card_type

    def __eq__(self, other):
        return self.number == other.number and self.color == other.color

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number