"""課題D-2: 長方形オブジェクト
次のコードが正しく動作するような Rectangle クラスを実装してください
diagonal は 対角線(の長さ) という意味です。
"""

import math


# 長方形
class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 面積
    def area(self):
        area = self.height * self.width
        # 小数点以下の2桁の小数点以下まで表示
        # round(area, 2)にしていたが、整数の場合小数点以下が出ないので文字列フォーマットに変更
        return f"{area:.2f}"

    # 対角線(の長さ)
    def diagonal(self):
        # sqrt:平方根を返す
        diagonal = math.sqrt(self.height**2 + self.width**2)
        return f"{diagonal:.2f}"


"""rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24"""
