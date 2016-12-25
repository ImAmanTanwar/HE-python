t=int(input())
while t>0:
    inp=input()
    val=""
    l=len(inp)
    for i in range(0,l):
        val+=str(chr(((ord(inp[i])-96+ord(inp[l-i-1])-96)%26)+96))
    print(val)
    t-=1
