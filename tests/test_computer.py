import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
from computer import computer_pon

class TestComputerPon(unittest.TestCase):
    def test_computer_pon(self):
        # テスト対象の関数を実行
        result = computer_pon()
        # 出力が指定されたリストのいずれかであることを確認
        self.assertIn(result, ["グー", "チョキ", "パー"])

if __name__ == "__main__":
    unittest.main()