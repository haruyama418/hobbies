# -*- coding: utf-8 -*-
word= ["apple","banana"]


i=0
while i<3:
    
    get_word = input("Any help? Expand your vocabulary:")
             
    judge = get_word in word
    if judge == True: 
       print("Again?  the meaning is ")

    elif judge == False: 
        print("new word! Adding to list. wait a sec...")
        word.append(get_word)
        #print(word)
        ja = input("what's the meaning?")
        with open('word_note.txt', 'a') as f:
          print(get_word+"   :   "+ja, file=f)
          print("------------------------" ,file=f)
          


        #with open('word_note.txt') as f:
         # print(f.readlines())
        print("process succeeded! keep going!")
         
print("nice")
