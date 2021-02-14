t=int(input())
counter=0
i=0
j=0
while t:
    n=int(input())
    arr=[]
    learningobdata=[]
    for i in range(n):
        str=input()
        arr.append(str)
    for j in range(n-1,-1,-1):
        flag=0
        c=0
        for i in range(n-1,-1,-1):
            if arr[i][j]=='#':
                learningobdata.append(i)
                c=i
                continue
            elif i<c:
                continue
            elif i in learningobdata:
                continue
            else:
                counter=counter+1
    print(counter)
    counter=0
    t=t-1
                
                
                
            
                
