/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
  typedef pair<int, int> pi;
  pi run(TreeNode* root) {
    if (!root) return {0, 0};
    pi result, left, right;
    if (root->left) {
      left = run(root->left);
    }
    if (root->right) {
      right = run(root->right);
    }
    result.first = max(left.first, right.first) + 1;
    result.second = left.first + right.first;
    int child = max(left.second, right.second);
    result.second = max(result.second, child);
    return result;
  }
  int diameterOfBinaryTree(TreeNode* root) {
    return run(root).second;
  }
};
