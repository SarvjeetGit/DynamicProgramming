n=int(input())
arr=[int(x) for x in input().split()]
if(sum(arr)%2!=0):
    print(False)
else:
    k=sum(arr)//2
    dp=[[0 for j in range(k+1)] for i in range (n+1)]
    for i in range (n+1):
        for j in range (k+1):
            if(j==0):
                dp[i][j]=False
            if(i==0):
                dp[i][j]=True
    for i in range (1,n+1):
        for j in range (1,k+1):
            if arr[i-1]<=k :
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            elif arr[i-1]>k :
                dp[i][j]=dp[i-1][j]
    print(dp[n][k])
