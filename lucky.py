t=int(input())
while t>0:
        n=int(input())
        nums=input().split()
        val={}
        for i in range(0,n):
                num=int(nums[i])
                if num in val :
                    val[num]+=1
                else:
                    val[num]=1
        m=min(val)
        k=val.get(m,None)
        if k%2==1:
            print("Lucky")
        else:
            print("Unlucky")
        t-=1
