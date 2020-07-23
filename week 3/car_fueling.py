"""# python3
import sys

count=0
def compute_min_refills(distance, tank, stops):
    global count
    #print(max(stops),tank,count)
    if(distance-stops[-1]>tank):
        return(-1)
    if tank>max(stops) and tank>=distance and distance-stops[-1]<tank:
        return(count)
    if tank>max(stops) and tank<distance:
        return(count+1)
    if stops[1]-stops[0]>tank:
        return(-1)
    maxi=0
    f=0
    for i in stops:
        if(maxi<i and tank>=i):
            maxi=i
            f=stops.index(maxi)
    count=count+1
    for i in range(f,len(stops)):
        stops[i]=stops[i]-maxi
    #print(stops)
    #print(f)
    return(compute_min_refills(distance-maxi, tank, stops[f:]))"""
import sys

def compute_min_refills(d, dist_with_full_tank, stops):
    num_refills = 0
    current_refills = 0
    last_refills = 0
    while current_refills <= d:
        last_refills = current_refills
        while (stops[current_refills + 1] - stops[last_refills]) <= dist_with_full_tank:
                current_refills = current_refills + 1
                if current_refills == (d - 1):
                    break
        if current_refills == last_refills:
            return (-1)
        if current_refills < (d - 1):
            num_refills = num_refills + 1
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    
    print(compute_min_refills(d, m, stops))
