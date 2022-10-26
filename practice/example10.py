import io
import sys

# input here
_INPUT = """\
3 6
......
.#.#..
......
"""
sys.stdin = io.StringIO(_INPUT)

# ------------ your code here ---------------

# 0:下、1:右、2:上、3:左、4:右下、5:右上、6左上、7:左下
DX = [1,0,-1,0,1,-1,-1,1]
DY = [0,1,0,-1,1,1,-1-1]

# 入力
H,W = map(int,input().split())
S = [input() for i in range(H)]

# 答えを表すには二次元配列を用意する('.'のところは0とする)
result = [[0 if v == '.' else '#' for v in row] for row in S]

# 各マス(i,j)を順に処理
for i in range(H):
    for j in range(W):
        # 飽きます以外はそsのままにする
        if S[i][j] != '.':
            continue
        
        # 周囲8マスの'#'の個数を数える
        for dx ,dy in zip(DX,DY):
            ni,nj = i + dx, j + dy
            
            # マス(i.j)が盤面外の場合はスキップ
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue
            
            # #であれば増やす
            if S[ni][nj] =='#':
                result[i][j] += 1

# 出力形式に合わえて出力
for row in result:
    print(*row, sep='')
