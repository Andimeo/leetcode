class Slope {
	int up, down;

	public int hashCode() {
		int hash = 7;
		hash = 31 * hash + up;
		hash = 31 * hash + down;
		return hash;
	}

	public boolean equals(Object o) {
		if (null == o || !(o instanceof Slope))
			return false;
		Slope slope = (Slope) o;
		return up == slope.up && down == slope.down;
	}
}

public class Solution {
	private int gcd(int x, int y) {
		return y == 0 ? x : gcd(y, x % y);
	}

	public int maxPoints(Point[] points) {
		int res = 0;
		for (int i = 0; i < points.length; i++) {
			int equal = 0;
			int max = 0;
			Map<Slope, Integer> map = new HashMap<Slope, Integer>();
			for (int j = i + 1; j < points.length; j++) {
				int up = points[j].y - points[i].y;
				int down = points[j].x - points[i].x;
				if (up == 0 && down == 0) {
					equal++;
					continue;
				}
				int v = gcd(up, down);
				up /= v;
				down /= v;
				Slope slope = new Slope();
				slope.up = up;
				slope.down = down;
				if (map.containsKey(slope))
					map.put(slope, map.get(slope) + 1);
				else
					map.put(slope, 1);
				max = Math.max(max, map.get(slope));
			}
			res = Math.max(res, max + equal + 1);
		}
		return res;
	}

	public static void main(String[] args) {
		Point[] points = new Point[3];
		points[0] = new Point(0, 0);
		points[1] = new Point(-1, -1);
		points[2] = new Point(2, 2);
		System.out.println(new Solution().maxPoints(points));
	}
}