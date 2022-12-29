from card import Card

SUITS = ['hearts', 'diamonds', 'spades', 'clubs']
VALUES = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
DECK = [Card(value, suit) for value in VALUES for suit in SUITS]