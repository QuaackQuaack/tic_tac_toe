import random 
result_for_human= (('p','r'),('r','s'),('s','p'))
result_for_pc = (('r','p'),('s','r'),('p','s'))
draw = (('r','r'),('s','s'),('p','p'))
computer = ('r','p','s')
score = {'bot' : 0 , 'user' : 0 }  
valid = ['r','p','s','']
while True:
    try:
        user = input('''Enter you data 
                 for rock enter R 
                 for paper enter P 
                 for scissor enter S ''').lower()
        if user not in valid:
            raise Exception()
    except:
        print('only enter r  , p , s')
        continue
    if len(user) < 1: break
    decision = (user,random.choice(computer))
    print(decision)
    for x in range(0,3):
        if decision == result_for_human[x]:
            print('you have won\n')
            score['user']= score.get('user',0) + 1
            break
        elif decision == result_for_pc[x]:
            print('computer had won\n')
            score['bot']= score.get('bot',0) + 1
            break
        elif decision == draw[x]:
            print('it is draw')
        
            

    print(f'the scoreboard is {score}\n')


    



