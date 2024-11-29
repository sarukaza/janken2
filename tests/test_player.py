import unittest
from unittest.mock import patch

def player_pon():
    hands_dic = {'1':"グー", '2':"チョキ", '3':"パー"}
    print("1.グー 2.チョキ 3.パー")
    player_hand = input("グー、チョキ、パーのいずれかを入力してください：")
    while player_hand not in hands_dic.keys():
        print("不正な入力です。もう一度入力してください。")
        player_hand = input("グー、チョキ、パーのいずれかを入力してください：")
    
    return hands_dic[str(player_hand)]

class TestPlayerPon(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_player_pon_gu(self, mock_input):
        self.assertEqual(player_pon(), "グー")

    @patch('builtins.input', side_effect=['2'])
    def test_player_pon_choki(self, mock_input):
        self.assertEqual(player_pon(), "チョキ")

    @patch('builtins.input', side_effect=['3'])
    def test_player_pon_pa(self, mock_input):
        self.assertEqual(player_pon(), "パー")

    @patch('builtins.input', side_effect=['4', '1'])
    def test_player_pon_invalid_then_valid(self, mock_input):
        self.assertEqual(player_pon(), "グー")

if __name__ == "__main__":
    unittest.main()