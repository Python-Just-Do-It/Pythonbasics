def minStringSwap(s1, s2):
    xVariableCount = 0
    yVariableCount = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] == "x":
            xVariableCount += 1
        if s1[i] != s2[i] and s1[i] == "y":
            yVariableCount += 1
    
    xUniqueSwapCount = xVariableCount // 2
    yUniqueSwapCount = yVariableCount // 2
    remianingVariableSwapCount = 2 * (xVariableCount % 2)
    return(xUniqueSwapCount + yUniqueSwapCount + remianingVariableSwapCount)

print(minStringSwap("xxyyxyxyxx", "xyyxyxxxyx"))
print(minStringSwap("xxyyxyxyxxxyxyx", "xyyxyxxxyxyxyxy"))
