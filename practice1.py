n=int(input("Enter the size of the array-"))
a=[]
counter=0
for i in range(n):
    a.append(int(input()))
for i in a:
    if i%2==0:
        counter=counter+1
print("In the array ",a," number of even numbers are",counter)
