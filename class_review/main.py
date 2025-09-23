from customer import Customer

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# C-1. フルネームを取得できる
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力
print(michelle.full_name())

# C-2. 年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力
print(michelle.age)

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
# C-5. 3歳以下の入場料金の無料化
# C-6. 75歳以上の料金区分の追加
"""料金の計算ルール
未満児料金(3歳未満):0円
こども料金(20歳未満): 1000円
おとな料金(20歳以上65歳未満): 1500円
シニア料金(65歳以上): 1200円
後期高齢者料金(75歳以上):500円"""
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 500 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,500" という値を出力
print(michelle.info_csv())

# C-7. 単一顧客の情報取得形式の追加その1
print(ken.info_csv_c7())  # "Ken Tanaka      15      1000" という値を出力
print(tom.info_csv_c7())
print(ieyasu.info_csv_c7())
print(michelle.info_csv_c7())

# C-8. 単一顧客の情報取得形式の追加その2
print(ken.info_csv_c8())  # "Ken Tanaka|15|1000" という値を出力
print(tom.info_csv_c8())
print(ieyasu.info_csv_c8())
print(michelle.info_csv_c8())
