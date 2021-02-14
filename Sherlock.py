t=int(input())
counter=0
i=0
j=0
r=0
while r!=t:
    flag=0
    n=int(input())
    arr=[]
    obstruction=[]
    temp=[]
    for i in range(n):        
        str=input()
        arr.append(str)
        
    for j in range(n-1,-1,-1):
        flag=0
        for i in range(n-1,-1,-1):
            for x in range(n-1,i-1,-1):
                if arr[x][j]=='#':
                    flag=-1
                    break
                if x==i:
                    for y in range(j,n,1):
                        if arr[x][y]=='#':
                            flag=-1
                            break
                if flag==-1:
                    break
            if flag==0:
                counter=counter+1
            flag=0
    print(counter)
    counter=0
    r=r+1
    
    
    
