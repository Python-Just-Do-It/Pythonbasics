'''
1217.Play with Chips

There are some chips, and the i-th chip is at position chips[i].

You can perform any of the two following types of moves any number of times (possibly zero) on any chip:

    Move the i-th chip by 2 units to the left or to the right with a cost of 0.
    Move the i-th chip by 1 unit to the left or to the right with a cost of 1.

There can be two or more chips at the same position initially.

Return the minimum cost needed to move all the chips to the same position (any position).

#example 1
Input: chips = [1,2,3]
Output: 1
Explanation: Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
'''

'''
Success
Details
Runtime: 100 ms, faster than 5.80% of Python3 online submissions for Play with Chips.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Play with Chips.

'''

def calculateCostBetweenPositions(num):
    
        if num == 1:
            return 1
        elif num == 2:
            return 0
        else:
            return num%2
        
def minCostToMoveChips(chips):
    
    l_chips = len(chips)

    se = list(set(chips))

    l_set = len(se)

    cost = []

    ini_set = 0

    while ini_set < l_set:

        ic = 0
        val = se[ini_set]

        for chip_position in range(l_chips): 

            if chips[chip_position] != val :

                dif = abs(chips[chip_position] - val)

                cs = calculateCostBetweenPositions(dif)
                ic += cs

        cost.append(ic)

        ini_set +=1

    return min(cost)

print(minCostToMoveChips([2,2,3,4,5]))