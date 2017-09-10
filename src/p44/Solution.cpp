class Solution {
	public:
		bool isMatch(const char *s, const char *p) {
			int i = 0;
			int j = 0;
			int backup_i = -1;
			int backup_j = -1;
			while (s[i] != '\0') {
				if (s[i] == p[j] || p[j] == '?') {
					i++; j++;
				} else if (p[j] == '*') {
					backup_j = j;
					backup_i = i;
					j++;
				} else if (s[i] != p[j]) {
					if (backup_j == -1) {
							return false;
					}
					j = backup_j;
					i = backup_i + 1;
					backup_i = i;
					j++;
				}
			}
			if (s[i] == '\0') {// && left all '*' return true;
				while (p[j] != '\0') {
					if (p[j] != '*') {
						return false;
					}
					j++;
				}
				return true;
			}
			return false;
		}
};
