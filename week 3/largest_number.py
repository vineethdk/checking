#Uses python3

import sys

"""def largest_number(a):
    #write your code here
    n=len(str(max(list(map(int,a)))))
    per=[]
    for i in range(1,n+1):
        temp=[]
        for j in a:
            if(i==len(list(j))):
                temp.append(j)
        #print(temp)
        temp.sort(reverse=True)
        per.extend(temp)
    res = ""
    for x in per:
        res += x
    return res"""

def largest_number(array): 
      
    extval, ans = [], "" 
      
    # calculating the length of largest number 
    # from given and add 1 for further operation 
    l = len(str(max(array))) + 1
      
    # iterate given values and  
    # calculating extended values 
    for i in array: 
        temp = str(i) * l 
          
        # make tuple of extended value and  
        # equivalant original value then  
        # append to list 
        extval.append((temp[:l:], i)) 
      
    # sort extval in descending order 
    extval.sort(reverse = True) 
      
    # iterate extended values 
    for i in extval: 
          
        # concatinate original value equivalant 
        # to extended value into ans variable 
        ans += str(i[1]) 
          
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = list(map(int,data[1:]))
    print(largest_number(a))
    
