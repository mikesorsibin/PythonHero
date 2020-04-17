#print('\n'*100) clear screen
#player1 = input("Please pick a marker 'X' or 'O'")


def displayboard(board):
    print('\n' *100)
    print(board[7] + '|' +board[8] + '|' +board[9])
    print('-----')
    print(board[4] + '|' +board[5] + '|' +board[6])
    print('-----')
    print(board[1] + '|' +board[2] + '|' +board[3])


test_board = ['#','X','O','X','O','X','O','X','O','X']
displayboard(test_board)
test_board1 = [' ']*10
displayboard(test_board1)


def player_input():
    marker = ''

    while marker!='X' and marker!='O':
        marker = input("Player1 please pick a marker 'X' or 'O':")
    player1= marker

    if player1 =='X':
        player2 ='O'
    else:
        player2 ='X'

    

    #print(f"Player 1 is {player1}")
    #print(f"Player 2 is {player2}")
    return (player1,player2)

    

    
player1,player2 = player_input()   
print(f"Player 1 is {player1}")
print(f"Player 2 is {player2}")



def place_marker(board,marker,position=0):
    print("This game takes position similar to a number in a keyboard.\nPlayer must take one turn at a time.\nThe firstplayer should play first and the second player second and so on")
    position = int(input("Enter a number from index 1-9 where you want to place your marker in the board:"))
    #print(position)
    board[position]=marker
    #if position == range(board[1:10]):
        #board = 
        
    


place_marker(test_board,'$')
displayboard(test_board)


def win_check(board,mark):
    return  board[1]==board[2]==board[3]== mark \
                                        or board[5]==board[6]==board[7]== mark \
                                        or board[7]==board[8]==board[9]== mark \
                                        or board[1]==board[5]==board[9]== mark \
                                        or board[3]==board[5]==board[7]== mark \
                                        or board[1]==board[4]==board[7]== mark \
                                        or board[2]==board[5]==board[8]== mark \
                                        or board[3]==board[6]==board[9]== mark \

print(win_check(test_board,'X'))



import random

def choose_first():
    
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'

print(choose_first())



def space_check(board,position):
    return board[position]== ' '

print(space_check(test_board,8))


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
            
print(full_board_check(test_board))


def player_choice(board):
    position = 0
    if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        postion = int(input("Choose your next position : (1-9)"))
    return position

def replay():
    return input("Do you want to play again ?Enter yes or no :").lower().startswith("y")


print(replay())


print("Welcomee to tic tac toe")

while True:
    the_board = [' ']*10
    player1,player2 = player_input()
    turn = choose_first()
    print(turn + "will go first" )

    play_game = input("Are you ready to play? Enter yes or no")

    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn =='player 1':
            displayboard(the_board)
            position = player_choice(the_board)
            place_marker(board,marker,position)

            if win_check(theBoard, player1_marker):
                displayboard(the_Board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    displayboard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    
                
            
                
            
            

        else:
            # Player2's turn.
            
            displayboard(the_board)
            position = player_choice(the_board)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                displayboard(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    displayboard(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    
     
       

            
    
    
        

     
    
    
    
    
    

