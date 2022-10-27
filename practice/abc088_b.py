import io
import sys

# input here
_INPUT = """\
2
3 1
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
2
"""

# ------------ your code here ---------------
# N 枚のカードがあります. i 枚目のカードには, aiという数が書かれています.
# Alice と Bob は, これらのカードを使ってゲームを行います. ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. Alice が先にカードを取ります.
# 2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.

N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

Alice = 0
Bob = 0
for i in range(N):
    if i % 2 ==0:
        Alice += a[i]
    else:
        Bob += a[i]

print(Alice - Bob)