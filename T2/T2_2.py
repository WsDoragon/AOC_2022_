with open('T2_input2.txt') as f:
    lines = f.readlines()
    f.close()

# X need to lose, 
# Y need to end in a draw 
# Z need to win.

# A for Rock, 
# B for Paper, and
# C for Scissors.

# A X = 0 + 3 | A Y = 3 + 1 | A Z = 6 + 2
# B X = 0 + 1 | B Y = 3 + 2 | B Z = 6 + 3
# C X = 0 + 2 | C Y = 3 + 3 | C Z = 6 + 1

oponent = {"A": 1, "B":2, "C":3}

points = 0

for i in lines:
    if (i[2] == "X"):
        if(i[0] == "A"):
            points += 3
        else:
            points += oponent[i[0]] - 1
            print("lose against", i[0])
            print(points)
    if (i[2] == "Y"):
        points += oponent[i[0]] + 3
    
    if (i[2] == "Z"):
        if(i[0] == "C"):
            points += 1 + 6
        else:
            points += oponent[i[0]] + 6 + 1


print("Final points:", points)