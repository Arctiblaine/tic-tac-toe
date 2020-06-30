'''
    Archie's Tic-Tac-Toe but it's in python.
    6/29/2020
    For Helpful Birb, hopefully.
'''
def is_valid_move(board, pos, player):
    ''' '''
    try:
        section = board[pos]
    except IndexError:
        return False
    if section == 'X' or section == 'O':
        return False
    
    return True

def move(board, pos, player):
    ''' '''
    if player == 'Player 1':
        board[pos] = 'X'
    else:
        board[pos] = 'O'

    return board

def print_board(board):
    ''' '''
    # should be like
    print('+-----------+\n', end='')
    print('| ', ' | '.join(board[0:3]), ' |', sep='')
    print('|---|---|---|') 
    print('| ', ' | '.join(board[3:6]), ' |', sep='')
    print('|---|---|---|') 
    print('| ', ' | '.join(board[6:9]), ' |', sep='')
    print('+-----------+\n')

def is_game_over(board, winning_combo):
    ''' '''
    for combo in winning_combo:
        if board[combo[0]] == board[combo[1]]:
            if board[combo[1]] == board[combo[2]]:
                if board[combo[1]] == 'X':
                    print('Player 1 won!')
                else:
                    print('Player 2 won!')
                return True
            return False
        return False
    # return which player won.
            

def main():
    ''' '''
    is_game_won = False
    
    winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                 (6, 4, 2), (3, 4, 5), (0, 1, 2), (6, 7, 8)]
    
    board = ['0', '1', '2',
             '3', '4', '5',
             '6', '7', '8']

    player = 'Player 1'

    while not is_game_won:
        print_board(board)

        pos = int(input(player + ', ender index: '))

        if is_valid_move(board, pos, player):
            if player == 'Player 1':
                move(board, pos, player)
                player = 'Player 2'
            else:
                move(board, pos, player)
                player = 'Player 1'

            is_game_won = is_game_over(board, winning_combo)
                  
main()

    

