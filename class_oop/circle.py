"""課題D-1: 円オブジェクト
次のコードが正しく動作するような Circle クラスを実装してください
area は面積、 perimeter は周囲長(=円周の長さ) という意味です。"""

import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    # 円の面積
    def area(self):
        # **:◯乗
        area = self.radius**2 * math.pi
        # 小数点以下の2桁の小数点以下まで表示
        return f'{area:.2f}'

    # 円の外周
    def perimeter(self):
        perimeter = self.radius * 2 * math.pi
        # 小数点以下の2桁の小数点以下まで表示
        return f"{perimeter:.2f}"

"""
# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85"""
