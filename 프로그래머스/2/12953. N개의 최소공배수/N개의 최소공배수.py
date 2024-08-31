def solution(arr):
    import math
    result = int(arr[0]*arr[1]/math.gcd(arr[0], arr[1]))
    for i in range(2, len(arr)):
        result = int(result*arr[i]/math.gcd(result, arr[i]))
    return result
    