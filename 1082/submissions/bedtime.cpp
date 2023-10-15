#include <bits/stdc++.h>

using namespace std;

int main(){
    char _;
    int h,m,s,h1,m1,s1;
    string am, am1;
    cin >> h >> _ >> m >> _ >> s >> am;
    cin >> h1 >> _ >> m1 >> _ >> s1 >> am1;

    if(am == "pm") h+=12;
    if(am1 == "pm") h1 +=12;
    
    int a = h *60*60 + m*60 + s, a1 = h1*60*60 + m1*60 + s1;
    if(a > a1) a1 += 24*60*60;

    cout << (a1-a) /60 << '\n';
    return 0;
}