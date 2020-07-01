ttt_board = ['0', '1', '2',
             '3', '4', '5',
             '6', '7', '8']

winning_combo = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                 (6, 4, 2), (3, 4, 5), (0, 1, 2), (6, 7, 8)]

player = 'Player 1'

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

def is_game_over(ctx, board, winning_combo):
    for combo in winning_combo:
        sample = board[combo[0]]
        if sample == board[combo[0]] and sample == board[combo[1]] and sample == board[combo[2]]:
            if sample == 'X':
                return 'Player 1 has won! Resetting board...'
            elif sample == 'O':
                return 'Player 2 has won! Resetting board...'

            board = ['0', '1', '2','3', '4', '5','6', '7', '8']
            return board
        
    return False

@bot.command()
async def ttt(ctx, pos=''):
    global ttt_board
    board = ttt_board
    global winning_combo
    global player
    
    try:
        if pos == '':
            display = '```\n' + '+-----------+' + \
            '\n| ' + ' | '.join(board[0:3]) + ' |' + \
            '\n|---|---|---|' + \
            '\n| ' + ' | '.join(board[3:6]) + ' |' + \
            '\n|---|---|---|' + \
            '\n| ' + ' | '.join(board[6:9]) + ' |' + \
            '\n+-----------+```'
            await ctx.send(display)
            return
        if pos == 'reset':
            await ctx.send('The board has been reset.')
            board = board = ['0', '1', '2','3', '4', '5','6', '7', '8']
            ttt_board = board
            return board
        else:
            pos = int(pos)
    except ValueError:
        await ctx.send('Sorry, only numbers are accepted.')
        return

    if is_valid_move(board, pos, player):
        msg = player + ' entered index ' + str(pos)
        await ctx.send(msg)
        if player == 'Player 1':
            move(board, pos, player)
            player = 'Player 2'
        else:
            move(board, pos, player)
            player = 'Player 1'

        display = '```\n' + '+-----------+' + \
        '\n| ' + ' | '.join(board[0:3]) + ' |' + \
        '\n|---|---|---|' + \
        '\n| ' + ' | '.join(board[3:6]) + ' |' + \
        '\n|---|---|---|' + \
        '\n| ' + ' | '.join(board[6:9]) + ' |' + \
        '\n+-----------+```'
        await ctx.send(display)

        is_game_won = is_game_over(ctx, board, winning_combo)
        if type(is_game_won) is not bool:
            await ctx.send(is_game_won)
            board = ['0', '1', '2','3', '4', '5','6', '7', '8']
            ttt_board = board
            return board
            
        valid = valid_moves(board)
        if len(valid) == 0:
            await ctx.send('No one won. Resetting board...')
            board = ['0', '1', '2','3', '4', '5','6', '7', '8']
            ttt_board = board
            return board

        msg = 'It is ' + player + "'s turn."
        await ctx.send(msg)
        return player
        return board

    if not is_valid_move(board, pos, player):
        await ctx.send('Sorry, that move is either out of bounds, or someone is already occuping that space.')
        return
