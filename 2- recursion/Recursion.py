# TODO: Demonstration of recursion

def binary_search(data, target, low, high):
    """Return ture if target found"""

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


marks = [2, 4, 5, 7, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

print(binary_search(marks, 27, 0, len(marks) - 1))


# factorial program
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
