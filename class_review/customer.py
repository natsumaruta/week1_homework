class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # C-1. フルネームを取得できる
    # print(ken.full_name())  # "Ken Tanaka" という値を出力

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    # C-2. 年齢という概念の追加
    # print(ken.age)  # 15 という値を出力

    def age(self):
        return self.age

    # C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
    # C-5. 3歳以下の入場料金の無料化
    # C-6. 75歳以上の料金区分の追加
    """料金の計算ルール
       未満児料金(3歳未満):0円
       こども料金(20歳未満): 1000円
       おとな料金(20歳以上65歳未満): 1500円
       シニア料金(65歳以上): 1200円
       後期高齢者料金(75歳以上):500円"""
    # print(ken.entry_fee())  # 1000 という値を出力

    def entry_fee(self):
        if self.age >= 75:  # 後期高齢者料金(75歳以上):500円
            return 500
        elif self.age >= 65:  # シニア料金(65歳以上) 1200円
            return 1200
        elif self.age >= 20:  # おとな料金(20歳以上65歳未満): 1500円
            return 1500
        elif self.age >= 4:  # こども料金(20歳未満)
            return 1000
        else:  # 未満児料金(3歳未満):0円
            return 0

    # C-4. 単一の顧客情報をCSV形式で取得できる
    # print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力

    def info_csv(self):
        full_name = self.full_name()
        age = self.age
        entry_fee = self.entry_fee()
        return f"{full_name},{age},{entry_fee}"

    # C-7. 単一顧客の情報取得形式の追加その1
    # print(ken.info_csv())  # "Ken Tanaka      15      1000" という値を出力

    def info_csv_c7(self):
        full_name = self.full_name()
        age = self.age
        entry_fee = self.entry_fee()
        return f"{full_name:<16}{age:<8}{entry_fee}"

    # C-8. 単一顧客の情報取得形式の追加その2
    # print(ken.info_csv())  # "Ken Tanaka|15|1000" という値を出力

    def info_csv_c8(self):
        full_name = self.full_name()
        age = self.age
        entry_fee = self.entry_fee()
        return f"{full_name}|{age}|{entry_fee}"

    pass
