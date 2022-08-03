Geners = 6
att = 2
Fav = 3

table = [[0 for i in range(att)] for j in range(Geners)]
table[0][0]="Action"
table[1][0]="Adventure"
table[2][0]="Comedy"
table[3][0]="History"
table[4][0]="Horror"
table[5][0]="Romance"
# Horror, Romance, Comedy, History , Adventure , Action






def TableMod(genre):
    if genre == "Action":
            table[0][1] =   table[0][1] + 1
    elif genre == "Adventure":
            table[1][1] =   table[1][1] + 1
    elif genre == "Comedy":
            table[2][1] =   table[2][1] + 1
    elif genre == "History":
            table[3][1] =   table[3][1] + 1
    elif genre == "Horror":
            table[4][1] =   table[4][1] + 1
    elif genre == "Romance":
            table[5][1] =   table[5][1] + 1
    #else == ....
                
                
                

def GetInp():
    ppls = int(input())
    for i in range (ppls):
        Name, GA, GB, GC = input().split()
        TableMod(GA)
        TableMod(GB)
        TableMod(GC)
    return 0



def PrintHandler():
    
    
    sorter = lambda x: (-x[1], x[0])
    new = sorted(table, key = sorter)
    
    
    for i in range (Geners):
        print (new[i][0] + " : " + str(new[i][1]))
    return 0;




GetInp()
#print (table)
PrintHandler() 


#-----------------------------------------------------
#Sample Input:
# 4
# hossein Horror Romance Comedy
# mohsen Horror Action Comedy
# mina Adventure Action History
# sajjad Romance History Action

# #Desired Output:
# Action : 3
# Comedy : 2
# History : 2
# Horror : 2
# Romance : 2
# Adventure : 1
#-----------------------------------------------------