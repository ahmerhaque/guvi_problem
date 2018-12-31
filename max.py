
b=int(input())
a=list(map(int,input().split()))
c=sorted(a)
d=c[::-1]
x=sum(d)

if x==0:
    print(x)
else:
    for i in d:
        print(i,end="")
