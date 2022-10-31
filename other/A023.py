import io
import sys

# input here
_INPUT = """\
11
1 1 1 0 1 1 1 0 1 1 0
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
10
"""

N = int(input())
S = list(map(int, input().split(' ')))

holiday = 0
count = 0
result = 0

for i in range(7):
    if S[i] == 0:
        holiday += 1

if holiday >= 2:
    count = 7

#休日の合計が2日以下なら無条件に0日
for j in range(1, N - 6):
    
    if S[j - 1] == 0:
        holiday -= 1
        
    if S[j + 6] == 0:
        holiday += 1
        
    if(holiday >= 2):
        # count = 7 if count < 7 else count+1
        if count < 7:
            count = 7
        else:
            count += 1
    else:
        # result = count if count > result else result
        if count > result:
            result = count
        else:
            result
        
        count = 0

# result = count if count > result else result
if count > result:
    result = count
else:
    result

print(result)