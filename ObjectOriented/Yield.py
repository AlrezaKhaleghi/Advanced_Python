# yield



def GenNum(number):
    i = 0
    while i <= number:
        yield i 
        i += 1



# yield is suitable for loops and iteration!

for i in GenNum(10000):
    print (i)

