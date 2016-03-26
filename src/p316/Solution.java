package p316;

import java.util.Stack;

public class Solution {

	int countOne(int n) {
		int count = 0;
		while (n > 0) {
			count++;
			n = n & (n - 1);
		}
		return count;
	}

	int unsetBit(int bit, char c) {
		return bit ^ (1 << (c - 'a'));
	}

	int setBit(int bit, char c) {
		return bit | (1 << (c - 'a'));
	}

	public String removeDuplicateLetters(String s) {
		int bits[] = new int[s.length() + 1];
		bits[s.length()] = 0;
		for (int i = s.length() - 1; i >= 0; i--) {
			char c = s.charAt(i);
			bits[i] = setBit(bits[i + 1], c);
		}

		Stack<Character> stack = new Stack<>();
		int bit = 0;
		for (int i = 0; i < s.length(); i++) {
			//最后一个条件，当这个字符已经出现在栈中时，不需要考虑这个字符了，因为假设它可以和后面的构成一个更小字典序的组合，那么已经在栈中的字符同样可以
			while (!stack.empty() && countOne(unsetBit(bit, stack.peek()) | bits[i]) == countOne(bits[0]) && stack.peek() > s.charAt(i) && setBit(bit, s.charAt(i)) != bit) {
				bit = unsetBit(bit, stack.pop());
			}
			int newBit = setBit(bit, s.charAt(i));
			if (bit != newBit) {
				bit = setBit(bit, s.charAt(i));
				stack.push(s.charAt(i));
			}
		}
		StringBuilder sb = new StringBuilder();
		while (!stack.empty()) {
			sb.append(stack.pop());
		}
		return sb.reverse().toString();
	}

	public static void main(String[] args) {
		System.out.println(new Solution().removeDuplicateLetters("bacabc"));
	}

}
