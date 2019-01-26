x,y=map(int,input().split())
a=list(map(int,input().split()))

b=sorted(a)
print(b)
c=b[::-1]

print(c[y-1])
