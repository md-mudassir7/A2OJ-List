


a = [[0, 0, 0, 0, 0]]
for i in range(3):
    a.append([0]+list(map(int, input().split()))+[0])
a.append([0, 0, 0, 0, 0])
for i in range(1,4):
    for j in range(1,4):
        print((a[i][j]+a[i-1][j]+a[i+1][j]+a[i][j-1]+a[i][j+1]+1)%2, end='')
    print()
