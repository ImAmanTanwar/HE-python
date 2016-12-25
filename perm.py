t=int(input())
val=[0] * 100000
val[0]=1
val[1]=1
for i in range(2,100000):
    num=((i+1)//2)*2
    val[i]=val[i-1]+num
while t>0:
    inp=int(input())
    print(val[inp-1])
    t-=1
