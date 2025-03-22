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

  int n, k;
  cin >> n >> k;

  ll malfunctions = 0;
  list<int> lru;
  unordered_set<int> valid;

  while (k--) {
    string s;
    cin >> s;

    if (s == "READ") {
      int bAddr, eAddr;
      cin >> bAddr >> eAddr;

      for (; bAddr <= eAddr; bAddr++) {
        auto it = find(all(lru), bAddr);

        if (it != lru.end()) { // it is cached
          malfunctions += 1 - valid.count(bAddr);
          lru.erase(it);
        } else { // it is not cached
          if (sz(lru) == n) { // evict oldest entry
            lru.pop_front();
          }
          valid.insert(bAddr);
        }
        // maintain LRU invariant
        lru.push_back(bAddr);
      }
    } else if (s == "MALFUNCTION") {
      valid.clear();
    } else {
      assert(false);
    }
  }
  cout << malfunctions;
}