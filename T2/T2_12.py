with open('T2_input2.txt') as f:
    lines = f.readlines()
    f.close()
    
# A for Rock, 
# B for Paper, and
# C for Scissors.

oponent1 = {"A": 1, "B":2, "C":3}

# X for Rock, 
# Y for Paper, and 
# Z for Scissors.

my_choice1 = {"X": 1, "Y":2, "Z":3}

# A X = 3 + 1 | A Y = 6 + 2 | A Z = 0 + 3
# B X = 0 + 1 | B Y = 3 + 2 | B Z = 6 + 3
# C X = 6 + 1 | C Y = 0 + 2 | C Z = 3 + 3

#(1 for Rock, 2 for Paper, and 3 for Scissors)
win = 0

for i in lines:
    if((oponent1[i[0]] < my_choice1[i[2]]) or (oponent1[i[0]] == 3 and my_choice1[i[2]] == 1)):
        if(not (oponent1[i[0]] == 1 and my_choice1[i[2]] == 3)):
            win += 6 + my_choice1[i[2]]
            print("win")
            #print(win)
            #print(i)
        else:
            win += 0 + my_choice1[i[2]]
    else:
        if(oponent1[i[0]] == my_choice1[i[2]]):
            win += 3 + my_choice1[i[2]]
            print("draw")
        else:
            win += 0 + my_choice1[i[2]]
            print("lose")
    
print(win)