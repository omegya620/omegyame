import random

z = ('グー','チョキ','パー')
b = random.choice(z)
a = input('じゃんけん!(グー、チョキ、パーのどれかで答えてね。)')
print(f'相手は{b}を出した!')

if b == a:
    print('＊あいこ＊')
elif (b == 'グー' and a == 'パー') or (b == 'チョキ' and a == 'グー') or (b == 'パー' and a == 'チョキ'):
    print('＊勝ち！＊')
else:
    print('＊負け、、、＊')
