import io
import sys

# input here
_INPUT = """\
4
1 2
2 3
5 7
8 15
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
11
"""

# ------------ your code here ---------------

N = int(input())

days =[]
for i in range(N):
    a = list(map(int, input().split()))
    days.append(a)

begin_working_days = []
finish_working_days = []
for working_days in days:
    begin_working_days.append(working_days[0])
    finish_working_days.append(working_days[1])
begin_working_days.append(0)
finish_working_days.append(0)
print(begin_working_days)
print(finish_working_days)

result = 0
for i in range(N):
    if finish_working_days[i] <= begin_working_days[i + 1] + 1 and begin_working_days[i + 1] != 0:
        result = finish_working_days[i + 1] - begin_working_days[i] + 1

print(result)