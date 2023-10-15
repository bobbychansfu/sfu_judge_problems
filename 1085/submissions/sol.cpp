#include <bits/stdc++.h>
#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int n, l, v, q;
  cin >> n >> l >> v >> q;

  vector<double> balls(n);
  rep(i, 0, n) {
    int x;
    string s;
    cin >> x >> s;

    if (s == "LEFT") {
      balls[i] = x / (double)v;
    } else if (s == "RIGHT") {
      balls[i] = (l - x) / (double)v;
    }
  }

  sort(all(balls));

  rep(i, 0, q) {
    int t;
    cin >> t;

    cout << distance(upper_bound(all(balls), t), balls.end()) << '\n';
  }
}