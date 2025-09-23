"""A-8: リストを要素に持つリスト
users_info を使って次のような出力をしてください"""

users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]


for user_info in users_info:
    user = user_info
    print(f"Name: {user_info[0]}, Age: {user_info[1]}")
