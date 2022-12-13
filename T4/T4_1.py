# dict = {1: ["2-4" , "6-8"]}
# In how many assignment pairs does one range fully contain the other



def readInput():
    #sec_ids={}
    sec_ids = []
    sec = 0
    with open("input4.txt") as f:
        for i in f:
            a = i.replace("\n", "").split(",")
            
            #sec_ids[sec] = a
            sec_ids.append(a)
            sec += 1
            #print(sec_ids)
        #print(len(sec_ids))
        return(sec_ids)

def part1(file):
    cant = 0
    
    for i in file:
        #print(i)

        # For with each number in the pairs ex: 2-4 = 2,3,4 AND 6-8 = 6,7,8
        first_p = ""
        #print(i[0].split("-"),i[0][2])
        for j in range(int(i[0].split("-")[0]), int(i[0].split("-")[1] )+ 1):
            first_p += str(j) + "-"
        
        arrayF = first_p.split("-")
        arrayF.pop()
        
        second_p = ""
        for k in range(int(i[1].split("-")[0]), int(i[1].split("-")[1]) + 1):
            second_p += str(k) + "-"
        
        arrayS = second_p.split("-")
        arrayS.pop()

        
        print("--------\n",arrayF,"\n",arrayS)
        print(len(arrayF), len(arrayS))
        
        if (len(arrayF) <= len(arrayS)):
            if((arrayS[0] <= arrayF[0])  and (arrayF[len(arrayF) - 1] <= arrayS[len(arrayS) - 1])):
                print((arrayS[0] <= arrayF[0])  and (arrayF[len(arrayF) - 1] <= arrayS[len(arrayS) - 1]))
                cant += 1
        else:
            if((arrayF[0] <= arrayS[0] )  and (arrayS[len(arrayS) - 1] <= arrayF[len(arrayF) - 1])):
                print((arrayF[0] <= arrayS[0] )  and (arrayS[len(arrayS) - 1] <= arrayF[len(arrayF) - 1]))
                cant += 1
            
        ''' 546
        break
        if (len(arrayF) <= len(arrayS)):
            if (arrayS.find(arrayF[0]) != -1 and arrayS.find(arrayF[len(arrayF) - 2]) != -1):
                
                #print (second_p.find(first_p[0]) != -1 and second_p.find(first_p[len(first_p) - 1]) != -1)
                cant +=1
            #else:
                #print(second_p.find(first_p[0]) != -1 and second_p.find(first_p[len(first_p) - 1]) != -1)
        
        else:
            if (arrayF.find(arrayS[0]) != -1 and arrayF.find(arrayS[len(arrayS) - 2]) != -1):
                #print(first_p.find(second_p[0]) != -1 and first_p.find(first_p[len(second_p) - 1]) != -1)
                cant +=1
            #else:
                #print(first_p.find(second_p[0]) != -1 and first_p.find(first_p[len(second_p) - 1]) != -1)
        '''
    return cant

    #  pair1_1 = i[0][0]
    #  pair1_2 = i[0][2]

    #  pair2_1 = i[0][0]
    #  pair2_2 = i[0][2]


def main():
    contain = readInput()
    #print(len(contain))
    print(part1(contain))


main()


