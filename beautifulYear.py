def fun(s):
    if s.count(s[0])==1 and s.count(s[1])==1 and s.count(s[2])==1 and s.count(s[3])==1:
        return True
    return False
n=int(input())+1
while len(set(str(n)))<4:
    n+=1
print(n)
