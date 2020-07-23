# Uses python3
import sys
def get_change(m):
    global count
    if m==5 or m==1 or m==10:
        return(count+1)
    elif m>1 and m<5:
        count=get_change(m-1)+1
        return(count)
    elif m>5 and m<10:
        count=get_change(m-5)+1
        return(count)
    elif m>10:
        count=get_change(m-10)+1
        return(count)
    
    return count

count=0

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
