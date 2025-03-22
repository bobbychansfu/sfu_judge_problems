#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

/*
    56505009 - 9600
    compute maximum number instead of digit-sum
    same logic as before, represent number as array of 10digits
*/
struct number {
    bool is_zero = true;
    int num_digits = 0;
    vi dig_count = vi(10, 0);

    inline number operator+ (int num) {
        auto result = *this;
        
        result.is_zero &= !num;
        result.dig_count[9-num]++;
        ++result.num_digits;
        return result;
    }
};
inline bool operator<(const number a, const number b) {
    if(a.is_zero || b.is_zero) {
        if(!a.is_zero) return false;
        else if(!b.is_zero)  return true;
        else return a.num_digits < b.num_digits;
    }
    if(a.num_digits != b.num_digits) return a.num_digits < b.num_digits;
    return  a.dig_count < b.dig_count;
};
ostream& operator<<(ostream& out, const number a) {
    if(a.is_zero) {
        out << 0;
        return out;
    }
    rep(i, 0, 10) {
        rep(j, 0, a.dig_count[i]) out << 9 - i;
    }
    return out;
}

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    cin >> n;

    vi nums(n);
    string s;
    cin >> s;
    for(int i=0; i<n; ++i){
        nums[i] = s[i]-'0';
    }

    // first 3 elements are dummy
    vector<number> dp(n+3);
    rep(i, 3, n+3) {
        auto take = max(dp[i-2] + nums[i-3], dp[i-3] + nums[i-3]);
        auto skip = dp[i-1];
        dp[i] = max(skip, take);
    }

    cout << dp[n+2] << '\n';
 
    return 0;
}