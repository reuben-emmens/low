class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    # need this method to be able to print the Card in a readable way
    def __repr__(self) -> str:
        return f"({self.value} of {self.suit})"