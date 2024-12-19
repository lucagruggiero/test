#Question 1
def score(team_name, wins, losses, ties):
    score = (wins + (ties)/2)/(wins + losses + ties)
    all_scores.append(team_name + ": " + str(score))
    
def main(teams):
    global all_scores
    all_scores = []
    for team in teams:
        score(*team)
    all_scores.sort(key = lambda x: x[1])

main([['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]])
print(all_scores)






#Question 2
import turtle
def draw_complete_bipartite(coord_list_1, coord_list_2):
    turtle.speed(0)
    turtle.penup()
    for coord1 in coord_list_1:
        for coord2 in coord_list_2:
            turtle.penup()
            turtle.setposition(coord1[0], coord1[1])
            turtle.pendown()
            turtle.setposition(coord2[0], coord2[1])
    turtle.hideturtle()
    turtle.done()
coord_list_1 = [[-200, 200], [-200, 90], [-50, -20]]
coord_list_2 = [[50, 200], [50, 170], [300, 90], [50, 30], [50, 0], [50, -13], [50, -73]]

draw_complete_bipartite(coord_list_1, coord_list_2)





#Question 3

#setup
import random
deck_of_cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

#draw random card and remove it from deck_of_cards
def draw_card():
    index = random.randint(0, len(deck_of_cards) - 1)
    return deck_of_cards.pop(index)

#calculate score of the hand
def calculate_hand_score(hand):
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11 #ace starts with 11 at first
        else:
            value += card
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value
def check_blackjack(hand):
    return len(hand) == 2 and calculate_hand_score(hand) == 21

#dealers turn until 17
def dealer_turn(dealer_hand):
    while calculate_hand_score(dealer_hand) <= 16:
        dealer_hand.append(draw_card())
    return dealer_hand

#display results and determine winner
def display_results(player_hand, dealer_hand):
    player_value = calculate_hand_score(player_hand)
    dealer_value = calculate_hand_score(dealer_hand)
    print()
    print("Final Results:")
    print()
    print("Your hand:", player_hand, "=", player_value)
    print("Dealer's hand:", dealer_hand, "=", dealer_value)
    print()
    if player_value > 21:
        print("You busted! Dealer wins.")
    elif dealer_value > 21:
        print("Dealer busts! You win!")
    elif check_blackjack(player_hand) and not check_blackjack(dealer_hand):
        print("You have Blackjack! You win!")
    elif check_blackjack(dealer_hand) and not check_blackjack(player_hand):
        print("Dealer has Blackjack! Dealer wins.")
    elif player_value > dealer_value:
        print("You win!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("You tied with the dealer!")  

def play_blackjack():
    global deck_of_cards
    deck_of_cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    #setup
    print()
    print("Let's play blackjack!")
    print()
    print("Player's hand:", player_hand)
    print("Dealer's hand: [", dealer_hand[0], ", ? ]")
    print()
    while True:
        player_value = calculate_hand_score(player_hand)
        if player_value >= 21:
            break
        choice = input("Do you want to hit or stand? ").strip().lower()
        if choice == 'hit':
            player_hand.append(draw_card())
            print("Player's hand: ", player_hand)
        elif choice == 'stand':
            break
        else:
            print("Invalid input. Please choose 'hit' or 'stand'.")
    #if player hasnt busted yet
    if calculate_hand_score(player_hand) <= 21:
        dealer_hand = dealer_turn(dealer_hand)

    #display final hand and results
    display_results(player_hand, dealer_hand)
def main():
    end = False
    play_blackjack()
    print()
    while not end:
        decision = input("Do you want to play again? ").strip().lower()
        if decision == "yes":
            end == False
            play_blackjack()
        elif decision == "no":
            end = True
            print("Thanks for playing!")
        else:
            print("Invalid input. Type 'yes' or 'no'.")
            end = False

main()
