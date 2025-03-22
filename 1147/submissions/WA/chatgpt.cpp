#include <iostream>
#include <unordered_map>
#include <deque>
#include <unordered_set>

using namespace std;

class LRUCache {
public:
    LRUCache(int n) : cache_size(n), isMalfunctioning(false), corrupted_reads(0) {}

    // Function to process a read event
    void read(int x, int y) {
        for (int i = x; i <= y; ++i) {
            if (isMalfunctioning) {
                // If the cache is malfunctioning, check if the value is in the cache
                if (cache_set.find(i) != cache_set.end()) {
                    // If the value is in the cache and corrupted, count as a corrupted read
                    if (corrupted_set.find(i) != corrupted_set.end()) {
                        corrupted_reads++;  // This read is corrupted since it's in the corrupted set
                    }
                }
                // Add the item to the cache anyway (new read after malfunction)
                if (cache.size() >= cache_size) {
                    // Evict least recently used item
                    int lru = cache.front();
                    cache.pop_front();
                    cache_set.erase(lru);
                    cache_map.erase(lru);
                    corrupted_set.erase(lru);  // Remove from corrupted set on eviction
                }
                cache.push_back(i);
                cache_set.insert(i);
                cache_map[i] = --cache.end();
                // After malfunction, mark it as corrupted
                if (isMalfunctioning) {
                    corrupted_set.insert(i);
                }
            } else {
                // If the cache is working fine (not malfunctioning)
                if (cache_set.find(i) != cache_set.end()) {
                    // Move the element to the most recently used position
                    cache.erase(cache_map[i]);
                    cache.push_back(i);
                    cache_map[i] = --cache.end();
                } else {
                    // Cache miss: add to the cache
                    if (cache.size() >= cache_size) {
                        // Evict least recently used item
                        int lru = cache.front();
                        cache.pop_front();
                        cache_set.erase(lru);
                        cache_map.erase(lru);
                    }
                    cache.push_back(i);
                    cache_set.insert(i);
                    cache_map[i] = --cache.end();
                }
            }
        }
    }

    // Function to handle malfunction event
    void malfunction() {
        isMalfunctioning = true;  // Set malfunction flag to true
        // Malfunctioning only marks existing values as corrupted, not clearing the cache.
    }

    // Function to get the count of corrupted reads
    int get_corrupted_reads() const {
        return corrupted_reads;
    }

private:
    int cache_size;
    bool isMalfunctioning;  // Flag to track if the cache is malfunctioning
    unordered_set<int> cache_set;
    unordered_map<int, deque<int>::iterator> cache_map;
    deque<int> cache;
    int corrupted_reads;  // Counter for corrupted reads
    unordered_set<int> corrupted_set;  // Track which elements are corrupted
};

int main() {
    int n, k;
    cin >> n >> k;

    LRUCache cache(n);

    for (int i = 0; i < k; ++i) {
        string command;
        cin >> command;

        if (command == "READ") {
            int x, y;
            cin >> x >> y;
            cache.read(x, y);
        } else if (command == "MALFUNCTION") {
            cache.malfunction();
        }
    }

    cout << cache.get_corrupted_reads() << endl;
    return 0;
}
