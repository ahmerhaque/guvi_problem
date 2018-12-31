a=sorted(list(map(int,input().split())))
l=[]
for i in range (0,len(a)-1,1):
    if a[i]==a[i+1]:
        l.append(a[i])
    else:
        continue
print(*list(set(l)))
