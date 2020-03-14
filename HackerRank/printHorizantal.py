'''
Given binary tree

                        8
                   /         \
                  3            10                        
                /  \             \
               1    6               14
                   / \             /
                  4     7        13


print horizantal nodes [ [8], [3,10], [1,6,14], [4,7,13] ]
'''


#Node definition
class Node:
    
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None

# Node insertion
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

r = Node(8) 
insert(r,Node(3)) 
insert(r,Node(10)) 
insert(r,Node(1)) 
insert(r,Node(6)) 
insert(r,Node(14)) 
insert(r,Node(4))
insert(r,Node(7)) 
insert(r,Node(13))


def find_temps(nde):
    nxt_nodes = []
    if nde.left is not None:
        nxt_nodes.append(nde.left)
    if nde.right is not None:
        nxt_nodes.append(nde.right)
    return nxt_nodes

def print_horizantol_order(root): 
    if root is None: 
        return []
    
    final_list = []
    temp = [root]
    
    while len(temp) > 0:
        lst = []
        t_temp = []
        
        for n in temp:
            lst.append(n.val)
            n_nodes = find_temps(n)
            t_temp.extend(n_nodes)
            
        final_list.append(lst)
        temp = t_temp
    return final_list

print(print_horizantol_order(r))


#Ans is [[8], [3, 10], [1, 6, 14], [4, 7, 13]]