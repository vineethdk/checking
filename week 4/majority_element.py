import sys

def get_majority_element(a, left, right):
    a.sort()
    max=0
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    for i in a:
        if(isMajority(a, n, i)):
            return(1)
    return -1



def isMajority(arr, n, x): 
      
    # Find the index of first occurrence of x in arr[] */ 
    i = _binarySearch(arr, 0, n-1, x) 
  
    # If element is not present at all, return false*/ 
    if i == -1: 
        return False
  
    # check if the element is present more than n / 2 times */ 
    if ((i + n//2) <= (n -1)) and arr[i + n//2] == x: 
        return True
    else: 
        return False
  
 
def _binarySearch(arr, low, high, x): 
    if high >= low: 
        mid = (low + high)//2 # low + (high - low)//2; 
  
        ''' Check if arr[mid] is the first occurrence of x. 
            arr[mid] is first occurrence if x is one of the following 
            is true: 
            (i) mid == 0 and arr[mid] == x 
            (ii) arr[mid-1] < x and arr[mid] == x'''
          
        if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x): 
            return mid 
        elif x > arr[mid]: 
            return _binarySearch(arr, (mid + 1), high, x) 
        else: 
            return _binarySearch(arr, low, (mid -1), x) 
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
