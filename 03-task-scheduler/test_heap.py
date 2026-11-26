import random
from heap import MaxHeap


def test_lecture_example():
    heap = MaxHeap()
    for name, priority in [("A", 3), ("B", 9), ("C", 5), ("D", 7)]:
        heap.insert(priority, name)
    order = [heap.extract_max()[1] for _ in range(4)]
    assert order == ["B", "D", "C", "A"]


def test_random_matches_sorted():
    values = [random.randint(1, 100) for _ in range(200)]
    heap = MaxHeap()
    for v in values:
        heap.insert(v, "x")
    result = [heap.extract_max()[0] for _ in range(200)]
    assert result == sorted(values, reverse=True)


def test_empty_heap():
    heap = MaxHeap()
    try:
        heap.extract_max()
        assert False, "should have raised"
    except IndexError:
        pass


def test_single_item_and_duplicates():
    heap = MaxHeap()
    heap.insert(5, "a")
    assert heap.extract_max() == (5, "a")
    heap.insert(2, "b")
    heap.insert(2, "c")
    assert len(heap) == 2


if __name__ == "__main__":
    test_lecture_example()
    test_random_matches_sorted()
    test_empty_heap()
    test_single_item_and_duplicates()
    print("all tests passed")
