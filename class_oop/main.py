from circle import Circle
from rectangle import Rectangle
from square import Square
from mycounterv1 import MyCounterV1
from mycounterv2 import MyCounterV2
from mycounterv3 import MyCounterV3

# 半径1の円
circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 18.85

# 高さ５×幅６の長方形
rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

# 高さ３×幅３の長方形
rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24

# １辺が1.5の長方形
square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

# １辺が15の長方形
square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21


# d-4
counter1 = MyCounterV1(value=0)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV1(value=7)
print(counter2.value)  # 7

counter2.count_up()
print(counter2.value)  # 8

counter2.count_up()
print(counter2.value)  # 9


# d-5
counter1 = MyCounterV2(value=0, step=1)
print(counter1.value)  # 0

counter1.count_up()
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 2

counter2 = MyCounterV2(value=0, step=3)
print(counter2.value)  # 0

counter2.count_up()
print(counter2.value)  # 3

counter2.count_up()
print(counter2.value)  # 6


# d-6
counter1 = MyCounterV3(value=1, step=2)
print(counter1.value)  # 1

counter1.count_up()
print(counter1.value)  # 3

counter1.count_up()
print(counter1.value)  # 5

counter1.count_down()
print(counter1.value)  # 3

counter2 = MyCounterV3(value=3, step=4)
print(counter2.value)  # 3

counter2.count_down()
print(counter2.value)  # -1

counter2.count_down()
print(counter2.value)  # -5
