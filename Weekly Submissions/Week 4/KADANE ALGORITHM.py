KADANE ALGORITHM:

Initialize:
    max_so_far = INT_MIN
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
  (c) if(max_ending_here < 0)
            max_ending_here = 0
return max_so_far

CODE: 

def maximumSubarraySum(arr):
       n = len(arr)
       maxSum = -1e8
       currSum = 0

       for i in range(0, n):
           currSum = currSum + arr[i]
           if(currSum > maxSum):
               maxSum = currSum
           if(currSum < 0):
               currSum = 0
      
       return maxSum

if __name__ == "__main__":
    # Your code goes here
    print(maximumSubarraySum([1, 3, 8, -2, 6, -8, 5]));