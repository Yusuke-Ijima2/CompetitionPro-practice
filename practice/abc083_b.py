import io
import sys

# input here
_INPUT = """\
20 2 5
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
84
"""

# ------------ your code here ---------------

# 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

def calc_sum_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

N,A,B = list(map(int, input().split()))

result = 0

for i in range(1, N+1): # 1以上N以下
    if A <= calc_sum_digits(i) <= B:
        result += i # 各行の合計

print(result)