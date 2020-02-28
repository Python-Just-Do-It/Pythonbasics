'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''

def crossProduct(ar1, ar2):
    ans = []
    for i in ar1:
        for j in ar2:
            ans.append(i+j)
    return ans

def func(nums):

    kv_dct = {"2": ['a','b','c'] ,
               "3": ['d','e','f'],
               "4": ['g','h','i'],
               "5": ['j','k','l'],
               "6": ['m','n','o'],
               "7": ['p','q','r','s'],
               "8": ['t','u','v'],
               "9": ['w','x','y','z']}
    
    if len(nums) == 1:
        if nums[0] in kv_dct:
            return kv_dct[nums[0]]
        
    elif len(nums) == 0:
            return ""
        
    for i in nums: 
        if i not in kv_dct:
            return "oops!! input is incorrect"
    
        
    keys = [kv_dct[i] for i in nums if i in kv_dct]
        
    l_keys = len(keys)
    
    while len(keys) != 0 :
        
        if len(keys) == l_keys:
            ch_ar = crossProduct(keys[0],keys[1])
            keys.pop(0)
            keys.pop(0)
            
        else:
            ch_ar = crossProduct(ch_ar,keys[0])
            keys.pop(0)
            
    return ch_ar

print(func("2356"))
