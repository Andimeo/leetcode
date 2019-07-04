#include <bits/stdc++.h>

using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    string to(int v) {
        stringstream ss;
        ss << v;
        return ss.str();
    }
    int to(string s) {
        stringstream ss(s);
        int v;
        ss >> v;
        return v;
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "";
        string result = to(root->val);
        if (root->left == NULL && root->right == NULL) return result;
        string left = serialize(root->left), right = serialize(root->right);
        result = result + "(" + left + ")" + "(" + right + ")";
        return result;    
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == "") return NULL;
        int left_start=-1, left_end=-1, right_start=-1, right_end=-1, level = 0;
        for (int i = 0 ; i < data.length(); i++) {
            if (data[i] == '(') {
                if (level == 0) {
                    if (left_start == -1) left_start = i;
                    else right_start = i;
                }
                level++;
            }
            if (data[i] == ')') {
                level--;
                if (level == 0) {
                    if (left_end == -1) left_end = i;
                    else right_end = i;
                }
            }
        }
        int val = (left_start == -1 ? to(data) : to(data.substr(0, left_start)));
        TreeNode* node = new TreeNode(val);
        if (left_start != -1) {
            node->left = deserialize(data.substr(left_start + 1, left_end - left_start - 1));
            node->right = deserialize(data.substr(right_start + 1, right_end - right_start - 1));
        }
        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
