

n,m=map(int,input().split())
l=list(map(int,input().split()))
if max(l)<=m:
    print(n)
else:
    res=l[::-1].index(max(l))
    print(n-res)
