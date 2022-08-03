# author: Alireza Khaleghi (alrezakhaleghi@gmail.com)
# this program is for Maktabkhoone advanced python course
# ---


team= 4
att = 6
table = [[0 for i in range(att)] for j in range(team)]
table[0][0]="Iran"
table[1][0]="Morocco"
table[2][0]="portugal"
table[3][0]="Spain"
# Nation, wins, loses, draws, goal difference, points


def TableMod(TA, TB, GA, GB):
    
    if GA == GB:
        table[TA][3] = table[TA][3] + 1
        table[TB][3] = table[TB][3] + 1
        table[TA][5] = table[TA][5] + 1
        table[TB][5] = table[TB][5] + 1
    elif GA > GB:
        diff = GA - GB 
        table[TA][1] = table[TA][1] + 1
        table[TB][2] = table[TB][2] + 1
        table[TA][4] = table[TA][4] + diff
        table[TB][4] = table[TB][4] - diff
        table[TA][5] = table[TA][5] + 3
    #GA < GB    
    else :
        diff = GB - GA 
        table[TB][1] = table[TB][1] + 1
        table[TA][2] = table[TA][2] + 1
        table[TB][4] = table[TB][4] + diff
        table[TA][4] = table[TA][4] - diff
        table[TB][5] = table[TB][5] + 3

    return 0
    
    


def InputHandler(lines):
    
    #0 ="Iran"
    #1 ="Morocco"
    #2 ="portugal"
    #3 ="Spain"
    for i in range (lines):
        A, B = input().split("-")
        GA = int(A)
        GB = int(B)

        if i == 0:
            TableMod(0, 3, GA, GB)     
        elif i == 1:
            TableMod(0, 2, GA, GB)
        elif i == 2:
            TableMod(0, 1, GA, GB)
        elif i == 3:
            TableMod(3, 2, GA, GB)
        elif i == 4:
            TableMod(3, 1, GA, GB)
        elif i == 5:
            TableMod(2, 1, GA, GB) 
        #else == ....
        
    return 0
        
        
def OutputHandler ():
    max_point = 0
    max_win = 0
    
    for i in range (0,4):
        
        if table[i][2] > max_win:
            max_win = table[i][2]
            
        if table[i][5] > max_point:
            max_point = table[i][5]
   
        
        
def PrintHandler(arr, rows):
    for i in range (rows):
        print (arr[i][0] + "  wins:" + str(arr[i][1]) + " , " + "loses:" + str(arr[i][2]) + " , " + "draws:" + str(arr[i][3]) + " , " + "goal difference:" + str(arr[i][4]) + " , " + "points:" + str(arr[i][5]))
        # Nation, wins, loses, draws, goal difference, points
    return 0




InputHandler(6)
#table.sort(reverse = True)
#print(table)
sorter = lambda x: (-x[5], -x[1], x[0])
new = sorted(table, key = sorter)
#print(new)
PrintHandler(new, 4)








#-----------------------------------------------------
#Sample Input:
# 2-2
# 2-1
# 1-2
# 2-2
# 3-1
# 2-1

# Desired Output:
# Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
# Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
# Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
# Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3
#-----------------------------------------------------
