n,m=list(map(int,input().split()))
a=[int(p) for p in input().split()]
b=a
while m:
    x,d=list(map(str,input().split()))
    d=int(d)
    if x=="R":
        print(b)


    elif x=="C":
      for i in range(n-1,-1,-1):
          g=i-d
          if g>=0:
              b[g]=a[i]
          else:
              
              b[n+g]=a[i]

    elif x=="A":
        while d:
            temp=a[n-1]
            for i in range(n-2,-1,-1):
                a[i+1]=a[i]
            a[0]=temp
            d=d-1
        
    
    m=m-1
