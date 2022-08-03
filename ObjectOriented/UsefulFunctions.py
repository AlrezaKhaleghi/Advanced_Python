
a = [(2,3) , (4,5) , (0,3) , (8,9) , (0,99)]
a.sort(key = lambda x: x[1])
print (a)


# map(function, list)
# list(map(function, list))
# the output is not the list and we should convert it to the list by list (----)

numbers = [ 10, 8, 0, 2, 5, 4, 13, 9]
x = map (lambda x: x * 2 , numbers)
print (x)
print (list (x))



# advanced IF with Lambda
# applying lambda finction with if to the list:
y = map (lambda x: 'big' if x>5 else 'small' , numbers)
print (list(y))



# filter
# list(filter(func, list)) 
# the filter works for us if function value equals true! (x % 2 == 0)

filtered = list(filter(lambda x: x % 2 == 0, numbers))
print (filtered)




# yield function 

def Counter(n):
    current = 0
    while (current <= n):
        yield current
        current += 1


for i in Counter (250):
    print (i)

