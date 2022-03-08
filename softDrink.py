

n,k,l,c,d,p,nl,np=map(int,input().split())
res=min(k*l//nl,c*d,p/np)
print(int(res//n))
