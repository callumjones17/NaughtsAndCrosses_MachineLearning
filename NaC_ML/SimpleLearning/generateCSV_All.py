import csv

#PC Always goes first, for this game.
# Turns 1, 3, 5, 7,  and 9

#Turn 1:
#1 Possibility
turns = []
#turns.append([1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18])
#myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']] 
for comb in range(0,1):
    combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
    turns.append(combination)

turn1File = open('Turn1.csv','w')
with turn1File:
    writer = csv.writer(turn1File)
    writer.writerows(turns)



# Turn 2:
turns = []
for turn1 in range(0,9):
    combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
    combination[turn1] = 'O'
    combination[turn1+9] = '0'
    turns.append(combination)
turn2File = open('Turn2.csv','w')
with turn2File:
    writer = csv.writer(turn2File)
    writer.writerows(turns)


#Turn 3:
#72 Possibilities
turns = []
for turn1 in range(0,9):
     for turn2 in range(0,9):
          combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
          if turn1==turn2:
              continue
          combination[turn1] = 'O'
          combination[turn2] = 'X'
          combination[turn1+9]='0'
          combination[turn2+9]='0'
          turns.append(combination)

turn3File = open('Turn3.csv','w')
with turn3File:
    writer = csv.writer(turn3File)
    writer.writerows(turns)


# Turn 4:
turns = []
for turn1 in range(0,9):
     for turn2 in range(0,9):
         for turn3 in range(0,9):
            combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
            if turn1==turn2 or turn1 == turn3 or turn2 == turn3:
                continue
            combination[turn1] = 'O'
            combination[turn2] = 'X'
            combination[turn3] = 'O'
            combination[turn1+9]='0'
            combination[turn2+9]='0'
            combination[turn3+9] ='0'
            turns.append(combination)

turn4File = open('Turn4.csv','w')
with turn4File:
    writer = csv.writer(turn4File)
    writer.writerows(turns)





#Turn 5:
turns = []
for turn1 in range(0,9):
     for turn2 in range(0,9):
         for turn3 in range(0,9):
             for turn4 in range(0,9):
                combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
                if turn1==turn2 or turn1==turn3 or turn2==turn3 or turn1==turn4 or turn2==turn4 or turn3==turn4:
                      continue
                combination[turn1] = 'O'
                combination[turn2] = 'X'
                combination[turn3] = 'O'
                combination[turn4] = 'X'
                combination[turn1+9]='0'
                combination[turn2+9]='0'
                combination[turn3+9]='0'
                combination[turn4+9]='0'
                turns.append(combination)

turn5File = open('Turn5.csv','w')
with turn5File:
    writer = csv.writer(turn5File)
    writer.writerows(turns)




#Turn 6:
turns = []
for turn1 in range(0,9):
     for turn2 in range(0,9):
         for turn3 in range(0,9):
             for turn4 in range(0,9):
                 for turn5 in range(0,9):
                    combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
                    if turn1==turn2 or turn1==turn3 or turn2==turn3 or turn1==turn4 or turn2==turn4 or turn3==turn4 or turn1 == turn5 or turn2 == turn5 or turn3 == turn5 or turn4 == turn5:
                        continue
                    combination[turn1] = 'O'
                    combination[turn2] = 'X'
                    combination[turn3] = 'O'
                    combination[turn4] = 'X'
                    combination[turn5] = 'O'
                    combination[turn1+9]='0'
                    combination[turn2+9]='0'
                    combination[turn3+9]='0'
                    combination[turn4+9]='0'
                    combination[turn5+9]='0'
                    turns.append(combination)

turn6File = open('Turn6.csv','w')
with turn6File:
    writer = csv.writer(turn6File)
    writer.writerows(turns)



