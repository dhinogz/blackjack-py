import random

def deal_card():
	"""Returns a random card from a deck"""
	CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(CARDS)
	return card

def calculate_score(cards):
	"""Takes in a hand of cards and returns the calculated score"""
	score = sum(cards)
	# if [10, 11] == cards or [11, 10] == cards:
	if score == 21 and len(cards) == 2:
		return 0
	if score > 21 and 11 in cards:
		print(f"Your cards: {cards}, current score {sum(cards)}")
		cards.remove(11)
		cards.append(1)
		print("You went over. Ace is counted as 1")
	score = sum(cards)
	return score

def compare(user_score, dealers_score):
	"""Takes in the two players scores and returns winner"""
	if dealers_score == 0:
		return "Dealer wins with a Blackjack"
	elif user_score == 0:
		return "You win with a Blackjack"
	elif user_score == dealers_score:
		return "Draw"
	elif user_score > 21:
		return "You went over. Dealer wins"
	elif dealers_score > 21:
		return "Dealer went over. You win"
	else:
		if user_score > dealers_score:
			return "You win"
		elif user_score < dealers_score:
			return "Dealer wins"

def show_initial_score(users_cards, dealers_cards):
	"""Prints out users and dealers scores during the ongoing game"""
	print(f"Your cards: {users_cards}, current score {sum(users_cards)}")
	print(f"Dealers first card: {dealers_cards[0]}\n")


def show_final_score(users_cards, dealers_cards, result):
	"""Prints out the final scores"""
	print("------------\nFINAL RESULTS")
	print(f"Your cards: {users_cards}, final score {sum(users_cards)}")
	print(f"Dealers cards: {dealers_cards}, final score {sum(dealers_cards)}\n")
	print(result)