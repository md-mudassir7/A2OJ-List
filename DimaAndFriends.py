
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
cnt=0
if (s+1)%(n+1)!=1:
    cnt+=1
if  (s+2)%(n+1)!=1:
    cnt+=1
if  (s+3)%(n+1)!=1:
    cnt+=1
if  (s+4)%(n+1)!=1:
    cnt+=1
if (s+5)%(n+1)!=1:
    cnt+=1
print(cnt)
    
