#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vector<vector<vi>> st;

struct Tree1 {
	typedef int T;
	static constexpr T unit = INT_MIN;
	T f(T a, T b) { return max(a, b); } // (any associative fn)
	vector<T> s; int n;
	Tree1(int n = 0, T def = unit) : s(2*n, def), n(n) {}
	void update(int pos, T val) {
		for (s[pos += n] = val; pos /= 2;)
			s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
	}
	T query(int b, int e) { // query [b, e)
		T ra = unit, rb = unit;
		for (b += n, e += n; b < e; b /= 2, e /= 2) {
			if (b % 2) ra = f(ra, s[b++]);
			if (e % 2) rb = f(s[--e], rb);
		}
		return f(ra, rb);
	}
};

struct Tree2 {
	typedef int T;
	static constexpr T unit = INT_MAX;
	T f(T a, T b) { return min(a, b); } // (any associative fn)
	vector<T> s; int n;
	Tree2(int n = 0, T def = unit) : s(2*n, def), n(n) {}
	void update(int pos, T val) {
		for (s[pos += n] = val; pos /= 2;)
			s[pos] = f(s[pos * 2], s[pos * 2 + 1]);
	}
	T query(int b, int e) { // query [b, e)
		T ra = unit, rb = unit;
		for (b += n, e += n; b < e; b /= 2, e /= 2) {
			if (b % 2) ra = f(ra, s[b++]);
			if (e % 2) rb = f(s[--e], rb);
		}
		return f(ra, rb);
	}
};
int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	vi nums(n);
	for(auto &x : nums) cin >> x;

	Tree1 maxTree(n);
	Tree2 minTree(n);

	rep(i, 0, n) {
		maxTree.update(i, nums[i]);
		minTree.update(i, nums[i]);
	}
	

	
	auto query = [&](int l, int r) {
		return maxTree.query(l, r + 1) - minTree.query(l, r + 1);
	};
	constexpr int INF = 1e9+7;
	vector<vi> dp(n, vi(k, INF));
	rep(i, 0, n) dp[i][0] = query(0, i);

	// vector<vi> par(n, vi(k, -1));
	rep(i, 1, n) {	
		rep(j, 1, k) {	
			rep(L, j-1, i) {
				// min cost of k-partition at i is
				// min ..L { cost of k-1 partition at L + cost for (L, i] }
				if (dp[L][j-1] + query(L+1, i) < dp[i][j]) {
					dp[i][j] = dp[L][j-1] + query(L+1, i);
					// par[i][j]=L;
				}		
			}
		}
	}

	// rep(i, 0, n) {
	// 	 rep(j, 0, k) {
	// 		cout << dp[i][j] << " ";
	// 	}
	// 	cout << '\n';
	// }

	cout << dp[n-1][k-1] << '\n';
	// int cur = n-1;
	// int kk = k-1;
	// int jumps = 0;
	// do {
	// 	cout << cur << " ( " << nums[cur] << " ) | ";
	// 	cur = par[cur][kk];
	// 	--kk;
	// 	++jumps;
	// } while(cur >= 0);
	// cout << '\n';
	return 0;
}
