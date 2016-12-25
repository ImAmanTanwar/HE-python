n=int(input())
inp=input().split()
s=[0]*3
for i in range(0,n):
    s[i%3]+=int(inp[i])
print(str(s[0])+" "+str(s[1])+" "+str(s[2]))
