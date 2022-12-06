def main():
    with open("Task1_AOC_input.txt") as f:
        #print(f.read())

        sumCal, highCal1, highCal2, highCal3 = 0, 0, 0, 0
        elfNum, highElf1, highElf2, highElf3 = 1, 1, 1, 1

        
        for i in f:

            #print(i)

            if (i == "\n"):
                print("elf calories " + str(elfNum) + ": " + str(sumCal))
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
        
        print("-------------------FINAL RESULTS-------------\n"+
                    "1st Highest Cal elf " + str(highElf1) + ": " + str(highCal1) + "\n" +
                  
                
                    "-----------------------------------------------")



main()