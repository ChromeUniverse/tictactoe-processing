# DEVELOPMENT LOG:
#
#
# valid()      DONE
# play()       DONE
# win_line()   DONE
# win_col()    DONE
# win_row()    DONE
# win_diag()   DONE
# check_win()  DONE
# game loop    DONE
#
#

board_size = 3
line = [0 for i in range(board_size)]
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]

def board_print():
    for row in board:
        print(row)

# checks if the move was valid or not
# DONE! 
def valid(row, col):
    if board[row][col] != 0:
        return False
    else:
        return True

# main play function here 
def play(player, row, col):
    #checking if valid
    if valid(row,col) == False:
        return 0 # invalid move
    
    elif valid(row,col) == True:
        board[row][col] = player # updates board with player number
        return 1 # valid move

# function that checks wins line by line
# is called by other functions
# DONE!
def win_line(board_line):
    if board_line[0] != 0 :
        if board_line[0] == board_line[1]:
            if board_line[1] == board_line[2]:
                return True
    return False






# checking collumns
# DONE!
def win_row():
    for row_array in board:
        if win_line(row_array) == True:
            return row_array[0] #returns winning player
    return False
            
                   
# checking rows
# DONE!
def win_col():
    for col in range(board_size):
        col_array = []
        for row in range(board_size):
            col_array.append(board[row][col])
        if win_line(col_array) == True:
            return col_array[0] # return winning player
    return False
    
# checking diagonals
# DONE!
def win_diag():
    diag_main = [board[row][row] for row in range(3)]
    if win_line(diag_main) == True:
        return diag_main[0] # returns winning player
    diag_secn = [board[row][2-row] for row in range(3)]
    if win_line(diag_secn) == True:
        return diag_secn[0]
    return False
    
    
    
# main win check function here
# DONE!
def check_win():
    col = win_col()
    row = win_row()
    diag = win_diag()
    if col != False:
        return col #returns winning player
    if row != False:
        return row
    if diag != False:
        return diag
    return False
        




# Game loop

winner = False # keeps loop running
while winner == False :
    
    while winner == False:
        print('Player 1')
        row , col = [int(num) for num in input().split()] # input()
        result = play(1, row, col) # play
        if result == 1: # valid
            winner = check_win() # updates game_over
            board_print()
            break
        if result == 0: # invalid
            print('invalid, enter again')
    
    while winner == False:
        print('Player 2')
        row , col = [int(num) for num in input().split()] # input()
        result = play(2, row, col) # play
        if result == 1: # valid
            winner = check_win() # updates game_over
            board_print()
            break
        if result == 0: # invalid
            print('invalid, enter again')
            
print("Player " + str(winner) + ' wins the game!')
