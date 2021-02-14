t = int(input())
counter = 0
flag = 0
x = 0
l = 0
g = 0
while x != t:
    counter = 0
    N, k, b = list(map(int, input().split()))
    p = []
    p = [int(p) for p in input().split()]
    del p[N:len(p)]
    while (True):
        p.sort()
        flag = N - 2
        i=len(p)-1
        while(i>0)and(flag>=0):
            l = k * p[flag] + b
            if l <= p[i]:
                counter = counter + 1
                g=-1
                i = flag + 1
            elif l > p[i]:
                if i!=1:
                   i = i + 1
                else:
                    break
            flag = flag - 1
            i=i-1
        if g==-1:
            print(counter+1)
        else:
            print(counter)
        break

    x = x + 1
