#fibonacci longest
def lenLongestFibSubseq(arr):
    from collections import defaultdict
    max_len = 0
    dp = defaultdict(lambda: 2)
    num_set = set(arr)
    
    for j in range(1, len(arr)):
        for i in range(j):
            a, b = arr[i], arr[j]
            expected = b - a
            if expected < a and expected in num_set:
                dp[(a, b)] = dp.get((expected, a), 2) + 1
                max_len = max(max_len, dp[(a, b)])
    
    return max_len if max_len > 2 else 0
