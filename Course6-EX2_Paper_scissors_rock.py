print("================")
print("1.請輸入 '石頭', '剪刀' ,'布' 中的任意一個")
print("2.輸入end結束遊戲!")
print("================")

import random
name=input("請輸入你的名字:")
print("歡迎%s猜拳"%name)

com=0
per=0
draw=0
while True:
        #電腦隨機出拳
        s=int(random.randint(1,3))
        if(s==1):
                computer="剪刀"
        elif(s==2):
                computer="石頭"
        else:
                computer="布"

        #玩家出拳
        person=input("請出拳:")

        #判斷玩家與電腦出拳結果
        person_list=["石頭","剪刀","布"]
        if(person in person_list) and (person != "end"):
                if(computer == person):
                        print("電腦出拳：",computer)
                        print ("平手了")
                        draw+=1
                        # continue
                elif(computer=="石頭" and person=="剪刀") or (computer=="剪刀" and person=="布") or (computer=="布" and person=="石頭"):
                        print("電腦出拳： ", computer)
                        print ("電腦贏了")
                        com+=1
                else:
                        print("電腦出拳：", computer)
                        print ("%s贏了" % name)
                        per+=1
        #處理輸入不相干且非為end之答案
        elif(person not in person_list) and (person != "end"):
                print ("拜託！我只會判斷 剪刀 石頭 布，別為難我!")
                continue
                
        #輸入end，結束遊戲並統計
        else:
                sum = com + per + draw
                print ("這次遊戲，%s共猜拳%d次,贏拳%d次,輸拳%d次,平手%d次" %(name,sum,per,com,draw))
                print ("歡迎%s下次再玩!" % name)
                break