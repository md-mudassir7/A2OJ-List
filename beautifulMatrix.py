mat=[]
for i in range(5):
    mat.append(list(map(int,input().split())))
    if 1 in mat[i]:
        l=[i,mat[i].index(1)]
print(abs(l[0]-2)+abs(l[1]-2))
    
