
def findCostForChip(data):
    oddCount = 0
    evenCount = 0
    for chip in data:
        if chip % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return min(oddCount, evenCount)



print(findCostForChip([2,2,2,3,3]))