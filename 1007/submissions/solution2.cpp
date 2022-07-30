#include <bits/stdc++.h>
using namespace std;
// incomplete
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef complex<double> cd;

int main() {
	int n, q, a, b;
    char s[12];
    char c;
    
    scanf("%d%d", &n, &q);
    
    vector<string> VS(n+7, "white");

    while(q--){
        scanf(" %c", &c);
        if (c == 'q') {
            scanf("%d", &a);
            string ans = VS[a];
            printf("%s\n",ans.c_str());
        } else {
            scanf("%d%d %s", &a, &b, s);
            string S(s);
            rep(i,a,b+1){
                VS[i] = S;
            }
        }
    }
}