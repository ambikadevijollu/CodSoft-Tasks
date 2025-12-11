import random

def display_title():
    print("\n============================")
    print("     ROCK • PAPER • SCISSORS")
    print("============================\n")

def get_player_choice():
    options = ["rock", "paper", "scissors"]
    while True:
        choice = input("Your move (rock/paper/scissors): ").strip().lower()
        if choice in options:
            return choice
        print("Invalid input! Try again.\n")

def find_winner(player, computer):
    if player == computer:
        return "tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "player"
    return "computer"

def play():
    display_title()
    scores = {"player": 0, "computer": 0, "tie": 0}

    while True:
        player = get_player_choice()
        computer = random.choice(["rock", "paper", "scissors"])

        print(f"Computer chose: {computer}")

        result = find_winner(player, computer)

        if result == "player":
            print("🎉 You win this round!")
            scores["player"] += 1
        elif result == "computer":
            print("💻 Computer wins this round!")
            scores["computer"] += 1
        else:
            print("🤝 It's a tie!")
            scores["tie"] += 1

        print(f"\nScore → You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['tie']}\n")

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\n====== FINAL RESULT ======")
    print(f"You: {scores['player']}")
    print(f"Computer: {scores['computer']}")
    print(f"Ties: {scores['tie']}")

    if scores["player"] > scores["computer"]:
        print("\n🏆 You won the game!")
    elif scores["player"] < scores["computer"]:
        print("\n💻 Computer won the game!")
    else:
        print("\n🤝 Match tied!")

    print("\nThanks for playing!")

if __name__ == "__main__":
    play()
