#include <bits/stdc++.h>

using namespace std;

int main() {
  map<char, char> m{{'Y', 'A'}, {'M', 'B'}, {'Z', 'C'}, {'U', 'D'}, {'G', 'E'},
                    {'K', 'F'}, {'B', 'G'}, {'S', 'H'}, {'L', 'I'}, {'V', 'J'},
                    {'H', 'K'}, {'T', 'L'}, {'O', 'M'}, {'P', 'N'}, {'C', 'O'},
                    {'I', 'P'}, {'X', 'Q'}, {'J', 'R'}, {'D', 'S'}, {'A', 'T'},
                    {'N', 'U'}, {'W', 'V'}, {'F', 'W'}, {'R', 'X'}, {'Q', 'Y'},
                    {'E', 'Z'}};

  char c;
  while (cin >> c) {
    if (m.count(c)) {
      cout << m[c];
    } else {
      cout << c;
    }
  }
}