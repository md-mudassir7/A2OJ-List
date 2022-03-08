s=input()
res=''
i=0
for j in range(len(s)):
    if i>=len(s):
        break
    if s[i]=='.':
        res+='0'
        i+=1
        continue
    elif s[i]=='-' and s[i+1]=='.':
        res+='1'
        i+=2
        continue
    elif s[i]=='-' and s[i+1]=='-':
        res+='2'
        i+=2
        continue
print(res)
