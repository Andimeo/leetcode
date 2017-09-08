class Solution {

    TreeNode s1,s2,pre;
    void hehe(TreeNode root)
    {
        if(null == root)return ;
        hehe(root.left);
        if(pre != null && pre.val > root.val)
        {
            if(s1==null){s1=pre;s2=root;}
            else s2=root;
        }
        pre=root;
        hehe(root.right);
    }
    public void recoverTree(TreeNode root) {
        if(null == root)return ;
        s1=s2=pre=null;
        hehe(root);
        int t = s1.val;
        s1.val = s2.val;
        s2.val = t;
    }
};