n,k=input().split()
n=int(n)
k=int(k)
arr=[int(i) for i in input().split()]

dp=[[0 for i in range(k+1)] for j in range (n+1)]

for i in range (n+1):
    for j in range(k+1):
        if i==0:
            dp[i][j]=False
        if j==0:
            dp[i][j]=True
for i in range (1,n+1):
    for j in range(1,k+1):
        if(arr[i-1]<=j):
            dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
        elif(arr[i-1]>j):
            dp[i][j]=dp[i-1][j]
print(dp[n][k])
