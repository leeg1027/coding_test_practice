def solution(prices):
    result = [0]*len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                result[i] = j-i
                break
        result[i] = j-i
    return result