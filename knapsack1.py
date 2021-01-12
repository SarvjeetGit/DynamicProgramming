# solving basic 0/1 knapsack problem using recursion

wt=[int (i) for i in input().split()]
val=[int (i) for i in input().split()]
limit=int(input())

def maxProfit(wt,val,n,lim):
    if(n==0 or lim==0):
        return 0
    if (wt[n-1]<=lim):
        return max(val[n-1]+maxProfit(wt,val,n-1,lim-wt[n-1]),maxProfit(wt,val,n-1,lim))
    elif (wt[n-1]>lim):
        return maxProfit(wt,val,n-1,lim)

res=maxProfit(wt,val,len(wt),limit)
print(res)