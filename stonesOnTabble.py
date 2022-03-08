#1
n=int(input())
s=input()
cnt=0
l=[s[0]]
for i in range(1,n):
    if s[i]!=l[-1]:
        l.append(s[i])
print(n-len(l))

#2
n=int(input())
s=input()
print(sum(a==b for a,b in zip(s[1:],s)))
