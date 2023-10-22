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

bool dfs(int curr, int to, vector<bool> &vis, vector<set<int>> &G){
	if (curr == to) return 1;
	if (vis[curr]) return 0;
	vis[curr] = true;
	for(auto e:G[curr]){
		if (dfs(e, to, vis, G)) return 1;
	}
	return 0;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m, k;
	cin >> n >> m >> k;

	vector<set<int>> G(n+1);

	vector<int> ans;
	rep(i,0,m){
		int a, b;
		cin >> a >> b;
		G[a].insert(b);
		G[b].insert(a);
	}
	rep(i,0,k){
		int t, a, b;
		cin >> t >> a >> b;
		if (t == 1){
			G[a].insert(b);
			G[b].insert(a);
		} else if (t==2){
			G[a].erase(b);
			G[b].erase(a);
		} else {
			vector<bool> v(n+1, 0);
			ans.push_back(dfs(a, b, v, G));
		}
	}
	for(auto a: ans){
		cout << a << " ";
	}
	cout << endl;
}