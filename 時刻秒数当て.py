from datetime import datetime

k = 0

while True:
    ｚ = int(input('今何秒？'))
    k +=1
    a = datetime.now().second

    if z == a:
        print(f'正解!答えは{a}でした。回答数{k}回。')
        break
    elif z > a:
        print('まだ小さいよ。')
    elif z < a:
        print('まだ大きいよ。')