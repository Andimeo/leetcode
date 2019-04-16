/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 *
};
*/

int nextVal(char *s, int &l) {
  int d;
  sscanf(s, "%d", &d);
  int dd = d;
  l = 0;
  while (dd) {
    l++;
    dd /= 10;
  }
  return d;
}

int nextDash(char *s) {
  int l = 0;
  while(*s && s[l++] == '-');
  return l;
}

class Solution {
public:
  int v[1004], d[1004];
  TreeNode* recoverFromPreorder(string S) {
    char *s = S.c_str();
    int i = 0;
    while (*s) {
      int depth = nextDash(s);
      s += depth;
      int l;
      int val = nextVal(s, l);
      s += l;
      v[i] = val;
      d[i] = depth;
      i++;
    }
    if (!i) return nullptr;
    return recover(0, i - 1, 0);
  }

  TreeNode* recover(int start, int end, int depth){
    if (end < start) return nullptr;
    TreeNode *root = new TreeNode(v[start]);
    root->left = nullptr;
    root->right = nullptr;
    int first = -1, second = -1;
    for (int i = start + 1 ; i <= end; i++) {
      if (d[i] == depth + 1 && first == -1) {first = i; continue; }
      if (d[i] == depth + 1 && first != -1) second = i;
    }
    if (first == -1) return root;
    if (second == -1)
      root->left = recover(second, end, depth + 1);
    else {
      root->left = recover(first, second - 1, depth + 1);
      root->right = recover(second, end, depth + 1);
    }
    return root;
  }
};
