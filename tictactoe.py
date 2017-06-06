from random import randint

def draw_board(board):
    for i in range(3):
        row = '|'
        for j in range(3):
            row += board[(i,j)]+'|'
        print(row)
        print('______')

def check_win_condition(board):
    # cirles and exes in rows and columns - this check is scalable for a board larger than 3x3
    for i in range(3):
        circles_r, exes_r, circles_c, exes_c = 0, 0, 0, 0
        for j in range(3):
            # rows
            if board[(i,j)] == 'x':
                exes_r += 1
            elif board[(i,j)] == 'o':
                circles_r += 1
            # columns
            if board[(j,i)] == 'x':
                exes_c += 1
            elif board[(j,i)] == 'o':
                circles_c += 1
            
        if circles_r==3 or circles_c==3:
            return 'cirles'
        elif exes_r==3 or exes_c==3:
            return 'exes'
        
    # circles and exes diagonal
    if board[(0,0)] == 'x' and board[(1,1)] == 'x' and board[(2,2)] == 'x':
        return 'exes'
    elif board[(2,0)] == 'x' and board[(1,1)] == 'x' and board[(0,2)] == 'x':
        return 'exes'
    elif board[(0,0)] == 'o' and board[(2,2)] == 'o' and board[(2,2)] == 'o':
        return 'cirles'
    elif board[(2,0)] == 'o' and board[(1,1)] == 'o' and board[(0,2)] == 'o':
        return 'cirles'

    # TODO: check for tie - no spaces left

    # if nobody wins
    return False

def computer_move(board):
    x = randint(0,2)
    y = randint(0,2)
    while board[(x,y)] !=' ':
        x = randint(0,2)
        y = randint(0,2)
    board[(x,y)]='x'

def smart_computer_move(board):
    # Rule 1: If I have a winning move, take it.
    # TODO: make a functiona out of it
    for i in range(3):
        for j in range(3):
            # will this move make me win?
            temp = board[(i,j)]
            # lets check the situation when we make the move
            board[(i,j)] = 'x'
            if check_win_condition(board):
                return
            else: 
                # did not win - revert changes
                board[(i,j)] = temp
    
    # Rule 2: If the opponent has a winning move, block it.
    # TODO: make a functiona out of it
    for i in range(3):
        for j in range(3):
            # will this move make opponent win?
            temp = board[(i,j)]
            board[(i,j)] = 'o'
            if check_win_condition(board):
                board[(i,j)] = 'x'
                return
            else: 
                # he won't win this move - revert changes
                # TODO: 
                board[(i,j)] = temp
    
    # TODO: Rule 3: If I can create a fork (two winning ways) after this move, do it.
    # TODO: Rule 4: Do not let the opponent creating a fork after my move. (Opponent may block your winning move and create a fork.)
    # TODO: Rule 5: Place in the position such as I may win in the most number of possible ways.
    
    # while the above AI is not finished - we mage a random move
    computer_move(board)

def update_board(board, move):
    board[move] = 'o'

def convert_text_to_move(text):
    move_list = text.split(',')
    return (int(move_list[0]-1), int(move_list[1]-1))

board = {}
for i in range(3):
    for j in range(3):
        board[(i,j)] = ' '

draw_board(board)
# TODO: error handling
text = input("Where do you want to put the circle (-> x,y) ? ")
who_won = False

while not who_won:
    update_board(board, convert_text_to_move(text))
    who_won = check_win_condition(board)
    if not who_won:
        smart_computer_move(board)
    who_won = check_win_condition(board)
    draw_board(board)
    if who_won:
        print("Game end;", who_won, "won")
    else:
        text = input("Where do you want to put the circle (-> x,y) ? ")

