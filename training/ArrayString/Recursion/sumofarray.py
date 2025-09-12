import cProfile


def sumOfArray(arr: list) -> int:
    if len(arr) == 0:
        return 0

    print(f"arr[0]={arr[0]} | arr = {arr}")
    return arr[0] + sumOfArray(arr[1:])


array = [i for i in range(1, 800)]

# print(sumOfArray(array))
cProfile.run("sumOfArray(array)")
