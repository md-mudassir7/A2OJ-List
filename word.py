s=input()
cnt=0
for i in range(len(s)):
    if s[i].islower():
        cnt+=1
if cnt>=len(s)-cnt:
    print(s.lower())
else:
    print(s.upper())
