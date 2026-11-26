from islands import count_islands


def test_example():
    assert count_islands(["11000", "11000", "00100", "00011"]) == 3


def test_empty_and_all_water():
    assert count_islands([]) == 0
    assert count_islands(["000", "000"]) == 0


def test_all_land_is_one_island():
    assert count_islands(["111", "111"]) == 1


def test_diagonal_does_not_connect():
    assert count_islands(["10", "01"]) == 2


def test_single_cell():
    assert count_islands(["1"]) == 1
    assert count_islands(["0"]) == 0


def test_snake_shape():
    # one long winding island, would break a recursive version on big inputs
    assert count_islands(["11111", "00001", "11111", "10000", "11111"]) == 1


if __name__ == "__main__":
    test_example()
    test_empty_and_all_water()
    test_all_land_is_one_island()
    test_diagonal_does_not_connect()
    test_single_cell()
    test_snake_shape()
    print("all tests passed")
