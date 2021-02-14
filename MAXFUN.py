t=int(input())
while t:
    n=int(input())
    p=[int(p) for p in input().split()]
    p.sort()
    print( abs(p[0]-p[n-2]) + abs( p[n-2]-p[n-1] )  + abs(p[n-1]-p[0]) )
    t-=1
