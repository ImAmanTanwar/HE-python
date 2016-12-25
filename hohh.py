t=int(input())
while t>0 :
    inp=str(input())
    n=len(inp)
    i=0
    sol=""
    while i<n//2:
        sol+=inp[i]
        i+=2
    print(sol)
    t-=1    
