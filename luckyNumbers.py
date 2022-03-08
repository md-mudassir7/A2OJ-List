def lucky(n):
    s=str(n)
    if s.count('7')==len(s)-s.count('4'):
        return True
    return False
n=int(input())
s=str(n)
cnt=0
for i in s:
    if i=='4' or i=='7':
        cnt+=1
if lucky(cnt):
    print('YES')
else:
    print('NO')
