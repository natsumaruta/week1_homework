"""課題D-6: カウンターその3
次のコードが正しく動作するような MyCounterV3 クラスを実装してください"""

from mycounterv2 import MyCounterV2


# MyCounterV2のクラスを継承する
class MyCounterV3(MyCounterV2):
    def __init__(self, value, step):
        # 継承元の__init__メソッドを呼び出す
        super().__init__(value, step)

    def count_down(self):
        self.value -= self.step
        return self.value


"""counter1 = MyCounterV3(value=1, step=2)
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
"""
