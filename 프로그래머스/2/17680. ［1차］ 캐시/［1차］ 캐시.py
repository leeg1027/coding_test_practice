def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    result = 5
    x = []
    for i in cities:
        x.append(i.lower())
        
    array = [x[0]]
    
    for i in range(1, len(x)):
        if x[i] not in array:
            array.append(x[i])
            if len(array) > cacheSize:
                array.pop(0)
            result += 5
        else:
            array.remove(x[i])
            array.append(x[i])
            result += 1
    return result