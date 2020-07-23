# Uses python3
import sys

def get_change(m):
    #write your code here
    mnc=[0]*(m+1)
    for i in range(1,m+1):
        mnc[i]=10000
        for j in [1,3,4]:
            if i>=j:
                temp=mnc[i-j]+1
                if(temp<mnc[i]):
                    mnc[i]=temp
    return(mnc[m])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
