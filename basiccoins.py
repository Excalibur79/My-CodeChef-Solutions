x=int(input("Enter value- "))

n=int(input("Enter  number of denomination values to be used-"))
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)-1,-1,-1):
       a=(int)(x/arr[i])
       print("",a,arr[i])
       x=(int)(x%arr[i])
    
