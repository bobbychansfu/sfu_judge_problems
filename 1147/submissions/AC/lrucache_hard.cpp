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

  class cache_entry {
  public:
    int start;
    int end;
    int time;

    int range() { return end - start; }

    int valid(int currTime) { return time == currTime; }
  };

  ll malfunctions = 0;
  int freeSpots = n;

  int globalTime = 0;
  list<cache_entry> lru;
  map<int, list<cache_entry>::iterator> m;

  while (k--) {
    string s;
    cin >> s;

    if (s == "READ") {
      int bAddr, eAddr;
      cin >> bAddr >> eAddr;
      eAddr += 1; // [)

#ifdef SHORTCUT
      bool shortcut = false;
      int origEnd = eAddr;

      // only entries [bAddr, bAddr + n) can contribute to malfunction count
      // entries [bAddr + n, eAddr) are guaranteed to be read in from ROM
      if (eAddr - bAddr >= 2 * n) {
        shortcut = true;
        eAddr = bAddr + n;
      }
#endif

      while (bAddr < eAddr) {
        auto it = m.upper_bound(bAddr);
        if (it != m.begin() &&
            prev(it)->second->end > bAddr) { // bAddr is cached
          auto cp = prev(it)->second;        // cached entry
          auto pp = *it->second;
          auto cpp = *cp;

          // account for possible malfunctions
          malfunctions +=
              (min(eAddr, cp->end) - bAddr) * (!cp->valid(globalTime));

          // split left side cache entry if necessary (LRU invariant)
          if (cp->start < bAddr) {
            m[cp->start] = lru.insert(next(cp), {cp->start, bAddr, cp->time});
          }

          // split right side cache entry if necessary (LRU invariant)
          if (cp->end > eAddr) {
            m[eAddr] = lru.insert(next(cp), {eAddr, cp->end, cp->time});
          }

          m[bAddr] =
              lru.insert(lru.end(), {bAddr, min(eAddr, cp->end), cp->time});
          bAddr = cp->end;

          lru.erase(cp);

        } else { // it is not cached
          int nextCachedValue = INT_MAX;
          if (it != m.end()) {
            nextCachedValue = it->first;
          }

          cache_entry cp{bAddr, min(nextCachedValue, eAddr), globalTime};
          
          if (freeSpots) { // we can add to the cache
            cp.end = min(cp.end, bAddr + freeSpots);
            freeSpots -= cp.range();
            
          } else { // cache is full
            // evict only as much as needed
            auto last_used = lru.begin();
            cp.end = min(cp.end, bAddr + last_used->range());
            m.erase(last_used->start);

            // evict entire range
            if (last_used->range() <= cp.range()) {
              lru.erase(last_used);
            }

            // split cache entry if necessary (LRU invariant)
            if (last_used->range() > cp.range()) {
              m.erase(last_used->start);
              last_used->start += cp.range();
              m[last_used->start] = last_used;
            }
          }

          m[bAddr] = lru.insert(lru.end(), cp);
          bAddr = cp.end;
        }

#ifdef CONSOLIDATE
        // consolidation
        while (sz(lru) > 1) {
          auto it = prev(lru.end());
          auto pv = prev(it);

          if (pv->end + 1 == it->start && (it->time == pv->time || max(it->time, pv->time) < globalTime)) {
            pv->end = it->end;
            m.erase(it->start);
            lru.erase(it);
          } else {
            break;
          }
        }
#endif
      }

#ifdef SHORTCUT
      if (shortcut) {
        m.clear();
        lru.clear();
        m[origEnd - n] =
            lru.insert(lru.end(), {origEnd - n, origEnd, globalTime});
      }
#endif

    } else if (s == "MALFUNCTION") {
      globalTime++;
    } else {
      assert(false);
    }
  }

  cout << malfunctions;
}