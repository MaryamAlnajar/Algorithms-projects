# Max Profit Finder

Mini project for CS314, lecture 2 (divide and conquer).

Given daily stock prices, find the best day to buy and the best day to sell later.
I solved it two ways and compared them:

1. **Linear scan**: keep the lowest price seen so far. O(n).
2. **Divide and conquer**: turn prices into daily changes and find the maximum subarray
   (left half, right half, or crossing the middle). O(n log n).

## How to run

```
python main.py
python test_max_profit.py
```

`main.py` reads `prices.csv` (1000 days of made-up prices) and prints the answer from both methods.
No libraries are needed.

## Results

On `prices.csv` both methods give profit 51.84 (buy on day 69, sell on day 196).

| n | linear scan | divide and conquer |
|---|---|---|
| 10,000 | 0.0005 s | 0.016 s |
| 100,000 | 0.005 s | 0.17 s |
| 500,000 | 0.027 s | 0.87 s |

## Notes

- Both methods always agree. The tests compare them with a brute-force O(n²) check on 200 random lists.
- If the price only goes down the profit is 0 (no trade).
- The linear scan is simpler and faster here. Divide and conquer is still a good way to
  practice the idea, and the same "left / right / crossing" pattern works for other problems.
