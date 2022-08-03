
rows = int (input())
vocabs = []
translated = ""

def get_inp ():
    for i in range (rows):
        row = input().split(" ")
        vocabs.append(row)
    
    inp_sentence = str(input())
    return inp_sentence




def build_out(word):
    global translated
    translated =  translated + word + " "

    return 0




def translator (text):
    flag = False

    for i in range (rows):

        if text in vocabs [i]:
            peer = vocabs[i][0]
            Flag = True
            build_out(peer)
            return 0

    if flag == False :
            build_out(text)





def main ():
    
    input_sen = get_inp()
    words = input_sen.split(" ")
    length = len(words)


    for i in range (length):
        translator(words[i])

    print (translated)





main()
