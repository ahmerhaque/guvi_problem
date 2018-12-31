l=[]
b=int(input())
a=list(map(int,input().split()))
c=sorted(a)
d=c[::-1]
for i in d:
    print(i,end="")
