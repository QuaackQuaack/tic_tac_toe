#making of board
def board(value):
    print("welcome to game tictactoe ")
    print("\n")
    print(f'''
            {value[0]}  {value[1]}  {value[2]}
            {value[3]}  {value[4]}  {value[5]}
            {value[6]}  {value[7]}  {value[8]} \n''')
    print("this is sample of board where number reperesents position of 'X' and 'O'")

value_for_board = "012345678"
board(value_for_board)

#asking information with players
def asking_personal_info():
    valid_marks = ['X','O']
    print("in this section you need to give you personal info\n")
    player1_mark= input("which mark do you want to play, either O or X? \n").upper()
    try:
        if player1_mark == "X": 
            print("player 2 your mark is O\n")
            player2_mark = 'O' #string ma xan hai input haru
        else:
            print("player 2 your mark is X")
            player2_mark = 'X'
        if player1_mark not in valid_marks: 
            raise Exception

    except:
        print("please yr don't be oversmart , just choose between X and O\n")
        
       
    return player1_mark , player2_mark 
player1_mark, player2_mark = asking_personal_info()

#to get X and O in each player turns
lst1 = ['X','O','X','O','X','O','X','O','X']
lst2 = ['O','X','O','X','O','X','O','X','O']
if player1_mark == "X" : choosing = lst1
else: choosing = lst2

#now gaming part
count = 0 
replacer = str()
def gaming(choosing,value_for_board,count,replacer):
    checker = []
    while count < 9 : # for debug lets put value of count as 2
        if count % 2 == 0:
            print(f"It is player one turn and he/she mark is {choosing[count]} \n")
            player1_entry = int(input("enter number between 0 to 9 only\n"))`
            checker.append(player1_entry)
          #  print(choosing[count]) #debug
            replacer = replacer + choosing[count]
           # print(replacer) 
        
        else:
            print(f"It is player two turn and him/her mar is {choosing[count]} \n")
            player2_entry = int(input('enter number between 0 to 9 only\n'))
            checker.append(player2_entry)
          #  print(choosing[count]) #debug
            replacer = replacer + choosing[count]

        count += 1 

    return replacer

replacer = gaming(choosing, value_for_board,count,replacer)
print(replacer) 

#now to print final board 
board(replacer)






    


    

        
    
