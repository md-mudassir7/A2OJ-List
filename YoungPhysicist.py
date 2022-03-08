n=int(input())
s1,s2,s3=0,0,0
for _ in range(n):
    x,y,f=map(int,input().split())
    s1+=x
    s2+=y
    s3+=f

if s1==0 and s2==0 and s3==0:
    print('YES')
else:
    print('NO')
