def print_(board):
    """
    This funcion prints the current state of the board
    """
    print('  |  |')
    print(' ' + board[0] + ' | ' + board[1] + '|' + board[2])
    print('  |  |')
    print('------------')
    print('  |  |')
    print(' ' + board[3] + ' | ' + board[4] + '|' + board[5])
    print('  |  |')
    print('------------')
    print('  |  |')
    print(' ' + board[6] + ' | ' + board[7] + '|' + board[8])
    print('  |  |')

def check_win(board, player):
    """
    This function checks whether the player has won the game
    """
    if (board[0]==player and board[1]==player and board[2]==player)or \
       (board[3]==player and board[4]==player and board[5]==player)or \
       (board[6]==player and board[7]==player and board[8]==player)or \
       (board[0]==player and board[3]==player and board[6]==player)or \
       (board[1]==player and board[4]==player and board[7]==player)or \
       (board[2]==player and board[5]==player and board[8]==player)or \
       (board[0]==player and board[4]==player and board[8]==player)or \
       (board[2]==player and board[4]==player and board[6]==player):
        return True
    else:
        return False

def play_game():
        """ This function plays the tic tac toe game. """
        board=['']*9
        player='X'
        game_over=False
        print("Let's play Tic Tac Toe!")
        print_(board)

        while not game_over:
            print(f"It's {player}'s turn.")
            position=int(input("Enter a position(1-9):"))-1
            if board[position]=='':
                board[position]=player
            else:
                print("That position is already taken.Try again..")
                continue
            print_(board)

            if check_win(board, player):
                print(f'Hurray!! {player} wins!CONGRATULATIONS:-)')
                game_over=True
            elif '' not in board :
                print("It's a tie!")
                game_over=True
            else:
                player='O' if player=='X' else 'X'
            
if __name__=='__main__':
    play_game()
