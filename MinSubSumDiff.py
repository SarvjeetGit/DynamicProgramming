import sys
arr=[int(x) for x in input().split()]
n=len(arr)
k=sum(arr)
dp=[[0 for j in range (k+1)] for i in range (n+1)]
for i in range(n+1):
    for j in range(k+1):
        if (i==0):
            dp[i][j]=False
        if(j==0):
            dp[i][j]=True

for i in range(1,n+1):
    for j in range(1,k+1):
        if(arr[i-1]<=j):
            dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
        elif(arr[i-1]>j):
            dp[i][j]=dp[i-1][j]
mn=sys.maxsize
for j in range (1,k//2):
    if(dp[n][j]==True):
        val=k-2*j
        mn=min(mn,val)

print(mn)