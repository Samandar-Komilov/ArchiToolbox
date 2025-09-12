# Given an array A, construct its prefix sum array P such that P[i] = A[0] + A[1] + ... + A[i].

arr = [1, 2, 3, 4, 5, 10, 11]


def get_prefix_sum(arr: list) -> list:
    ln = len(arr)
    prefixSum = [None] * ln
    prefixSum[0] = arr[0]

    for i in range(1, ln):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    return prefixSum


prefixSum = get_prefix_sum(arr)

# Find the sum of subarray[i,j]

start, end = map(int, input().split())

print("Prefix Sum:", prefixSum)
print(prefixSum[end - 1] - prefixSum[start - 1])


"""Analysis
Brute-Force approach is slow - O(n) per query. It means, every time user wants to see the cumulative sum of some subarray, we have to iterate.
Prefix Sum approach is fast, but with the cost of extra space (O(n)): every time user wants to see the cumulative sum of some subarray, we simply subtract the respective indexed prefixSum array elements.
"""
