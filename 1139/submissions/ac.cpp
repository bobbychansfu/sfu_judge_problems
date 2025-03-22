#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

vector<vector<vi>> st;
int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, k;
	cin >> n >> k;
	vi nums(n);
	for(auto &x : nums) cin >> x;

	int x = __bit_width(n)-1;
	st = vector<vector<vi>>(2, vector(x+1, vi(n)));
	rep(i, 0, n) {
		st[0][0][i] = st[1][0][i] = nums[i];
	}
	
	for (int i = 1; i <= x; i++) {
		for (int j = 0; j + (1 << i) <= n; j++) {
        	st[0][i][j] 
				= min(st[0][i - 1][j], st[0][i - 1][j + (1 << (i - 1))]);
			st[1][i][j] 
				= max(st[1][i - 1][j], st[1][i - 1][j + (1 << (i - 1))]);
		}
	}

	auto query = [&](int l, int r) {
		int i = __bit_width(r - l+1) - 1;
		return 
			max(st[1][i][l], st[1][i][r - (1 << i) + 1])
			- min(st[0][i][l], st[0][i][r - (1 << i) + 1]);
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

	cout << dp[n-1][k-1] << '\n';
	return 0;
}
