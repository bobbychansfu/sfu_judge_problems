#include <bits/stdc++.h>
using namespace std;
#define rep(i, a, b) for (int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

// configurable
// const int n = 10000;
// const int k = 1000;
// const double MALFUNCTION_CHANCE = 0.01;
// const int RANGE_MAX = 1E2;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int main(int argc, char *argv[]) {
  cin.tie(0)->sync_with_stdio(0);

  int n = atoi(argv[1]);
  int k = atoi(argv[2]);
  double MALFUNCTION_CHANCE = atof(argv[3]);
  int UPPER_BOUND = atoi(argv[4]);
  int RANGE_MAX = atoi(argv[5]);

  cout << n << ' ' << k << '\n';
  rep(i, 0, k) {
    if (uniform_real_distribution<double>(0, 1)(rng) < MALFUNCTION_CHANCE) {
      cout << "MALFUNCTION\n";
      continue;
    }

    int lower = uniform_int_distribution(0, UPPER_BOUND)(rng);
    int upper = lower + uniform_int_distribution(0, RANGE_MAX)(rng);

    if (lower > upper) {
      swap(lower, upper);
    }

    cout << "READ " << lower << ' ' << upper << '\n';
  }
}