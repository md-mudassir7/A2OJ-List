
n=int(input())
if n%2>0:
    print(-1)
else:
    for i in range(0,n,2):
        print(i+2,i+1,end=" ")
