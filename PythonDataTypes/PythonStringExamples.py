#split strings based on a charecter

def splitString(inputString, splitChar = ' '):
    return inputString.split(splitChar)

print(splitString("abc,def,ghi", ','))
print(splitString("qwe@rty@uio", '@'))
print(splitString("abc def ghi"))

