inp=input().split()
n=int(inp[0])
q=int(inp[1])
nums=input().split()
while q>0:
    query=input().split()
    if query[0]=='1':
        nums[int(query[1])-1]=str((int(nums[int(query[1])-1])+1)%2)
    else:
        ind=int(query[2])
        if nums[ind-1]=='1':
            print("ODD")
        else:
            print("EVEN")
    q-=1