#Turn 7:
turns = []
for turn1 in range(0,9):
     for turn2 in range(0,9):
         for turn3 in range(0,9):
             for turn4 in range(0,9):
                 for turn5 in range(0,9):
                     for turn6 in range(0,9):
                        combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
                        if turn1==turn2 or turn1==turn3 or turn2==turn3 or turn1==turn4 or turn2==turn4 or turn3==turn4 or turn1==turn5 or turn1==turn6 or turn2==turn5 or turn2==turn6 or turn3==turn5 or turn3==turn6 or turn4==turn5 or turn4==turn6 or turn5==turn6:
                            continue
                        combination[turn1] = 'O'
                        combination[turn2] = 'X'
                        combination[turn3] = 'O'
                        combination[turn4] = 'X'
                        combination[turn5] = 'O'
                        combination[turn6] = 'X'
                        combination[turn1+9]='0'
                        combination[turn2+9]='0'
                        combination[turn3+9]='0'
                        combination[turn4+9]='0'
                        combination[turn5+9]='0'
                        combination[turn6+9]='0'
                        turns.append(combination)

turn7File = open('Turn7.csv','w')
with turn7File:
    writer = csv.writer(turn7File)
    writer.writerows(turns)


#Turn 8:
turns = []
for turn1 in range(0,9):
     for turn2 in range(0,9):
         for turn3 in range(0,9):
             for turn4 in range(0,9):
                 for turn5 in range(0,9):
                     for turn6 in range(0,9):
                         for turn7 in range(0,9):
                            combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
                            if turn1==turn2 or turn1==turn3 or turn2==turn3 or turn1==turn4 or turn2==turn4 or turn3==turn4 or turn1==turn5 or turn1==turn6 or turn2==turn5 or turn2==turn6 or turn3==turn5 or turn3==turn6 or turn4==turn5 or turn4==turn6 or turn5==turn6 or turn1==turn7 or turn2==turn7 or turn3==turn7 or turn4==turn7 or turn5==turn7 or turn6==turn7:
                                continue
                            combination[turn1] = 'O'
                            combination[turn2] = 'X'
                            combination[turn3] = 'O'
                            combination[turn4] = 'X'
                            combination[turn5] = 'O'
                            combination[turn6] = 'X'
                            combination[turn7] = 'O'
                            combination[turn1+9]='0'
                            combination[turn2+9]='0'
                            combination[turn3+9]='0'
                            combination[turn4+9]='0'
                            combination[turn5+9]='0'
                            combination[turn6+9]='0'
                            combination[turn7+9]='0'
                            turns.append(combination)

turn8File = open('Turn8.csv','w')
with turn8File:
    writer = csv.writer(turn8File)
    writer.writerows(turns)


    #Turn 9:
#turns = []
#for turn1 in range(0,9):
#     for turn2 in range(0,9):
#         for turn3 in range(0,9):
#             for turn4 in range(0,9):
#                 for turn5 in range(0,9):
#                     for turn6 in range(0,9):
#                         for turn7 in range(0,9):
#                             for turn8 in range(0,9):
#                                combination = ['-','-','-','-','-','-','-','-','-','1','1','1','1','1','1','1','1','1']
#                                if turn1==turn2 or turn1==turn3 or turn2==turn3 or turn1==turn4 or turn2==turn4 or turn3==turn4 or turn1==turn5 or turn1==turn6 or turn2==turn5 or turn2==turn6 or turn3==turn5 or turn3==turn6 or turn4==turn5 or turn4==turn6 or turn5==turn6 or turn1==turn7 or turn2==turn7 or turn3==turn7 or turn4==turn7 or turn5==turn7 or turn6==turn6 or turn1==turn8 or turn2==turn8 or turn3==turn8 or turn4==turn8 or turn5==turn8 or turn6==turn8 or turn7==turn8:
#                                    continue
#                                combination[turn1] = 'O'
#                                combination[turn2] = 'X'
#                                combination[turn3] = 'O'
#                                combination[turn4] = 'X'
#                                combination[turn5] = 'O'
#                                combination[turn6] = 'X'
#                                combination[turn7] = 'O'
#                                combination[turn8] = 'X'
#                                combination[turn1+9]='0'
#                                combination[turn2+9]='0'
#                                combination[turn3+9]='0'
#                                combination[turn4+9]='0'
#                                combination[turn5+9]='0'
#                                combination[turn6+9]='0'
#                                combination[turn7+9]='0'
#                                combination[turn8+9]='0'
#                                turns.append(combination)
#
#turn9File = open('Turn9.csv','w')
#with turn9File:
#    writer = csv.writer(turn9File)
#    writer.writerows(turns)




