#include <cstdio>
#include <map>
#include <string>
using namespace std;

map<int, string> M;

string q_at(int x){
    auto it = M.upper_bound(x);
    it--;
    return it->second;
}

int main(){
    int n, q, a, b;
    char s[12];
    char c;
    map<int, string>::iterator it, rm_start, rm_end;
    scanf("%d%d", &n, &q);
    M[-1]="white";
    while(q--){
        scanf(" %c", &c);
        if (c == 'q') {
            scanf("%d", &a);
            it = M.upper_bound(a);
            it--;
            printf("%s\n",it->second.c_str());
        } else {
            scanf("%d%d %s", &a, &b, s);
            string S(s);
            
            string col_after = q_at(b+1);
            rm_start = M.lower_bound(a);
            rm_end = M.upper_bound(b);

            M.erase(rm_start, rm_end);
            M[a] = S;
            M[b+1] = col_after;
        }
    }
}