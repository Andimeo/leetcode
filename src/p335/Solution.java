package p335;

import java.util.ArrayList;
import java.util.List;

public class Solution {
	class Point {
		int x, y;

		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	class Segment {
		Point p1, p2;

		public Segment(int x1, int y1, int x2, int y2) {
			this.p1 = new Point(x1, y1);
			this.p2 = new Point(x2, y2);
		}
	}

	public boolean isSelfCrossing(int[] d) {
		int multipliers[][] = { { 0, 1 }, { -1, 0 }, { 0, -1 }, { 1, 0 } };
		int x = 0, y = 0;
		List<Segment> list = new ArrayList<>();
		for (int i = 0; i < d.length; i++) {
			int nx = x + multipliers[i % 4][0] * d[i], ny = y + multipliers[i % 4][1] * d[i];
			Segment seg = new Segment(x, y, nx, ny);
			x = nx;
			y = ny;
			if (isCrossing(list, seg)) {
				return true;
			}
			list.add(seg);
		}
		return false;
	}

	private boolean isCrossing(List<Segment> list, Segment seg) {
		for (int i = 0; i < list.size() - 1; i++) {
			Segment oldSeg = list.get(i);
			if (isCrossing(oldSeg, seg)) {
				return true;
			}
		}
		return false;
	}

	private boolean isCrossing(Segment oldSeg, Segment seg) {
		int d1, d2, d3, d4;
		d1 = crossProduct(oldSeg.p1, oldSeg.p2, seg.p1);
		d2 = crossProduct(oldSeg.p1, oldSeg.p2, seg.p2);
		d3 = crossProduct(seg.p1, seg.p2, oldSeg.p1);
		d4 = crossProduct(seg.p1, seg.p2, oldSeg.p2);
		if (((d1 < 0 && d2 > 0) || (d1 > 0 && d2 < 0)) && ((d3 < 0 && d4 > 0) || (d3 > 0 && d4 < 0)))
			return true;
		else if (d1 == 0 && on_segment(oldSeg.p1, oldSeg.p2, seg.p1))
			return true;
		else if (d2 == 0 && on_segment(oldSeg.p1, oldSeg.p2, seg.p2))
			return true;
		else if (d3 == 0 && on_segment(seg.p1, seg.p2, oldSeg.p1))
			return true;
		else if (d4 == 0 && on_segment(seg.p1, seg.p2, oldSeg.p2))
			return true;
		else
			return false;
	}

	private boolean on_segment(Point p1, Point p2, Point p3) {
		int minx = Math.min(p1.x, p2.x), maxx = Math.max(p1.x, p2.x);
		int miny = Math.min(p1.y, p2.y), maxy = Math.max(p1.y, p2.y);
		return p3.x <= maxx && p3.x >= minx && p3.y <= maxy && p3.y >= miny;
	}

	private int crossProduct(Point p1, Point p2, Point p3) {
		return (p3.x - p1.x) * (p2.y - p1.y) - (p2.x - p1.x) * (p3.y - p1.y);
	}
}
