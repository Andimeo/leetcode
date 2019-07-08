class Solution {
public:
  vector<int> maxDepthAfterSplit(string seq) {
    int n = seq.length();
    vector<int> result(n, 0);
    int level = 0;
    for (int i = 0; i < n ; i++) {
      if (seq[i] == '(') {
	if (level++ % 2 == 1) result[i] = 1;
      } else {
	if (--level % 2 == 1) result[i] = 1;
      }
    }
    return result;
  }
};






































  ----:---F1  *scratch*      All L1     (Fundamental)--------------------------------------------------------------------------------------------------------------------------
 create mode 100644 src/p815/solution.cpp
------------------------------------------------------------
  ~/Documents/workspace/leetcode(master) » git push origin master                                                                                  andimeo@luyangs-MacBook-Pro
  Enumerating objects: 12, done.
					     Counting objects: 100% (12/12), done.
Delta compression using up to 4 threads
					     Compressing objects: 100% (8/8), done.
					     Writing objects: 100% (10/10), 1.44 KiB | 738.00 KiB/s, done.
					     Total 10 (delta 4), reused 0 (delta 0)
					     remote: Resolving deltas: 100% (4/4), completed with 2 local objects.
					     To https://github.com/Andimeo/leetcode.git
   66ed6fc..cbf9c5f  master -> master
------------------------------------------------------------
     ~/Documents/workspace/leetcode(master) » ls                                                                                                      andimeo@luyangs-MacBook-Pro
a.out  airbnb bin    src
------------------------------------------------------------
     ~/Documents/workspace/leetcode(master) » emacs ../leetcode/airbnb/8-puzzle.py                                                                    andimeo@luyangs-MacBook-Pro
------------------------------------------------------------








































     ----:---F1  *scratch*      All L1     (Fundamental)--------------------------------------------------------------------------------------------------------------------------
     ~/Documents/workspace/leetcode(master) » ls                                                                                                      andimeo@luyangs-MacBook-Pro
a.out  airbnb bin    src








































     ----:---F1  *scratch*      All L1     (Fundamental)--------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------
     ~/Documents/workspace/leetcode(master) » cd ..                                                                                                   andimeo@luyangs-MacBook-Pro
------------------------------------------------------------
~/Documents/workspace » cd algorithm                                                                                                             andimeo@luyangs-MacBook-Pro
------------------------------------------------------------
~/Documents/workspace/algorithm(master) » ls                                                                                                     andimeo@luyangs-MacBook-Pro
codeforce     fenwick       geometry      graph_theory  number_theory string        topcoder
------------------------------------------------------------
~/Documents/workspace/algorithm(master) » cd ..                                                                                                  andimeo@luyangs-MacBook-Pro
------------------------------------------------------------
~/Documents/workspace » ls                                                                                                                       andimeo@luyangs-MacBook-Pro
EverydayWechat               MyBlog                       coala-tutorial               leetcode                     topcoder
ICPC                         RemoteSystemsTempFiles       coursera                     scala-functional-programming xTR
JVM                          algorithm                    fpinscala                    stoc_filter
-------------------------------------->..." to include in what will be committed)

src/p773ed files present (use "git add" to track)
------------------------------------------------------------
~/Documents/wor*      All L----------------------------------------------------------
~/Documents/workspace/leetcode(master*) » git add .      ----:---F1  *scratch*      All L1     (Fundamental)----------------------------
~/Documents/workspace/leetcode(master*) » gst                            s/workspace/leetcode(master) » gito
-----------------------------------------------------------
~/Documents/workspace/leetcodeetcode(master) » git push origin master                                                                                  andimeo@luyangs             andimeo@luyangs-MacBook-Pro
------------------------------------------------------------
~/Documents/workspace/leetcode(--------
~/Documents/workspace done.
Writist login: Fri Ju               d::__1::__vector_base<int, std::__1
