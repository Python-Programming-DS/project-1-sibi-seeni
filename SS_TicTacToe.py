# File : SS_TicTacToe.py
# Date : 09/20/2025
#   A program to play a two-player Tic-Tac-Toe game implementation
#
#   by : Sibi Seenivasan 

def resetBoard():
    # Fresh board
    return [[" " for _ in range(3)] for _ in range(3)]

def printBoard(board):
    # Current state of board with exact formatting
    print("-----------------")
    print("R\\C | 0 | 1 | 2 |")
    print("-----------------")
    for idx, row in enumerate(board):
        # Join with '|' and surround with '|'
        print(f"{idx}   | {' | '.join(cell if cell != ' ' else ' ' for cell in row)} |")
        print("-----------------")
    print() # Add a newline after the board

def validateEntry(row, col, board):
    # If move is within range and cell is empty
    # This check is actually handled explicitly in the main loop to match the sample output's error messages
    if 0 <= row <= 2 and 0 <= col <= 2:
        return board[row][col] == " "
    return False

def checkFull(board):
    # Returns True if cells are filled
    for row in board:
        if " " in row:
            return False
    return True

def checkWin(board, turn):
    # Checks for 3-in-a-row horizontally, vertically, or diagonally win
    for i in range(3):
        # Horizontal check
        if all(board[i][j] == turn for j in range(3)):
            return True
        # Vertical check
        if all(board[j][i] == turn for j in range(3)):
            return True
    # Diagonals check
    if all(board[i][i] == turn for i in range(3)) or all(board[i][2 - i] == turn for i in range(3)):
        return True
    return False

def checkEnd(board, turn):
    # Returns True if the game is over (win or draw)
    return checkWin(board, turn) or checkFull(board)

def get_input(turn):
    # Prompts for input and returns cleaned row/col strings and the raw input string
    print(f"{turn}'s turn")
    print(f"Where do you want your {turn} placed?")
    print("Please enter row number and column number separated by a comma")
    move = input().strip()
    return move

def main():
    # Main game loop
    playing = True
    while playing:
        board = resetBoard()
        print("New Game: X goes first.")
        printBoard(board)
        turn = "X"
        
        while True:
            move = get_input(turn)
            
            # 1. Input parsing and basic format validation
            try:
                # Attempt to split and get strings, handling case where split(',') might not give 2 parts
                parts = move.split(",")
                row_str = parts[0].strip() if len(parts) > 0 else ""
                col_str = parts[1].strip() if len(parts) > 1 else ""
                
                # Attempt to convert to integers
                row, col = int(row_str), int(col_str)
                valid_format = True

            except (ValueError, IndexError):
                # Handle cases like "a,b", "1", "1,b", "a,1"
                valid_format = False
                row_str, col_str = move.split(",") if ',' in move else (move, "")
                row_str = row_str.strip()
                col_str = col_str.strip()
                # Print what was *entered* for row/col
                print(f"You have entered row #{row_str}")
                print("\t\t\tand column #", col_str)
                
            # 2. Validation for out-of-range (0, 1, or 2)
            if valid_format and not (0 <= row <= 2 and 0 <= col <= 2):
                print(f"You have entered row #{row}")
                print(f"\t\t\tand column #", col)
                print() # Empty line from sample
                print("Invalid entry: try again.")
                print("Row & column numbers must be either 0, 1, or 2.")
                continue
                
            # 3. Validation for non-numeric or malformed input
            if not valid_format:
                # Use the strings that failed conversion to match sample output
                print("Invalid entry: try again.")
                print("Row & column numbers must be either 0, 1, or 2.")
                continue

            # 4. Validation for cell already taken (must be after valid_format and range check)
            if not validateEntry(row, col, board):
                print(f"You have entered row #{row}")
                print(f"and column #{col}")
                print("That cell is already taken.")
                print("Please make another selection.")
                continue

            # Valid move
            print(f"You have entered row #{row}")
            print(f"\t  and column #{col}")
            print("Thank you for your selection.")
            
            board[row][col] = turn
            printBoard(board)

            if checkWin(board, turn):
                print(f"{turn} IS THE WINNER!!!")
                break
            
            if checkFull(board):
                print("DRAW! NOBODY WINS!")
                break
            
            # Switch turn
            turn = "O" if turn == "X" else "X"

        print("Another game? Enter Y or y for yes.")
        response = input().strip()
        if response.lower() != "y":
            playing = False
            print("Thank you for playing!")

if __name__ == "__main__":
    main()