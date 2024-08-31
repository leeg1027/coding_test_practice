def solution(arr1, arr2):
    result = [[[] for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    arr_sum = 0
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                arr_sum += arr1[i][k]*arr2[k][j]
            result[i][j] = arr_sum
            arr_sum = 0
                
    return result