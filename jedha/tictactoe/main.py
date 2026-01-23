# main.py

from models import Player
from services import GameManager


player_x = Player("Elliot", "X")
player_o = Player("Marc", "O")
game = GameManager(player_x, player_o)

print("Tic Tac Toe")
print("Enter row and column (0-2) separated by space.")
game.board.display()

while True:
    print(f"{game.current_player}'s turn:")
    try:
        user_input = input("Row Col: ").strip().split()
        row, col = int(user_input[0]), int(user_input[1])
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Enter values between 0 and 2.")
            continue
    except (ValueError, IndexError):
        print("Invalid input. Enter two numbers.")
        continue
    
    if not game.play_turn(row, col):
        break

if __name__ == "__main__":
    run_game()