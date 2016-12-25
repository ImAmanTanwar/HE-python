t=int(input())
while t>0:
    alp=[13] * 26
    inp=input()
    l=len(inp)
    val=""
    for i in range(0,l):
       val+=str(chr((ord(inp[i])+alp[ord(inp[i])-97]-97)%26+97))
       alp[ord(inp[i])-97]+=1%26
    print(val)
    t-=1
