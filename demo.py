
t=int(input())
r=0
while r!=t:
    p=[]
    failed=True
    n=int(input())
    summ=0
    counter=0
    maincounter=0
    p=[int(p) for p in input().split()]
    for i in range(0,len(p),1):
       x=p[i]
       for j in range(0,len(p),1):
           if(j==i):
               continue
           else:
               summ=x+p[j]
               print(summ)
               if(summ%3!=0):
                   failed=False
                   break
                   
                   
                
       
    if(failed==False):
        print("Yes")
    else:
        print("No")
        
    r=r+1
