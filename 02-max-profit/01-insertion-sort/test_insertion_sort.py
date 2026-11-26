from insertion_sort import insertion_sort, merge_sort


def test_sorts():
    data = [5, 2, 9, 1, 5, 6]
    assert insertion_sort(data)[0] == sorted(data)
    assert merge_sort(data) == sorted(data)
    assert insertion_sort([])[0] == []


def test_counts_from_lecture():
    # reversed list of 4 -> 6 comparisons, 6 shifts
    assert insertion_sort([4, 3, 2, 1])[1:] == (6, 6)
    # sorted list of 4 -> 3 comparisons, 0 shifts
    assert insertion_sort([1, 2, 3, 4])[1:] == (3, 0)


if __name__ == "__main__":
    test_sorts()
    test_counts_from_lecture()
    print("all tests passed")
