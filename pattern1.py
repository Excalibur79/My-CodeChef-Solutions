k = 3
l = 1
m = 3
for i in range(1, 4, 1):
    if i == 2:
        l = 0
        g = 0
    if i == 3:
        l = 1
        g = 1
    for j in range(1, i+1, 1):
        print("*", end="")
    while k >= i:
        print(" ", end="")
        k = k - 1
    k = 2
    while l <= i:
        print("*", end="")
        l = l + 1
    while m >= i:
        print(" ", end="")
        m = m - 1
    m = 2
    for g in range(1, i+1, 1):
        print("*", end="")
    print("")
