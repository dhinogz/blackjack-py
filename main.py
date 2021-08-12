from os import system
from art import logo
from functions import deal_card, calculate_score, compare, show_initial_score, show_final_score

def play_game():
	print(logo)

	users_cards, dealers_cards = [], []
	[users_cards.append(deal_card()) for _ in range(2)]
	[dealers_cards.append(deal_card()) for _ in range(2)]

	dealers_score = calculate_score(dealers_cards)
	
	keep_drawing = True
	while keep_drawing:
		users_score = calculate_score(users_cards)
		show_initial_score(users_cards, dealers_cards)
		if users_score == 0 or dealers_score == 0 or users_score > 21:
			keep_drawing = False
		else:
			if input("Type 'y' to get another cards, type 'n' to pass: ") == 'n':
				keep_drawing = False
			else:
				users_cards.append(deal_card())
		
	while dealers_score < 17 and dealers_score != 0 and users_score != 0:
		dealers_cards.append(deal_card())
		dealers_score = calculate_score(dealers_cards)

	result = compare(users_score, dealers_score)
	show_final_score(users_cards, dealers_cards, result)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
	system('cls')
	play_game()
	

