k=int(input())
l1=int(input())
m=int(input())
n=int(input())
d=int(input())
l=[x for x in range(1,d+1)]
l=[x for x in l if x%k!=0]
l=[x for x in l if x%l1!=0]
l=[x for x in l if x%m!=0]
l=[x for x in l if x%n!=0]
print(d-len(l))
