
import random

num= 0
#while num<100:
#numはとりあえず何回やるか
while num <= 9:
    #rangeは何人でじゃんけんをするか
    for i in range(10):
        boy = random.randint(0, 2)
        if boy == 0:
            boy = "グー"
        elif boy == 1:
            boy = "チョキ"
        elif boy == 2:
            boy = "パー"

        # 書き込み
        with open('memo.txt', 'a') as f:
            f.write(boy)
        print(str(i) + "人目:"+boy)




    ld = open("memo.txt")
    lines = ld.readlines()
    ld.close()

    for line in lines:
    #０及グーがない→パーとチョキで決着
        rock = line.find("グー") >0
        scissors = line.find("チョキ") >0
        paper = line.find("パー") >0
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
        print('結果はアイコです、やり直してください')
        result = "tie"

    with open('memo.txt', 'w') as f:
        f.write("   ")

    num=num+1
    if result == "end":
        print(str(num) + '回目で決着がつきました。')
        break



