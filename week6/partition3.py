# Uses python3
import sys
import itertools
K=3
def isKPartitionPossibleRec(arr, subsetSum, taken,  
                            subset, K, N, curIdx, limitIdx): 
    if subsetSum[curIdx] == subset: 
          
        """ current index (K - 2) represents (K - 1)  
        subsets of equal sum last partition will  
        already remain with sum 'subset'"""
        if (curIdx == K - 2): 
            return True
          
        # recursive call for next subsetition  
        return isKPartitionPossibleRec(arr, subsetSum, taken,  
                                       subset, K, N, curIdx + 1 , N - 1) 
      
    # start from limitIdx and include  
    # elements into current partition  
    for i in range(limitIdx, -1, -1): 
          
        # if already taken, continue  
        if (taken[i]): 
            continue
        tmp = subsetSum[curIdx] + arr[i]  
          
        # if temp is less than subset, then only  
        # include the element and call recursively  
        if (tmp <= subset): 
              
            # mark the element and include into  
            # current partition sum  
            taken[i] = True
            subsetSum[curIdx] += arr[i]  
            nxt = isKPartitionPossibleRec(arr, subsetSum, taken,  
                                          subset, K, N, curIdx, i - 1) 
                                            
            # after recursive call unmark the element and  
            # remove from subsetition sum  
            taken[i] = False
            subsetSum[curIdx] -= arr[i]  
            if (nxt): 
                return True
    return False
  
# Method returns True if arr can be  
# partitioned into K subsets with equal sum  
def partition3(arr):
    global K
    N=len(arr) 
      
    # If K is 1, 
    # then complete array will be our answer  
    if (K == 1): 
        return True
      
    # If total number of partitions are more than N,  
    # then division is not possible  
    if (N < K): 
        return False
          
    # if array sum is not divisible by K then  
    # we can't divide array into K partitions  
    sum = 0
    for i in range(N): 
        sum += arr[i]  
    if (sum % K != 0): 
        return False
      
    # the sum of each subset should be subset (= sum / K)  
    subset = sum // K  
    subsetSum = [0] * K  
    taken = [0] * N 
      
    # Initialize sum of each subset from 0  
    for i in range(K): 
        subsetSum[i] = 0
          
    # mark all elements as not taken  
    for i in range(N): 
        taken[i] = False
          
    # initialize first subsubset sum as   
    # last element of array and mark that as taken  
    subsetSum[0] = arr[N - 1]  
    taken[N - 1] = True
      
    # call recursive method to check  
    # K-substitution condition  
    return isKPartitionPossibleRec(arr, subsetSum, taken,  
                                   subset, K, N, 0, N - 1) 

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    if partition3(A):
        print(1)
    else:
        print(0)

