import io
import sys

# input here
_INPUT = """\
3
8 12 40
"""
sys.stdin = io.StringIO(_INPUT)

# ------------ your code here ---------------

#整数numが2で何回割れるか
def how_many_times(num):
    counter = 0
    while num % 2 == 0:
        num //= 2
        counter += 1
    return counter

N = int(input())
A = list(map(int, input().split()))

# Aの要素にhow_many_timesを適用して、最小値を取る
# map(1,2)で2の配列全てに1を適用していくという意味
# min()でその配列の中で一番小さい値を摘出する
result = min(map(how_many_times,A))

print(result)
