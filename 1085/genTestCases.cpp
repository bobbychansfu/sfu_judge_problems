#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);

  int balls, length, velocity, queries;
  cin >> balls >> length >> velocity >> queries;

  assert(balls < length);
  cout << balls << ' ' << length << ' ' << velocity << ' ' << queries << '\n';

  set<int> s;
  rep(i, 0, balls) {
    int b = (rand() % (length - 1)) + 1;
    if (s.count(b)) {
      continue;
    }

    cout << b << ' ';
    if (rand() % 2) {
      cout << "LEFT";
    } else {
      cout << "RIGHT";
    }
    cout << '\n';
  }

  rep(i, 0, queries) {
    cout << (rand() % max(1, (length / velocity))) + velocity << '\n';
  }
}