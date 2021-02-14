t=int(input())

while t:
    p=[]
    n=int(input())
    sum=0
    p=[int(p) for p in input().split()]
    for i in range(1,n,1):
       if p[i-1]<p[i]:     
          a=p[i-1]
          b=p[i]
       else:
           b=p[i-1]
           a=p[i]
       sum=sum+b-a-1
    print(sum)
