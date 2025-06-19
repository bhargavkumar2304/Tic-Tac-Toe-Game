board = [' ' for _ in range(9)] # Represents the 3x3 board, indexed 0-8

def print_board():
    """Prints the current state of the Tic-Tac-Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def player_move(player_symbol):
    """Handles a player's move, taking input and updating the board."""
    while True:
        try:
            position = int(input(f"Player {player_symbol}, enter your move (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == ' ':
                board[position] = player_symbol
                break
            else:
                print("Invalid move. That position is either taken or out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def check_win(player_symbol):
    """Checks if the given player has won the game."""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player_symbol:
            return True
    return False

def check_draw():
    """Checks if the game is a draw."""
    return ' ' not in board

def play_game():
    """Manages the main game loop."""
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        player_move(current_player)

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw():
            print_board()
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
