
#Board_Structure
tictacBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
               '4': ' ' , '5': ' ' , '6': ' ' ,
               '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in tictacBoard:
    board_keys.append(key)




#This function will displays the tictactoe board
def displayBoard(board):

    print(board['7'] + '|' + board['8'] + '|'+ board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():
    turn = 'X'   
    count = 0

    for i in range (10):
        displayBoard(tictacBoard)
        print("It's your turn " + turn + "move to which place?")
        move = input()

        if tictacBoard[move] == ' ':
            tictacBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if tictacBoard['7'] == tictacBoard['8'] == tictacBoard['9'] != ' ': # top
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif tictacBoard['4'] == tictacBoard['5'] == tictacBoard['6'] != ' ': # mid
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif tictacBoard['1'] == tictacBoard['2'] == tictacBoard['3'] != ' ': # bottom
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif tictacBoard['1'] == tictacBoard['4'] == tictacBoard['7'] != ' ': # Rightside
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif tictacBoard['2'] == tictacBoard['5'] == tictacBoard['8'] != ' ': # mid
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif tictacBoard['3'] == tictacBoard['6'] == tictacBoard['9'] != ' ': # left
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif tictacBoard['7'] == tictacBoard['5'] == tictacBoard['3'] != ' ': # pahalang haha
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif tictacBoard['1'] == tictacBoard['5'] == tictacBoard['9'] != ' ': # pahalang din haha
                displayBoard(tictacBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If the board is full of x and o this will print gameover and the game is tie.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # This will change the turn O and X
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
        # Ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")  
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            tictacBoard[key] = " "

    game()
if __name__ == "__main__":
    game()