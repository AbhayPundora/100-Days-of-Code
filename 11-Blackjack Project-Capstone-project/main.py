from art import logo
import random

should_continue = True

def start_game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    computer = []

    def choose_cards(player,times):
        for i in range(0,times):
            player.append(random.choice(cards))

    choose_cards(user,2)
    choose_cards(computer,2)

    def check_blackjack(player_cards):
        if sum(player_cards) == 21:
            return 1


    def blackjack():
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer's first card: {computer[0]}")

        another_card = input("Type 'y' to get another card, type 'n' to pass:")

        if another_card == "y":
            choose_cards(user,1)
            if sum(user) > 21:
                if 11 in user:
                    user[user.index(11)] = 1
                    blackjack()
                else:
                    print(f"Your final hand: {user}, final score: {sum(user)}")
                    print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                    print("You went over. You lose 😭")
            else:
                blackjack()

        else:
            print(f"Your final hand: {user}, final score: {sum(user)}")

            while sum(computer) < 17:
                choose_cards(computer, 1)

            while sum(computer) > 21 and 11 in computer:
                computer[computer.index(11)] = 1

            if sum(computer) > 21:
                print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
                print("Opponent went over. You win 🥳")
                return

            print(f"Computer's final hand: {computer}, final score: {sum(computer)}")

            if check_blackjack(user) == 1 and len(user) == 2:
                print("Blackjack! you win!🥳")
            elif check_blackjack(computer) == 1 and len(computer) == 2:
                print("Blackjack! opponent win!😱")
            elif sum(user) > sum(computer):
                print("You win!🥳")
            elif sum(computer) > sum(user):
                print("You lose!😭")
            else:
                print("draw!😒")

    blackjack()

while should_continue:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()
    if play == 'y':
        start_game()
    else:
        should_continue = False