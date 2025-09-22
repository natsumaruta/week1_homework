"""A-10: サイコロ
下記のコードが期待通り動作するような、dice() 関数を実装してください ※ dice()関数は1から6の整数をランダムに返す"""

import random


def dice():
    result = random.randint(1, 6)
    return result


print(dice())
