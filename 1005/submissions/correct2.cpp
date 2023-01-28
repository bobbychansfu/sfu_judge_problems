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

int n, m;
bool p = false;
void do_rep(vi &a){
	vector<pair<int, int>> qs;
	int nq = (n-p)/2;
	cout << "q " << nq << endl;
	if (!p) {
		for(int i=0; i<n-1; i+=2){
			qs.push_back({i, i+1});
			cout << a[i] << " < " << a[i+1] << endl;
		}
	} else {
		for(int i=1; i<n-1; i+=2){
			qs.push_back({i, i+1});
			cout << a[i] << " < " << a[i+1] << endl;
		}
	}
	rep(i,0,nq){
		int b;
		cin >> b;
		if (b == 0) {
			swap(a[qs[i].first], a[qs[i].second]);
		}
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	// int n, m;
	cin >> n >> m;
	vi a(n);
	iota(all(a), 0);
	rep(i, 0, m-1){
		do_rep(a);
		p = !p;
	}
	cout << "a";
	rep(i,0,n){
		cout << " " << a[i];
	}
	cout << endl;
}