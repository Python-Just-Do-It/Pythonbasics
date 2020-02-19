def countIsUpperAndLower(s):
    upperCaseCount = 0
    lowerCaseCount = 0
    for char in s:
        if char.isupper():
            upperCaseCount += 1
        elif char.islower():
            lowerCaseCount += 1
        else:
            print("Invalid Charecter")
    return(upperCaseCount, lowerCaseCount)
    
print(countIsUpperAndLower("abcDEFGHI"))