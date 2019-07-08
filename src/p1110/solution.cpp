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
  void run(TreeNode* parent, TreeNode* root, set<int>& tod, vector<TreeNode*>& ans, bool left) {
    if (!root) return;
    TreeNode* new_parent = root;
    if (tod.count(root->val) == 1) {
      if (parent) {
	if (left) parent->left = NULL;
	else parent->right = NULL;
      }
      new_parent = NULL;
    } else if (!parent) {
      ans.push_back(root);
    }
    run(new_parent, root->left, tod, ans, true);
    run(new_parent, root->right, tod, ans, false);
  }
  vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
    vector<TreeNode*> result;
    set<int> td;
    for (auto ele : to_delete) td.insert(ele);
    run(NULL, root, td, result, true);
    return result;
  }
};
