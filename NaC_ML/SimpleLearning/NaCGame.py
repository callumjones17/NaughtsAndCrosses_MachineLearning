import csv
import os
from random import randint
from msvcrt import getch
import subprocess as sp

turn1 = []
turn3 = []
turn5 = []
turn7 = []

with open('Turn1.csv', newline='') as myFile:  
    reader = csv.reader(myFile)
    for row in reader:
        turn1.append(row)
with open('Turn3.csv', newline='') as myFile:  
    reader = csv.reader(myFile)
    for row in reader:
        turn3.append(row)
with open('Turn5.csv', newline='') as myFile:  
    reader = csv.reader(myFile)
    for row in reader:
        turn5.append(row)
with open('Turn7.csv', newline='') as myFile:  
    reader = csv.reader(myFile)
    for row in reader:
        turn7.append(row)

def display(gamescreen):
    first_line = '  ' + gamescreen[0] + ' | ' + gamescreen[1] + ' | ' + gamescreen[2] + '          ' + '1 | 2 | 3'
    second_line = ' ' + '-----------' + '        ' + '-----------' 
    third_line = '  ' + gamescreen[3] + ' | ' + gamescreen[4] + ' | ' + gamescreen[5] + '          ' + '4 | 5 | 6'
    fourth_line = ' ' + '-----------' + '        ' + '-----------'
    fith_line = '  ' + gamescreen[6] + ' | ' + gamescreen[7] + ' | ' + gamescreen[8] + '          ' + '7 | 8 | 9'
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fith_line)
    return

def randFunc(gamescreen):
    #turn = randint(0,8)
    comparator = []
    for pos in range(0,9):
        if gamescreen[pos+9]=='-':
            continue
        for beads in range(1,int(gamescreen[pos+9])+1):
            comparator.append(pos)
    turn = comparator[randint(0,len(comparator))-1]
    #print(comparator)
    return turn

def valid_key_press(gamescreen):
    valid_key = False
    while valid_key != True:
        key_pressed = ord(getch())
        if key_pressed > 48 and key_pressed < 58:
            if gamescreen[(key_pressed-49)] == '-':
                valid_key = True
                #print(key_pressed-49)
            else:
                print('Invalid Key')
        else:
            print('Invalid Key')
    return key_pressed-49

def check_for_winner(gamescreen):
    #0-No Winner
    #1 - O's win
    #2 - X's win
    #3 - Draw
    winner = 0
    #Across the Top
    if gamescreen[0] == gamescreen[1] and gamescreen[0] == gamescreen[2]:
        if gamescreen[0] == 'X':
            winner = 2
        elif gamescreen[0] == 'O':
            winner = 1
    #Left Side
    if gamescreen[0] == gamescreen[3] and gamescreen[0] == gamescreen[6]:
        if gamescreen[0] == 'X':
            winner = 2
        elif gamescreen[0] == 'O':
            winner = 1
    #Bottom
    if gamescreen[6] == gamescreen[7] and gamescreen[6] == gamescreen[8]:
        if gamescreen[6] == 'X':
            winner = 2
        elif gamescreen[6] == 'O':
            winner = 1
    #Right Side
    if gamescreen[2] == gamescreen[5] and gamescreen[2] == gamescreen[8]:
        if gamescreen[2] == 'X':
            winner = 2
        elif gamescreen[2] == 'O':
            winner = 1
    #Diag Left Top
    if gamescreen[0] == gamescreen[4] and gamescreen[0] == gamescreen[8]:
        if gamescreen[0] == 'X':
            winner = 2
        elif gamescreen[0] == 'O':
            winner = 1
    #Diag Right Top
    if gamescreen[2] == gamescreen[4] and gamescreen[2] == gamescreen[6]:
        if gamescreen[2] == 'X':
            winner = 2
        elif gamescreen[2] == 'O':
            winner = 1
    #Middle Hor
    if gamescreen[1] == gamescreen[4] and gamescreen[1] == gamescreen[7]:
        if gamescreen[1] == 'X':
            winner = 2
        elif gamescreen[1] == 'O':
            winner = 1
    #Middle Ver
    if gamescreen[3] == gamescreen[4] and gamescreen[3] == gamescreen[5]:
        if gamescreen[3] == 'X':
            winner = 2
        elif gamescreen[3] == 'O':
            winner = 1
    return winner

