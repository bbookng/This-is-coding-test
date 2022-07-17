N, M = map(int, input().split())

result = 0
for i in range(N):
    row = list(map(int, input().split()))
    row_min = min(row)
    result = max(result, row_min)

print(result)