"""課題B-4: 天気情報の分析
要件
3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
このデータを使って3つの問を満たす実装をしてください
"""


def main():

    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]
    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    # 気温の合計という変数に0を代入
    sum_temperature = 0
    # 気温の合計を計算
    for spot in weather_information:
        sum_temperature += spot["temperature"]
    # 駅の数
    station_count = len(weather_information)
    # 平均の計算式
    print(sum_temperature / station_count)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # 大阪府の駅のみの空リスト作成
    oosaka_stations = []

    # weather_informatioでprefectureが"大阪府"の場合のみ、駅名をoosaka_stationsリストに追加
    for spot in weather_information:
        if spot["prefecture"] == "大阪府":
            oosaka_stations.append(spot["station"])

    # カンマ区切りにして表示
    print(",".join(oosaka_stations))

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    sum_temperature_hukuoka = 0
    station_count_hukuoka = 0

    for spot in weather_information:
        # weather_informatioでprefectureが"福岡県"の場合
        if spot["prefecture"] == "福岡県":
            # 福岡県の気温合計に１駅分プラス
            sum_temperature_hukuoka += spot["temperature"]
            # 福岡県の駅数に１プラス
            station_count_hukuoka += 1
    # 福岡県の平均気温を表示
    print(sum_temperature_hukuoka / station_count_hukuoka)


if __name__ == "__main__":
    main()
