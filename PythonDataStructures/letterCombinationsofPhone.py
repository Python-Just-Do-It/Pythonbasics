from collections import deque 
  

def letterCombinationsGenerator(number, length, table): 
  
    resultList = [] 
    q = deque() 
    q.append("") 
  
    while len(q) != 0: 
        s = q.pop() 
  
        # If complete word is generated 
        # push it in the list 
        if len(s) == length: 
            resultList.append(s) 
        else: 
            # Try all possible letters for current digit 
            # in number[] 
            localLengthVariable =  len(s)
            arrValueAtIndex = number[localLengthVariable]
            value = table[arrValueAtIndex]

            for letter in value: 
                q.append(s + letter) 
  
    # Return the generated list 
    return resultList

def letterCombinations(inputString): 
  
    # table[i] stores all characters that  
    # corresponds to ith digit in phone 
    table = ["", "", "abc", "def", "ghi", "jkl", 
            "mno", "pqrs", "tuv", "wxyz"]
    inputArray = []
    for i in range(len(inputString)):
        inputArray.append(int(inputString[i]))
    list = letterCombinationsGenerator(inputArray, len(inputArray), table) 
  
    resultString = "" 
    for word in list: 
        resultString += word + " "
    return resultString


print(letterCombinations("23"))