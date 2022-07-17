n = int(input())
i, j = 1, 1
plans = input().split()

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            ni = i + di[i]
            nj = j + dj[i]
    if ni < 1 or nj < 1 or ni > n or nj > n:
        continue
    i, j = ni, nj

print(i, j)