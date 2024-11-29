# computer_hand:'グー', 'チョキ', 'パー'
# player_hand:'グー', 'チョキ', 'パー'

#戻り値："player_win","computer_win","draw"
def judge(computer_hand, player_hand):

   if player_hand == computer_hand:
       print("あいこ")
       return 'draw'
   elif (player_hand == 'グー' and computer_hand == 'チョキ') or \
           (player_hand == 'チョキ' and computer_hand == 'パー') or \
           (player_hand == 'パー' and computer_hand == 'グー'):
       print("あなたの勝ち！")
       return 'player_win'
   else:
       print("あなたの負け...")
       return 'computer_win'