def miniMaxSum(arr):
    # Write your code here
    minSum = 0
    maxSum = 0
    arr.sort()
    for i in range(0,4,1):
        minSum = minSum + arr[i]
    for i in range(1,5,1):
        maxSum = maxSum + arr[i]
    print(minSum, maxSum)