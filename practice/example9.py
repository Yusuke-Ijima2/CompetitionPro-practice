import io
import sys

# input here
_INPUT = """\
2
2
2
100
"""
sys.stdin = io.StringIO(_INPUT)

# ------------ your code here ---------------

A = int(input())
B = int(input())
C = int(input())
X = int(input())

result = 0

# 全探索
for i in range(0, A + 1):
    for j in range(0, B + 1):
        for k in range(0, C + 1):
            # あくまでここはi,j,kですべて探索できると考える
            
            # 合計金額がX円に一致したら1増やす
            if 500 * i + 100 * j + 50 * k == X:
                result += 1

print(result)