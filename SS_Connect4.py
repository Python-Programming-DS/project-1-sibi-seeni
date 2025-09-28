# File : SS_Connect4.py
# Date : 09/21/2025
#   A program to play Connect4
#
#   by : Sibi Seenivasan

def resetBoard():
    # Fresh Connect Four board
    return [['.' for _ in range(7)] for _ in range(6)]  # 6 rows, 7 columns

def printBoard(board):
    # Displays the board in the required output style with vertical bars and dashes
    separator = ' --- --- --- --- --- --- --- --- '
    
    # Print board from row 6 down to row 1
    for row in range(5, -1, -1):  
        # Print the dashed separator line above the row
        print(separator)
        
        # Build the row content
        line = f'| {row+1} ' 
        for col in range(7):
            cell_content = board[row][col] if board[row][col] != '.' else ' '
            line += f'| {cell_content} '
        line += '|' # Closing vertical bar
        print(line)
        
    print(separator)
    
    # Print the RC header row
    print('|R/C| a | b | c | d | e | f | g |')
    
    # Print the final bottom dashed line if needed for complete enclosure
    print(separator)


def validateEntry(board, col, row):
    # Validates that col ('a'-'g') and row (1-6) are valid
    col_indices = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6}
    if col not in col_indices or not (1 <= row <= 6):
        return False
    col_idx = col_indices[col]
    row_idx = row - 1
    # Check if the move is only in the lowest available row
    for r in range(6):
        if board[r][col_idx] == '.':
            return r == row_idx
    return False  # Column full

def checkFull(board):
    # Returns True if the board is full
    for col in range(7):
        if board[5][col] == '.':
            return False
    return True

def availablePosition(board):
    # Returns list of available positions
    cols = ['a','b','c','d','e','f','g']
    available = []
    for i, col in enumerate(cols):
        for row in range(6):
            if board[row][i] == '.':
                available.append(f'{col}{row+1}')
                break
    return available

def checkWin(board, turn):
    # Checks if the current player has won after their most recent move
    for r in range(6):
        for c in range(7):
            if board[r][c] == turn:
                # Check horizontal
                if c <= 3 and all(board[r][c+i]==turn for i in range(4)):
                    return True
                # Check vertical
                if r <= 2 and all(board[r+i][c]==turn for i in range(4)):
                    return True
                # Diagonal Lower Left to Upper Right
                if r <= 2 and c <= 3 and all(board[r+i][c+i]==turn for i in range(4)):
                    return True
                # Diagonal Upper Left to Lower Right
                if r >= 3 and c <= 3 and all(board[r-i][c+i]==turn for i in range(4)):
                    return True
    return False

def checkEnd(board, turn):
    # Returns True if game is over
    return checkWin(board, turn) or checkFull(board)

def main():
    # Game loop - alternating X and O,
    import sys
    cols = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6}
    players = ['X', 'O']
    print("New game: X goes first.") 
    while True:
        board = resetBoard()
        turn = 0  # 0 for X, 1 for O
        winner = None

        while True:
            printBoard(board)
            available = availablePosition(board)
            player = players[turn]
            
            available_str = '[' + ', '.join(f"'{pos}'" for pos in available) + ']' 
            
            prompt = (
                f"{player}'s turn.\n"
                f"Where do you want your {player} placed?\n"
                f"Available positions are: {available_str}\n"
                f"Please enter column-letter and row-number (e.g., a1): "
            )
            
            move = ""
            while True:
                move = input(prompt).strip()
                if len(move) == 2 and move[0] in cols and move[1] in '123456':
                    col = move[0]
                    row = int(move[1])
                    if validateEntry(board, col, row):
                        break
                print("Invalid entry. Try again.")
                
            print("Thank you for your selection.")
            
            # Place token
            col_idx = cols[col]
            row_idx = row - 1
            board[row_idx][col_idx] = player
            
            # Check for win/end
            if checkWin(board, player):
                printBoard(board)
                print(f"{player} IS THE WINNER!!!")
                winner = player
                break
            if checkFull(board):
                printBoard(board)
                print("It is a tie!")
                break
            turn = 1 - turn  # Switch player
            
        again = input("Another game (y/n)? ").strip().lower()
        if again != 'y':
            print("Thank you for playing!")
            sys.exit()

if __name__ == "__main__":
    main()
