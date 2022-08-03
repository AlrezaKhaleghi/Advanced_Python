def IsPrime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range (2, num):
            if num % i == 0:
                #print (i)
                return False
        else:
            return True


def PrimeNumbers(num):
    PrNums = []
    if num == 2:
        PrNums.append(2)
    elif  num > 2 :
        for i in range (2, num+1):
            if ( IsPrime(i)):
                PrNums.append(i)

    return PrNums

    
def PrimeFactors(num):
    PrFacts = []
    for n in PrimeNumbers(num):
        if (num % n == 0):
            PrFacts.append(n)

    return PrFacts    


def InpGet(linesnum):
    Inps = []

    for i in range (linesnum):
        InputNum = input ("")
        Inps.append(int(InputNum))

    return Inps


def Main(lines):
    numbers = [] 
    numbers = InpGet(lines)
    max = 0
    index = 0

    for i in range (lines):
        #print(numbers)
        #print(i)
        x = len (PrimeFactors(numbers[i]))

        if x >=  max :
        
            if x > max:
                max = x 
                index = i
                
            elif x == max:
                if numbers[index] < numbers [i]:
                    index = i



    print(numbers[index], max)
    return max




#print (PrimeNumbers(1026))
#print (PrimeFactors(1026))


print (Main(10))









#-----------------------------------------------------
# Sample Input:
# 123
# 43
# 54
# 12
# 76
# 84
# 98
# 678
# 543
# 231

#Desired Output:
#678 3
#-----------------------------------------------------