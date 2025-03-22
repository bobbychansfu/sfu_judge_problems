#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, m, k;

	cin >> n >> m >> k;

	typedef tuple<int, int, int> edge_t;
	vector<edge_t> edges;
	rep(i, 0, m) {
		int a, b, c;
		cin >> a >> b >> c;
		--a;
		--b;
		edges.emplace_back(c, a,b);
	}

	int dummy = n + 1;
	
	rep(i, 0, k) {
		int x;
		cin >> x;
		edges.emplace_back(0,n, x-1);
	}

	sort(all(edges));

	vi p(n+1, -1), h(n+1, 0);
	function<int(int)> find_ = [&](int a) {
		if(p[a] == -1) return a;

		return p[a] = find_(p[a]);
	};

	auto union_ = [&](int a, int b) {
		auto ra = find_(a), rb = find_(b);

		if(h[ra] < h[rb]) swap(ra, rb);

		p[rb] = ra;
		h[ra] += h[ra]==h[rb];
	};

	ll total_cost = 0;
	for(auto [c, a, b] : edges) {
		if(find_(a) != find_(b)) {
			total_cost += c;
			union_(a, b);
		}
	}

	cout << total_cost << '\n';

	return 0;
}
