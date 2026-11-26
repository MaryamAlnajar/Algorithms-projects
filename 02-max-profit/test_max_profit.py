import random
from max_profit import linear_scan, divide_and_conquer


def brute_force(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


def test_example():
    prices = [7, 1, 5, 3, 6, 4]
    assert linear_scan(prices) == (5, 1, 4)
    assert divide_and_conquer(prices) == (5, 1, 4)


def test_prices_only_go_down():
    prices = [9, 7, 5, 3, 1]
    assert linear_scan(prices)[0] == 0
    assert divide_and_conquer(prices)[0] == 0


def test_small_inputs():
    assert linear_scan([])[0] == 0
    assert divide_and_conquer([])[0] == 0
    assert divide_and_conquer([5])[0] == 0


def test_random_against_brute_force():
    for _ in range(200):
        prices = [random.randint(1, 50) for _ in range(random.randint(0, 30))]
        expected = brute_force(prices)
        assert linear_scan(prices)[0] == expected
        assert divide_and_conquer(prices)[0] == expected


if __name__ == "__main__":
    test_example()
    test_prices_only_go_down()
    test_small_inputs()
    test_random_against_brute_force()
    print("all tests passed")
