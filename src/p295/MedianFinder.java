package p295;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

abstract class Heap<T> {
	private List<T> heap = new ArrayList<>();
	private int size;

	protected abstract int compare(T a, T b);

	public void add(T b) {
		if (size == heap.size()) {
			heap.add(b);
			size++;
		} else {
			heap.set(size++, b);
		}
		shiftUp(size - 1);
	}

	public T peek() {
		if (size == 0)
			throw new NoSuchElementException();
		return heap.get(0);
	}

	public T pop() {
		if (size == 0)
			throw new NoSuchElementException();
		T ans = heap.get(0);
		heap.set(0, heap.get(--size));
		shiftDown(0);
		return ans;
	}

	public int size() {
		return size;
	}

	private void swap(int i, int j) {
		T temp = heap.get(i);
		heap.set(i, heap.get(j));
		heap.set(j, temp);
	}

	private void shiftUp(int index) {
		while (index > 0) {
			int parent = (index - 1) / 2;
			if (compare(heap.get(parent), heap.get(index)) < 0)
				swap(parent, index);
			index = parent;
		}
	}

	private void shiftDown(int index) {
		T max = heap.get(index);
		int maxIndex = index;
		int leftChild = index * 2 + 1;
		if (leftChild < size && compare(heap.get(maxIndex), heap.get(leftChild)) < 0) {
			max = heap.get(leftChild);
			maxIndex = leftChild;
		}
		int rightChild = index * 2 + 2;
		if (rightChild < size && compare(heap.get(maxIndex), heap.get(rightChild)) < 0) {
			max = heap.get(rightChild);
			maxIndex = rightChild;
		}
		if (maxIndex != index) {
			swap(index, maxIndex);
			shiftDown(maxIndex);
		}
	}
}

class MaxHeap extends Heap<Integer> {
	@Override
	protected int compare(Integer a, Integer b) {
		return a - b;
	}
}

class MinHeap extends Heap<Integer> {
	@Override
	protected int compare(Integer a, Integer b) {
		return b - a;
	}

}

public class MedianFinder {
	MaxHeap maxHeap = new MaxHeap();
	MinHeap minHeap = new MinHeap();

	// Adds a number into the data structure.
	public void addNum(int num) {
		maxHeap.add(num);
		if (minHeap.size() > 0 && maxHeap.peek() > minHeap.peek() || maxHeap.size() > minHeap.size() + 1) {
			minHeap.add(maxHeap.pop());
		}
		if (maxHeap.size() < minHeap.size()) {
			maxHeap.add(minHeap.pop());
		}
	}

	// Returns the median of current data stream
	public double findMedian() {
		if (maxHeap.size() == minHeap.size() + 1)
			return maxHeap.peek();
		return (maxHeap.peek() + minHeap.peek()) / 2.;
	}

	public static void main(String[] args) {
		MedianFinder f = new MedianFinder();
		f.addNum(-1);
		System.out.println(f.findMedian());
		f.addNum(-2);
		System.out.println(f.findMedian());
		f.addNum(-3);
		System.out.println(f.findMedian());
		f.addNum(-4);
		System.out.println(f.findMedian());
		f.addNum(-5);
		System.out.println(f.findMedian());
	}

}
