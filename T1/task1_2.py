from collections import Counter
def main():
    with open("Task1_AOC_input.txt") as f:
        #print(f.read())

        sumCal, highCal1, highCal2, highCal3 = 0, 0, 0, 0
        elfNum, highElf1, highElf2, highElf3 = 1, 1, 1, 1

        elfArray = []
        calDic = {}
        
        
        for i in f:

            #print(i)

            if (i == "\n"):
                print("elf calories " + str(elfNum) + ": " + str(sumCal))

                #elfArray.push(elfNum)
                calDic[elfNum] = sumCal

                if (sumCal > highCal1):
                    
                    highCal1 = sumCal
                    highElf1 = elfNum

                    print("--------------------------------\n"+
                    "1st Highest Cal elf " + str(highElf1) + ": " + str(highCal1) + "\n" +
                    "-----------------------------------------------")
                sumCal = 0
                elfNum += 1
            
            else:
                sumCal += int(i) 
        
        #a = dict(sorted(calDic.items(), key=lambda item: item[1]))
        #print(a)

        k = Counter(calDic)
        highElfs = k.most_common(3)
        print("Dictionary with 3 highest values:")
        print("Keys: Values")
        
        for i in highElfs:
            print(i[0]," :",i[1]," ")
        
        print("-------------------FINAL RESULTS-------------\n"+
                    "1st Highest Cal elf " + str(highElfs[0][0]) + ": " + str(highElfs[0][1]) + "\n" +
                    "2nd Highest Cal elf " + str(highElfs[1][0]) + ": " + str(highElfs[1][1]) + "\n" +
                    "3rd Highest Cal elf " + str(highElfs[2][0]) + ": " + str(highElfs[2][1]) + "\n" +
                    "Total calories: ", highElfs[0][1]+highElfs[1][1]+highElfs[2][1], "\n"
                
                    "-----------------------------------------------")



main()