#include <iostream>
#include <vector>
using namespace std;
using std::cin;
using std::cout;
using std::vector;
using std::max;
int n = 0;

int compute_min_refills(int milesAway,int fulltank, vector<int> Stops) { 
    int numRefills = 0;
    int currentRefill = 0;
    int lastRefill = 0;
    
    if ((Stops[currentRefill] + fulltank) >= milesAway) {
        return numRefills+1;
    }

    while (currentRefill < n) {
        lastRefill = currentRefill; 
        while ( ( currentRefill < n ) && ( (Stops[currentRefill + 1] - Stops[lastRefill]) <= fulltank ) )
        {
            currentRefill = currentRefill + 1;
        }
        
        if (currentRefill == lastRefill)
        {
            return -1;
        }
        numRefills = numRefills + 1;
        
        if ((Stops[currentRefill] + fulltank) >= milesAway)
        {
            return numRefills+1;
        }
    }
    return -1;  
}

int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}
