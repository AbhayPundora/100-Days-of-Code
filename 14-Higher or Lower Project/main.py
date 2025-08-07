from  art import logo,vs
from game_data import data
import random

score = 0
def display_player(player, symbol):
    print(f"Compare {symbol}: {player["name"]}, {player["description"]}, from {player["country"]}")

def arrange_players(player_a, player_b):
        your_count = player_a["follower_count"]
        opponent_count = player_b["follower_count"]
        return your_count, opponent_count

def show_result(message):
        print("\n" * 50)
        print(logo)
        print(f"{message} {score}")

print(logo)
player_a = random.choice(data)
game_over = False

while not game_over:
    player_b = random.choice(data)

    if player_a == player_b:
        player_b = random.choice(data)

    else:
        display_player(player_a, "A")
        print(vs)
        display_player(player_b, "B")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == "a":
            user_guessed_followers, opponent_followers = arrange_players(player_a, player_b)

        else:
            user_guessed_followers, opponent_followers = arrange_players(player_b, player_a)


        if user_guessed_followers > opponent_followers:
            score += 1
            player_a = player_b
            show_result("You're right! Current score ")

        else:
            show_result("Sorry, that's wrong. Final score: ")
            game_over = True





