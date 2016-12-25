n=int(input())
nums=input().split()
mul=1
for i in range(0,n):
    mul=(mul*int(nums[i]))%1000000007
print(mul)
