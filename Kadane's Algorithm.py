import sys
def maxSubarraySum(arr, n) :
    if n == 0:
        return 0
    maxi = -sys.maxsize-1 
    s = 0
    for i in range(n):
        s += arr[i]
        if s > maxi:
            maxi = s
        if s < 0:
            s = 0
    return max(maxi,s)

    
