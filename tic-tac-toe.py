def valid_moves(board):
    valid = []
    for slots in board:
        try:
            slot = int(slots)
            valid.append(slot)
        except:
            continue

    return valid
    
def is_valid_move(board, pos, player):
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
    print('+-----------+\n', end='')
    print('| ', ' | '.join(board[0:3]), ' |', sep='')
    print('|---|---|---|') 
    print('| ', ' | '.join(board[3:6]), ' |', sep='')
    print('|---|---|---|') 
    print('| ', ' | '.join(board[6:9]), ' |', sep='')
    print('+-----------+\n')

def is_game_over(board, winning_combo):
    for combo in winning_combo:
        sample = board[combo[0]]
        if sample == board[combo[0]] and sample == board[combo[1]] and sample == board[combo[2]]:
            if sample == 'X':
                print('Player 1 has won!')
            elif sample == 'O':
                print('Player 2 has won!')
                
            return True
        
    return False

def main():
    is_game_won = False
    
    winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                 (6, 4, 2), (3, 4, 5), (0, 1, 2), (6, 7, 8)]
    
    board = ['0', '1', '2',
             '3', '4', '5',
             '6', '7', '8']

    player = 'Player 1'
    print_board(board)
    valid = valid_moves(board)
    while not is_game_won:

        pos = int(input(player + ', ender index: '))

        if is_valid_move(board, pos, player):
            if player == 'Player 1':
                move(board, pos, player)
                player = 'Player 2'
            else:
                move(board, pos, player)
                player = 'Player 1'

            is_game_won = is_game_over(board, winning_combo)
            valid = valid_moves(board)
            if len(valid) == 0:
                print('No one won.')
                break
            print_board(board)
                  
if __name__ == '__main__':
    main()
