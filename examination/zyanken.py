
import random

num= 0
#while num<100:
#numはとりあえず何回やるか
while num <= 9:
    #rangeは何人でじゃんけんをするか
    for i in range(50):
        boy = random.randint(0, 2)
        if boy == 0:
            boy = "rock:0"
        elif boy == 1:
            boy = "scissors:1"
        elif boy == 2:
            boy = "paper:2"

        # 書き込み
        with open('memo.txt', 'a') as f:
            f.write(boy)
        print(str(i) + "人目:"+boy)




    ld = open("memo.txt")
    lines = ld.readlines()
    ld.close()

    for line in lines:
    #０及グーがない→パーとチョキで決着
        rock = line.find("rock") >0
        scissors = line.find("scissors") >0
        paper = line.find("paper") >0
    if rock == False:
        print("パーとチョキで決着がつきました:　チョキの勝ち")
        result= "end"
    elif scissors == False:
        print("グーとパーで決着がつきました：　パーの勝ち")
        result = "end"
    elif paper ==False:
        print("グーとチョキで決着がつきました：　グーの勝ち")
        result = "end"
    else:
        print('アイコです、やり直してください')
        result = "tie"

    with open('memo.txt', 'w') as f:
        f.write("   ")

    num=num+1
    if result == "end":
        print(str(num) + '回目で決着がつきました。')
        break



