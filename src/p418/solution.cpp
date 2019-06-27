#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  int wordsTyping(const vector<string>& sentence, int rows, int cols) {
    string line = "";
    for (auto& s : sentence) {
      line += (s + " ");
    }
    int n = line.length();
    int len = 0;
    for (int i = 0 ; i < rows; i++) {
      len += cols;
      if (line[len % n] == ' ') {
	len++;
      } else {
	while (len > 0 && line[(len - 1) % n] != ' ') {
	  len--;
	}
      }
    }
    return len / n;
  }
};

int main(void) {
  Solution sol;
  cout << sol.wordsTyping(vector<string> {"hello", "world"}, 2, 8) << endl;
  cout << sol.wordsTyping(vector<string> {"a", "bcd", "e"}, 3, 6) << endl;
  cout << sol.wordsTyping(vector<string> {"I", "had", "apple", "pie"}, 4, 5) << endl;
  cout << sol.wordsTyping(vector<string> {"ab", "abcd"}, 20000, 2) << endl;
  return 0;
}
