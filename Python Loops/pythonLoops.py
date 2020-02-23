# Data types in python
# 5, 6, 10 - int

# LIMIT - 2^31 - 1

# long 2 ^ 64 - 1

# String
# "Teja"

# floating numbers

# float, decimal
# 5 / 6 - 0.8

# Character Data type
# Sting consists of group of characters.

# 'a', 'b'

# varchar
# variable string
# [2,3,4] - list
# tuple in python -  (2,3,4) - Immutable

# list
# [1, 2, 3, 3, 2]
# it does store duplicates

# set 
# important points
# doesn't store duplicate
# Set([1,2,3,3,2]) - 1, 2, 3

# dictionary / map
# key value pair
# Kohli - 15, Rohit - 20
# {"Kohli" : 15, "Rohit" : 20}

# Mutability and Immutability                          Not possible
# (1, 2, "Hello", [1,2,3]) -> (1, 2, "Hello", [1,2,3,4]) -*>    (1, 2, "Hello", [1,2,3,4], 25.6)
# (#1, #2,)

#
# {name : [id, address, marks]}
#  bad design 
# {name : id}, {name : address}, {name : marks}
# [{name : "Yashwanth", id : 24, "address" : "California", "marks" : 70, "interests" : ["nba", "sports"], {{name : "Viswanth", id : 26, "address" : "Texas", "marks" : 70, "interest"}}]
# incrementMarks() - only applies on students
#  
# for each student I want to store - name, id, address, marks
# 
# classes in python

# Loops
# for loop and while loop

# for loop 
# Case 1 : Let's say you want the code for 100 times - for loop
# Case 2: Let's say you want to run until certain time/ condition is true - while loop

# for loop example:
# looping through an array - loop as many times as number of elements in the list - len(list)

# while loop
# run some code until certain is true
# val = true;
# 
# Find out the largest number starting from 1 where until upto number sum is 5054 or less.
# Let's say that largest number ix x, [1, x] <= 5054
# 1,2,3,.. x -> sum is less than 5054
# 

# 10
# 1, 2, 3, 4
# answer is 4.
def test():
    maxSum = 5054
    sum = 0
    i = 0
    while(sum <= maxSum): # runs when this condition true
        i += 1 # i = i + 1
        sum += i # sum = sum + i
    return i-1

#print(test())

def test1():
    sum = 0
    maxSum = 5054
    for i in range(1, 5055):
        if(sum == maxSum): 
            return i 
        if sum > maxSum:
            return i - 2
        else:    
            sum += i   
    return -1     
print(test1())        

# 101 - 101 * 51 - 5151
# answer should be 100







