package p313;

public class Solution {
	public int nthSuperUglyNumber(int n, int[] primes) {
		int indices[] = new int[primes.length];
		int value[] = new int[n];
		value[0] = 1;
		for (int i = 1; i < n; i++) {
			int min = Integer.MAX_VALUE;
			for (int j = 0; j < primes.length; j++)
				min = Math.min(min, primes[indices[j]] * primes[j]);
			value[i] = min;
			for (int j = 0; j < primes.length; j++)
				if (min == primes[indices[j]] * primes[j])
					indices[j]++;
		}
		return value[n-1];
	}
}