def process_win(index1,index1Pos,index3,index3Pos, index5,index5Pos, index7,index7Pos, winner):
    turn1.clear()
    turn3.clear()
    turn5.clear()
    turn7.clear()
    with open('Turn1.csv', newline='') as myFile:  
        reader = csv.reader(myFile)
        for row in reader:
            turn1.append(row)
    with open('Turn3.csv', newline='') as myFile:  
        reader = csv.reader(myFile)
        for row in reader:
            turn3.append(row)
    with open('Turn5.csv', newline='') as myFile:  
         reader = csv.reader(myFile)
         for row in reader:
            turn5.append(row)
    with open('Turn7.csv', newline='') as myFile:  
        reader = csv.reader(myFile)
        for row in reader:
            turn7.append(row)

    os.remove('Turn1.csv')
    os.remove('Turn3.csv')
    os.remove('Turn5.csv')
    os.remove('Turn7.csv')

    if winner == 2:
        #turn1[0][index1] = turn1[0][index1]
        #print('do nothing')
        if int(turn1[index1][9+index1Pos])!=1: turn1[index1][9+index1Pos]=int(turn1[index1][9+index1Pos])-1
        if int(turn3[index3][9+index3Pos])!=1: turn3[index3][9+index3Pos]=int(turn3[index3][9+index3Pos])-1
        if int(turn5[index5][9+index5Pos])!=1: turn5[index5][9+index5Pos]=int(turn5[index5][9+index5Pos])-1
        if had_turn7: 
            if int(turn7[index7][9+index7Pos])!=1: turn7[index7][9+index7Pos]=int(turn7[index7][9+index7Pos])-1
        print('You Win! Please Wait...')
    elif winner == 1:
        print('I Win, Please Wait...')
        turn1[index1][9+index1Pos]=int(turn1[index1][9+index1Pos])+5
        turn3[index3][9+index3Pos]=int(turn3[index3][9+index3Pos])+5
        turn5[index5][9+index5Pos]=int(turn5[index5][9+index5Pos])+5
        if had_turn7: turn7[index7][9+index7Pos]=int(turn7[index7][9+index7Pos])+5
        #print('do nothing 2')
    elif winner == 3:
        print('Draw! Please Wait...')
        turn1[index1][9+index1Pos]=int(turn1[index1][9+index1Pos])+3
        turn3[index3][9+index3Pos]=int(turn3[index3][9+index3Pos])+3
        turn5[index5][9+index5Pos]=int(turn5[index5][9+index5Pos])+3
        if had_turn7: turn7[index7][9+index7Pos]=int(turn7[index7][9+index7Pos])+3
        #print('do nothing 3')

    turn1File = open('Turn1.csv', 'w', newline='')  
    with turn1File:  
        writer = csv.writer(turn1File)
        writer.writerows(turn1)

    turn3File = open('Turn3.csv', 'w', newline='')  
    with turn3File:  
        writer = csv.writer(turn3File)
        writer.writerows(turn3)

    turn5File = open('Turn5.csv', 'w', newline='')  
    with turn5File:  
        writer = csv.writer(turn5File)
        writer.writerows(turn5)

    turn7File = open('Turn7.csv', 'w', newline='')  
    with turn7File:  
        writer = csv.writer(turn7File)
        writer.writerows(turn7)
    return

#Testing
#turn1[0][randFunc(turn1[0])] = 'O'
#turn3[0][randFunc(turn3[0])] = 'O'
#display(turn1[0])
#display(turn3[0])
winner = False
while winner != True:

    index1 =  0
    index3 = -1
    index5 = -1
    index7 = -1
    index1Pos = 0
    index3Pos = 0
    index5Pos = 0
    index7Pos = 0
    had_turn7 = False

    #Turn1
    currentTurn = turn1[0]
    #turn1[0][randFunc(turn1[0])] = 'O'
    index1Pos = randFunc(currentTurn)
    currentTurn[index1Pos] = 'O'
    display(currentTurn)

    #Turn2
    print('Please select a Position:')
    play_move = valid_key_press(currentTurn)
    currentTurn[play_move] = 'X'
    sp.call('cls',shell=True)
    display(currentTurn)

    #Turn3
    for turn3s in turn3:
        index3=index3+1
        if turn3s[0:8] == currentTurn[0:8]:
            currentTurn=turn3s
            break
    #turn3[index3][randFunc(turn3[index3])] = 'O'
    index3Pos = randFunc(currentTurn)
    currentTurn[index3Pos] = 'O'
    sp.call('cls',shell=True)
    display(currentTurn)

    #Turn4
    print('Please select a Position:')
    play_move = valid_key_press(currentTurn)
    #turn3[index3][play_move] = 'X'
    currentTurn[play_move] = 'X'
    sp.call('cls',shell=True)
    display(currentTurn)

    #Turn5
    for turn5s in turn5:
        index5=index5+1
        if turn5s[0:8] == turn3[index3][0:8]:
            currentTurn = turn5s
            break
    #turn5[index5][randFunc(turn5[index5])] = 'O'
    index5Pos = randFunc(currentTurn)
    currentTurn[index5Pos] = 'O'
    sp.call('cls',shell=True)
    display(currentTurn)
    win = check_for_winner(currentTurn)
    if win != 0:
        winner = True
        break

    #Turn6
    print('Please select a Position:')
    play_move = valid_key_press(currentTurn)
    #turn5[index5][play_move] = 'X'
    currentTurn[play_move] = 'X'
    sp.call('cls',shell=True)
    display(currentTurn)
    win = check_for_winner(currentTurn)
    if win != 0:
        winner = True
        break

    #Turn7
    for turn7s in turn7:
        index7=index7+1
        if turn7s[0:8] == turn5[index5][0:8]:
            currentTurn = turn7s
            break
    #turn7[index7][randFunc(turn7[index7])] = 'O'
    index7Pos = randFunc(currentTurn)
    currentTurn[index7Pos] = 'O'
    sp.call('cls',shell=True)
    display(currentTurn)
    had_turn7 = True
    win = check_for_winner(currentTurn)
    if win != 0:
        winner = True
        break

    #Turn8
    print('Please select a Position:')
    play_move = valid_key_press(currentTurn)
    currentTurn[play_move] = 'X'
    sp.call('cls',shell=True)
    display(currentTurn)
    win = check_for_winner(currentTurn)
    if win != 0:
        winner = True
        break

    #Turn9
    index9 = -1
    for spot in currentTurn:
        index9 = index9+1
        if spot == '-':
            break
    currentTurn[index9] = 'O'
    sp.call('cls',shell=True)
    display(currentTurn)
    win = check_for_winner(currentTurn)
    if win != 0:
        winner = True
        break
    if win == 0: win=3
    winner = True
process_win(index1,index1Pos,index3,index3Pos,index5,index5Pos,index7,index7Pos,win)
print('End of Game, Please Restart!')