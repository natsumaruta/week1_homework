"""課題D-3: 正方形オブジェクト
次のコードが正しく動作するような Square クラスを実装してください
diagonal は 対角線(の長さ) という意味です。"""

import math


class Square:

    def __init__(self, side):
        self.side = side

    # 面積
    def area(self):
        area = self.side**2
        # 今回は整数の場合は小数点を返していないのでroundでfloat型にする
        return round(area, 2)

    # 対角線(の長さ)
    def diagonal(self):
        # 1辺×2の平方根
        diagonal = self.side * math.sqrt(2)
        return round(diagonal, 2)


"""
square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21"""
