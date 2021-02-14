t=int(input())
while t:
    N,M=list(map(int,input().split()))
    P=[]
    p=[int(p) for p in input().split()]
    counter=p[0]
    a=0
    flag=-1
    p.sort()
    for i in p:
       if counter!=i:
           a=counter
           flag=0
           break
           
       counter=counter+1
    if a==M:
        print(len(p))
    else:
        print("-1")
        
    t=t-1
