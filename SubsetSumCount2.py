#solving subset sum count using top down approach

n,k=input().split()
n=int(n)
k=int(k)
arr=[int(x) for x in input().split()]
dp=[[0 for j in range(k+1)] for i in range (n+1)]
for i in range (n+1):
    for j in range (k+1):
        if(i==0):
            dp[i][j]=0
        if(j==0):
            dp[i][j]=1
for i in range(1,n+1):
    for j in range (1,k+1):
        if(arr[i-1]<=j):
            dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][k])
