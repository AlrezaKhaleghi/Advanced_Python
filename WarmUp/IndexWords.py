Passage = input().split(". ")
print (Passage)

none = False 
Counter = 0



for i in  Passage:
 
    Sentence = i.split(" ")
    i=0
    size=len(Sentence)

    for i in range(size):
        word = Sentence[i]
        Counter = Counter + 1
        # print (word)
        # print (word[0])
        # print (word[0].isupper())
        # if word[0].isupper() == True:
        #     print ("yeessss")
     
        if word[0].isupper() == True and i != 0:
            none = True 
            if word [:-1] == "." :
                 print(str(Counter) + ":" + word[0:-1])
            else : 
                 print(str(Counter) + ":" + word)

        

          

if none == False:
    print ("None")







# The Persian League is the largest sport event dedicated to 
# the deprived areas of Iran. The Persian League promotes peace 
# and friendship. This video was captured by one of our heroes 
# who wishes peace.


# 2:Persian
# 3:League
# 15:Iran
# 17:Persian
# 18:League