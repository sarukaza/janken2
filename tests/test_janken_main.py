import unittest
import sys
import os
from unittest.mock import patch

# 'source'ディレクトリをPythonパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
import player
import computer
import janken_judge

def main():
    player_win = 0
    computer_win = 0

    """3回戦のじゃんけんゲームを行う関数"""
    round = 1
    while round <= 3:
        print(f"-----ラウンド {round} -----")
        computer_hand = computer.computer_pon()
        player_hand = player.player_pon()
        result = janken_judge.judge(computer_hand, player_hand)

        print(f"あなたの手:{player_hand}")
        print(f"コンピューターの手:{computer_hand}")

        print("")  
        if result == 'draw':
            print("あいこです！ 再度対決！")    
        else:
            round += 1 
            if result == 'player_win':
                player_win += 1
                print("あなたの勝ちです！")
            else:
                computer_win += 1
                print("コンピューターの勝ちです！")            
        print("")

    print("【最終結果】")
    print(f"あなた:{player_win}勝")
    print(f"コンピュータ:{computer_win}勝")
    if player_win >= computer_win:
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です！")

if __name__ == '__main__':
    main()

class TestJanken(unittest.TestCase):

    @patch('player.player_pon', side_effect=['グー', 'チョキ', 'パー'])
    @patch('computer.computer_pon', side_effect=['チョキ', 'パー', 'グー'])
    @patch('janken_judge.judge', side_effect=['player_win', 'player_win', 'player_win'])
    def test_main_player_wins_all(self, mock_judge, mock_computer_pon, mock_player_pon):
        with patch('builtins.print') as mocked_print:
            main()
            expected_calls = [
                unittest.mock.call('-----ラウンド 1 -----'),
                unittest.mock.call('あなたの手:グー'),
                unittest.mock.call('コンピューターの手:チョキ'),
                unittest.mock.call(''),
                unittest.mock.call('あなたの勝ちです！'),
                unittest.mock.call(''),
                unittest.mock.call('-----ラウンド 2 -----'),
                unittest.mock.call('あなたの手:チョキ'),
                unittest.mock.call('コンピューターの手:パー'),
                unittest.mock.call(''),
                unittest.mock.call('あなたの勝ちです！'),
                unittest.mock.call(''),
                unittest.mock.call('-----ラウンド 3 -----'),
                unittest.mock.call('あなたの手:パー'),
                unittest.mock.call('コンピューターの手:グー'),
                unittest.mock.call(''),
                unittest.mock.call('あなたの勝ちです！'),
                unittest.mock.call(''),
                unittest.mock.call('【最終結果】'),
                unittest.mock.call('あなた:3勝'),
                unittest.mock.call('コンピュータ:0勝'),
                unittest.mock.call('あなたの総合勝利です！')
            ]
            mocked_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()
