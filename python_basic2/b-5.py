"""課題B-5:基本統計量の計算
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
合計値
最大値
最小値
平均値
ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
1つの統計量につき、それ専用の関数を実装すること"""

input_value = input("データを入力してください(スペース区切り) > ")
# list():リスト化
# map(関数, リスト) :リストの要素を順番に関数に通す
# (int,〜()):整数に変換
# value.split():前後の余計なもの（スペーズなど）を削除
input_value_list = list(map(int, input_value.split()))


# 合計値 計算式
def calculate_sum(value_list):
    sum_value = 0
    for d in value_list:
        sum_value += d
    return sum_value


# 最大値 計算式
def calculate_max(value_list):
    max_value = value_list[0]
    for d in value_list:
        if max_value <= d:
            max_value = d
    return max_value


# 最小値 計算式
def calculate_min(value_list):
    # mix_valueに０を代入してしまうと常に０が最小値になってしまうので注意。
    mix_value = value_list[0]
    for d in value_list:
        if mix_value >= d:
            mix_value = d
    return mix_value


# 平均値 計算式
def calculate_average(value_list):
    sum_value = calculate_sum(value_list)
    count_value = len(value_list)
    average_value = sum_value / count_value
    return average_value


# f"{}\n"：改行
print(
    f"合計値{calculate_sum(input_value_list)}\n"
    f"最大値{calculate_max(input_value_list)}\n"
    f"最小値{calculate_min(input_value_list)}\n"
    f"平均値{calculate_average(input_value_list)}"
)
