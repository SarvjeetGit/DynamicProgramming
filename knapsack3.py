#solving basic 0/1 knapsack problem using top down approach

wt=[int (i) for i in input().split()]
val=[int (i) for i in input().split()]
limit=int(input())
n=len(wt)
dp=[[-1 for i in range(limit+1)] for j in range(len(wt)+1)]

for i in range (n+1):
    for j in range (limit+1):
        if i==0 or j==0:
            dp[i][j]=0

for i in range (1,n+1):
    for j in range (1,limit+1):
        if (wt[i-1]<=j):
            dp[i][j]=max((val[i-1]+dp[i-1][j-wt[i-1]]),dp[i-1][j])
        elif(wt[i-1]>j):
            dp[i][j]=dp[i-1][j]
print(dp[n][limit])
