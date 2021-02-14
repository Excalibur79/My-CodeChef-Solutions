t=int(input())
while t:
    N,B,M=list(map(int,input().split()))
    counter=0
    if type(N/B) is float:
        N=N+B
    p=[]
    load=-1
    
    p=[int(p) for p in input().split()]
    for i in p:
        for j in range(0,N-B+1,B):
            
            if i>=j and i<=j+B-1:
            
                if load!=j:
                    counter=counter+1
                    load=j
                    break
                else:
                    break
                    
         
            
                
        
    print(counter)
        
            

    
    t=t-1

