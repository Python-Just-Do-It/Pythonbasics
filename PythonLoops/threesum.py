'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def threeSum(arr):
    
    l = len(arr)
    
    first = 0
    
    uni = []

    while first < l:
            
            for second in range(l):
                
                for third in range(l):
                    
                    if first != second:
                        
                        if (third != first) and (third != second):

                            a= [arr[first] , arr[second], arr[third]]
                            a.sort()
                           
                            if a not in uni:

                                add = arr[first] + arr[second] +  arr[third]
                                
                                if add == 0:
                                    
                                    uni.append(a)
            first += 1
            
    return uni
        
         
#time complexity is more for this solution
        
arr = [-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1]            
print(threeSum(arr)) 
            
    
    
