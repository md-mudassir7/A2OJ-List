
n=int(input())
d={a:i+1 for i,a in enumerate(map(int,input().split()))}
m=int(input())
x=sum(d[i] for i in map(int,input().split()))
print(x,(n+1)*m-x)
