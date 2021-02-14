t=int(input())
while t:
    g=int(input())
    ultimatesumchef=0
    ultimatesummorty=0
    while g:
        a,b=list(map(int,input().split()))
        x=a
        y=b
        sumchef=0
        summorty=0
        while(x!=0):
            m=x%10
            if m==0:
                x=int(x/10)
                continue
            else:
                sumchef=sumchef+m
            x=int(x/10)
        while(y!=0):
            n=y%10
            if n==0:
                y=int(y/10)
                continue
            else:
                summorty=summorty+n
            y=int(y/10)
              
        if sumchef<summorty:
           ultimatesummorty=ultimatesummorty+1
        elif sumchef>summorty:
           ultimatesumchef=ultimatesumchef+1
        else:
            ultimatesummorty=ultimatesummorty+1
            ultimatesumchef=ultimatesumchef+1
        g=g-1
    if ultimatesumchef>ultimatesummorty:
        print("0 ",ultimatesumchef)
    elif ultimatesumchef<ultimatesummorty:
         print("1 ",ultimatesummorty)
    else:
        print("2 ",ultimatesummorty)
    t=t-1
