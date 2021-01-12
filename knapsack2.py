#solving basic 0/1 knapsack problem using memoization

wt=[int (i) for i in input().split()]
val=[int (i) for i in input().split()]
limit=int(input())
dp=[[-1 for i in range(limit+1)] for j in range(len(wt)+1)] 

def maxProfit(wt,val,n,lim):
    if(n==0 or lim==0):
        return 0
    if (dp[n][lim]!=-1):
        return dp[n][lim]
    if (wt[n-1]<=lim):
        dp[n][lim] = max(val[n-1]+maxProfit(wt,val,n-1,lim-wt[n-1]),maxProfit(wt,val,n-1,lim))
        return dp[n][lim]
    elif (wt[n-1]>lim):
        dp[n][lim] = maxProfit(wt,val,n-1,lim)
        return dp[n][lim]

res=maxProfit(wt,val,len(wt),limit)
print(res)