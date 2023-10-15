#include <iostream>
#include <vector>
#include <unordered_map>
#include <fstream>
#include <bitset>
#include <set>
#include <map>
#include <cmath>
using namespace std;
// const int N_WORDS = 5757;

vector<string> words;

string re(string guess, string word){
	string res = "_____";
	for(int i=0;i<5;++i){
		if (guess[i]==word[i]){
			res[i] = '*';
			guess[i] = ' ';
			word[i] = '^';
		}
	}
	for(int i=0; i<5; ++i){
		for(int j=0; j<5; ++j){
			if (word[i] == guess[j]){
				res[j] = '-';
				guess[j] = ' ';
				word[i] = '^';
				break;
			}
		}
	}
	return res;
}

void dq(vector<string> &curr, string guess, string res){
	vector<string> ncurr;
	for(auto &s: curr){
		if (re(guess, s) == res) {
			ncurr.push_back(s);
		}
	}
	curr.clear();
	curr.assign(ncurr.begin(), ncurr.end());
}

string bestguess(vector<string> &curr){
	// int mn = 1e9;
	// string gg = "rates";
	// if (curr.size() > 2000) return gg;
	return curr[0];
	// for(auto &w: words){
	// 	map<string, int> M;
	// 	for(auto &s: curr){
	// 		M[re(w, s)]++;
	// 	}
	// 	int score = 0;
	// 	for(auto &[a, b]: M){
	// 		score += b*b;
	// 	}
	// 	if (score < mn){
	// 		mn = score;
	// 		gg = w;
	// 	}
	// }
	// return gg;
}

int main(){
	auto f = ifstream("words.txt");
	string word, hint;
	while(f >> word){
		if (word.size() != 5) {
			continue;
		}
		int n = words.size();
		words.push_back(word);
	}

	// for(int i=0; i<243; ++i){
	// 	if (i < 243)
	// }

	string ff;
	int G;
	int T;
	cin >> T >> G;

	int tot_guesses = 0;

	while(T--){
		vector<string> curr(words.begin(), words.end());
		string gg = "rates";

		while(true){
			if (tot_guesses >= G) return 0;
			if (curr.size() > 2){
				string best = bestguess(curr);
				gg = best;
			} else {
				gg = curr[0];
			}
			tot_guesses++;
			cout << gg << endl;
			cin >> hint;
			if (hint == "ERROR") {
				return 0;
			}
			if (hint == "*****") {
				break;
			}
			dq(curr, gg, hint);
		}
	}
}