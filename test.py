import sys
n,k = map(int,sys.stdin.readline().rstrip().split())
lst = [[0]*(n+1) for _ in range(k+1)]

for i in range(n+1):
    lst[1][i] = 1


for i in range(1,k+1):
    for j in range(n+1):
        for l in range(0,j+1):
            lst[i][j] += lst[i-1][j-l]
            lst[i][j] %= 1000000000

print(lst)
print(lst[k][n]%1000000000)
