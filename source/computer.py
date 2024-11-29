import random
#戻り値："グー","チョキ","パー"
def computer_pon():
   #リストにじゃんけんの手を格納
   hands=["グー","チョキ","パー"]
   computer_hand = random.choice(hands)
   return computer_hand