'''
1247. Minimum Swaps to Make Strings Equal

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

"Solution Hint"

case 1:

if length of two strings are not equal:
    then then swapping is not possible

case 2 :

if there are 2 pairs of x_y or y_x i.e. x_y = 2 or y_x = 2: 
    then 1 swap is required to make string equal

case 3 :

if x_y and y_x pairs are not equal :
    then swapping is not possible

case 4 :

if there is 1 x_y and 1 y_x pair i.e x_y = 1 and y_x = 1:
    then 2 swaps are required to make string equal

'''

def minimumSwap(s1,s2):
    
        if len(s1)!=len(s2): 
            return -1
        
        x_y=y_x=0
        
        for i in range(len(s1)):
            
            if s1[i]!=s2[i]:
                
                if s1[i]=='x':
                    x_y+=1
                else:
                    y_x += 1
        
        if (x_y+y_x)%2 != 0:
            return -1
        
        if x_y == y_x == 1:
            return 2
        
        else:
            
            ans = x_y//2 + y_x//2
            
            if x_y %2 != 0:
                ans+=2
                
        return ans

# print(minimumSwap("xyxyxx","yxyxyx"))