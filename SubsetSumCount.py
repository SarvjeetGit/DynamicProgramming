#solving subset sum count using recursion

n,k=input().split()
n=int(n)
k=int(k)
arr=[int(x) for x in input().split()]
c=0
def count(arr,n,k):
    if k==0:
        return 1
    elif k!=0 and n==0:
        return 0

    if arr[n-1]<=k:
        return count(arr,n-1,k)+count(arr,n-1,k-arr[n-1])
    elif arr[n-1]>k:
        return count(arr,n-1,k)

c=count(arr,n,k)
print(c)