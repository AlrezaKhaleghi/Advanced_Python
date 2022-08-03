


def GetInp():
    lines = int (input())
    table = [[0 for i in range(3)] for j in range(lines)]
    for i in range (lines):
        S, N, L = input().split(".")
        table[i][0] = S
        table[i][1] = N
        table[i][2] = L
    
    #print (table)
    return table




def DataManipulation(data):
    sorter = lambda x: (x[0], x[1])
    new = sorted(data, key = sorter)
    size = len(new)
    for i in range  (size):
        name = new[i][1]
        new[i][1] = name.capitalize()
        #print (new[i][1])
   
    return new



def PrintHandler(table):
    size = len(table)
    for i in range (size):
        OutLine = (str(table [i][0]) + " " + str(table [i][1]) + " " + str(table [i][2]))
        print (OutLine)



def main():
    Intrm = GetInp()
    table = DataManipulation (Intrm)
    PrintHandler (table)


main()








#-----------------------------------------------------
#Sample Input:
# 4
# m.hosSein.python
# f.miNa.C
# m.aHMad.C++
# f.Sara.java

# f Mina C
# f Sara java
# m Ahmad C++
# m Hossein python
#-----------------------------------------------------
