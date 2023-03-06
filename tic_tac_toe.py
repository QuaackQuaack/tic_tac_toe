def board(value):
    print("------welcome to game tictactoe------")
    print(f'''
            {value[0]}  {value[1]}  {value[2]}
            {value[3]}  {value[4]}  {value[5]}
            {value[6]}  {value[7]}  {value[8]} \n''')
    print("this is sample of board where number reperesents position of 'X' and 'O'")

value_for_board = "012345678"
board(value_for_board)

#asking information with players

valid_marks = ['X','O']
print("in this section you need to choose \n")
n = 0 
while n < 1 : #to use continue we need some loop
  try:
    player1_mark= input("which mark do you want to play, either O or X? \n").upper()
    if player1_mark == "X": 
      print("player 2 your mark is O\n")
      player2_mark = 'O' #string ma xan hai input haru
    elif player1_mark =="O":
      print("\nplayer1 your mark is O")
      player2_mark = 'X'
    if player1_mark not in valid_marks:
        raise Exception()
  except:
    print("\t----warning---\t")
    print("User are requested to entered O and X only\n")
    continue
  n+=1
#note continue is used with for and while loop only :) so we used for in line 17

#to get X and O in each player turns
lst1 = ['X','O','X','O','X','O','X','O','X']
lst2 = ['O','X','O','X','O','X','O','X','O']
if player1_mark == "X" : choosing = lst1
else: choosing = lst2

#now gaming part
def gaming(choosing,value_for_board):
    checker = []
    count =  0 
    #------------------note try and except is remaing to code-------------- 
    #to convert string into list for assignment
    lst_value_for_board = [i for i in value_for_board]
    while count < 9 : # for debug lets put value of count as 2
        try:
            if count % 2 == 0:
                print(f"It is player one turn and his/her mark is {choosing[count]} \n")
                player1_entry = int(input("enter number between 0 to 8 only\n"))
                lst_value_for_board[player1_entry] = choosing[count]
                checker.append(player1_entry)
                board(lst_value_for_board)

          #  print(choosing[count]) #debug 
            else:
                print(f"It is player two turn and his/her mark is {choosing[count]} \n")
                player2_entry = int(input('enter number between 0 to 8 only\n'))
                lst_value_for_board[player2_entry] = choosing[count]
                checker.append(player2_entry)
                board(lst_value_for_board)
            #print(choosing[count]) #debug
            if player1_entry not in checker and  player2_entry not in checker:
                raise Exception()
        except:
            print("-------ok you need to play this seriously-------")
            print("please enter only X and O, only those slot which are not occupied\n")
            continue
        count +=1
    return checker,lst_value_for_board



#checker is to check whether the slot is already full or not
checker,lst_value_for_board = gaming(choosing,value_for_board)

#to determine which player is winner
def winner_determiner(lst_value_for_board):
    if lst_value_for_board[0]==lst_value_for_board[1]==lst_value_for_board[2]:
        print(f'Player with mark {lst_value_for_board[0]} wins the game. UwU')
    elif lst_value_for_board[0]==lst_value_for_board[3]==lst_value_for_board[6]:
        print(f'Player with mark {lst_value_for_board[0]} wins the game. UwU')
    elif lst_value_for_board[0]==lst_value_for_board[4]==lst_value_for_board[8]:
        print(f'Player with mark {lst_value_for_board[0]} wins the game. UwU')
    elif lst_value_for_board[3]==lst_value_for_board[4]==lst_value_for_board[5]:
        print(f'Player with mark {lst_value_for_board[3]} wins the game. UwU')
    elif lst_value_for_board[6]==lst_value_for_board[7]==lst_value_for_board[8]:
        print(f'Player with mark {lst_value_for_board[7]} wins the game. UwU')
    elif lst_value_for_board[2]==lst_value_for_board[4]==lst_value_for_board[6]:
        print(f'Player with mark {lst_value_for_board[6]} wins the game. UwU')
    elif lst_value_for_board[1]==lst_value_for_board[4]==lst_value_for_board[7]: 
        print(f'Player with mark {lst_value_for_board[4]} wins the game. UwU')
    elif lst_value_for_board[2]==lst_value_for_board[5]==lst_value_for_board[8]: 
        print(f'Player with mark {lst_value_for_board[2]} wins the game. UwU')
    else:
        continue

winner_determiner(choosing)
           
