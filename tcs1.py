t=int(input())
while t:
    n=int(input())
    p=[]
    sum=0
    i=2
    counter=0
    x=0
    for j in range(n,0,-1):
        
        
        for i in range(1,j+1,1):
            sum=sum+i
           
            if i not in p:
              p.append(i)
            if(sum>=n):
             break
        sum=0
        n=p[len(p)-1]
        
    print(p)
    t=t-1    
	
