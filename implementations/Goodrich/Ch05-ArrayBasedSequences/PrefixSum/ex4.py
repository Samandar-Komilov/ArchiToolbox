# Given array A and integer K, check if any subarray sum is divisible by K.

arr = [1,2,3,4,7,32,66,23,15,98,54,22]


def get_cumulative_sums(arr: list) -> list | None:
    # In-place
    ln = len(arr)
    if (ln <= 0):
        print("Array size should be positive.")
    
    prefixSum = [None] * ln
    prefixSum[0] = arr[0]

    for i in range(1, ln):
        prefixSum[i] = prefixSum[i-1] + arr[i]
    
    return prefixSum

prf = get_cumulative_sums(arr)

print(prf)