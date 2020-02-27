def swapElementsInArray(arr):
    firstIndex = 0
    lastIndex = len(arr) - 1
    if lastIndex > 0 :
        while firstIndex < lastIndex:
            temp = arr[firstIndex]
            arr[firstIndex] = arr[lastIndex]
            arr[lastIndex] = temp
            firstIndex += 1
            lastIndex -= 1
    return arr


arrData = [1,2,3,4,5,6,7,8,9,10]
print(swapElementsInArray(arrData))