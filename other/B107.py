import io
import sys

# input here
_INPUT = """\
10 3 3
"""
sys.stdin = io.StringIO(_INPUT)

# output here
_OUTPUT = """\
7
8
9
4
5
6
1
2
3
"""

# ・カードの枚数を表す整数 N、
# 1 セットあたりの枚数を表す整数 M、
# シャッフルの回数を表す整数 K がこの順に半角スペース区切りで与えられます。
# ------------ your code here ---------------

N,M,K = list(map(int, input().split()))

def arrdef(arr):
    #配列の要素数をカウント
    length = len(arr)
    #開始位置を指定
    n = 0
    #分割する変数の個数を指定
    s = M
    #配列を指定した個数で分割していくループ処理
    arr1 = []
    arr2 = []
    for i in arr:
        arr1.append(arr[n:n+s:1])
        # print(arr[n:n+s:1])
        n += s
     
        #カウント数が配列の長さを超えたらループ終了
        if n >= length:
            break
        
    
    arr1 = list(reversed(arr1))
    arr2 = sum(arr1, [])
    return arr2


arr = []
for i in range(N):
    arr.append(i + 1)

for i in range(K):
    arr = arrdef(arr)

for a in arr:
    print(a)