temp=0
arr=[]
n=int(input("Enter the number of elements-"))
print("Enter the elements\n")
for i in range(n):
    arr.append(int(input()))
max=arr[0]
for j in range(1,n,1):
    if arr[j]>max:
        temp=max
        max=arr[j]
print("The second maximum number is:",temp)

