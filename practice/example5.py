import io
import sys

# input here
_INPUT = """\
14 2 4
"""
sys.stdin = io.StringIO(_INPUT)

# ------------ your code here ---------------

# 整数nの各行の和を求める関数
def calc_sum_digits(n):
    sum_digits = 0
    # 4649だとすると464あまり9,46あまり4...という風にあまりが足される
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

# 入力
N,A,B = map(int, input().split())

# 答えを格納する変数
result = 0

# 1以上N以下の整数iを調べる
for i in range(1, N + 1):
	if A <= calc_sum_digits(i) <= B:
		result += i

print(result)