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
int N;
vi a;
vector<pii> batch;
// FRONT OF ARROW, BACK OF ARROW
void make_batch(int rep, int step){
	batch.clear();
	int n_to_flip = 1 << (rep);
	int skip = 1 << (step);
	int dir = 0;
	int i = 0;
	int n = 0;
	int k = 0;
	while(i != N){
		if (dir) {
			batch.push_back({i, i+skip});
		} else {
			batch.push_back({i+skip, i});
		}
		i++;
		n++;
		k++;
		if (n == n_to_flip) {
			dir = !dir;
			n = 0;
		}
		if (k == skip) {
			i += skip;
			k = 0;
		}
	}
}
bool set_batch(){
	int k = 0;
	for(auto [i, j] : batch){
		if (a[i] < n && a[j] < n) k++;
	}
	cout << "q " << k << endl;
	for(auto [i, j] : batch){
		if (a[i] < n && a[j] < n) {
			cout << a[i] << " < " << a[j] << endl;
		}
	}
	vi res(k);
	cin >> res[0];
	if (res[0] == -1) {
		return 0;
	}
	rep(i,1,k) cin >> res[i];
	int p = 0;
	for(auto [i, j] : batch){
		int r;
		if (a[i] < n && a[j] < n) {
			r = res[p++];
		} else if (a[i] >= n && a[j] < n){
			r = 0;
		} else if (a[i] < n && a[j] >= n){
			r = 1;
		} else {
			r = a[i] < a[j];
		}
		if (r) {
			swap(a[i], a[j]);
		}
	}
	return 1;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	// int n, m;
	cin >> n >> m;
	N = 1;
	int reps = 0;
	while(N < n){
		N <<= 1;
		reps++;
	}
	a.resize(N, 0);
	iota(all(a), 0);
	rep(i,0,reps){
		for(int j=i; j>=0; --j){
			make_batch(i, j);
			if (!set_batch()) {
				return 0;
			}
		}
	}
	cout << "a";
	rep(i,0,n) cout << " " << a[i];
	cout << endl;

}