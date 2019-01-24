a=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(0,len(b),1):
    if b[i]==i:
        l.append(i)
print(*sorted(l))
