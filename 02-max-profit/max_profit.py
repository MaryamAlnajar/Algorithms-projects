def linear_scan(prices):
    """Best buy/sell days by remembering the lowest price so far. O(n)."""
    best_profit = 0
    buy_day = sell_day = None
    low_day = 0
    for day in range(1, len(prices)):
        if prices[day] < prices[low_day]:
            low_day = day
        profit = prices[day] - prices[low_day]
        if profit > best_profit:
            best_profit = profit
            buy_day, sell_day = low_day, day
    return best_profit, buy_day, sell_day


def crossing(diff, low, mid, high):
    """Best subarray of diff that crosses the middle."""
    left_sum = float("-inf")
    total = 0
    left_index = mid
    for i in range(mid, low - 1, -1):
        total += diff[i]
        if total > left_sum:
            left_sum = total
            left_index = i

    right_sum = float("-inf")
    total = 0
    right_index = mid + 1
    for j in range(mid + 1, high + 1):
        total += diff[j]
        if total > right_sum:
            right_sum = total
            right_index = j
    return left_index, right_index, left_sum + right_sum


def max_subarray(diff, low, high):
    if low == high:
        return low, high, diff[low]
    mid = (low + high) // 2
    left = max_subarray(diff, low, mid)
    right = max_subarray(diff, mid + 1, high)
    cross = crossing(diff, low, mid, high)
    return max(left, right, cross, key=lambda x: x[2])


def divide_and_conquer(prices):
    """Same answer using divide and conquer on the daily price changes. O(n log n)."""
    if len(prices) < 2:
        return 0, None, None
    diff = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    low, high, total = max_subarray(diff, 0, len(diff) - 1)
    if total <= 0:
        return 0, None, None
    # diff[i] is the change from day i to day i+1
    return total, low, high + 1
