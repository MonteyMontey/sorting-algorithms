import random

def merge(sorted_list_a,sorted_list_b): #total 7n + 9 (where n equals length of shortest list)
    new_list = [] #1
    
    while len(sorted_list_a) > 0 and len(sorted_list_b) > 0: #4
        
        if sorted_list_a[0] <= sorted_list_b[0]: #3
            element = sorted_list_a[0] #2
            new_list.append(element) #1
            sorted_list_a.remove(element) #1
        else:
            element = sorted_list_b[0] #2
            new_list.append(element) #1
            sorted_list_b.remove(element) #1

    if len(sorted_list_a) > 0: #2
        new_list += sorted_list_a #1
    else:
        new_list += sorted_list_b #1

    return new_list #1



def mergesort(integer_list):
    if len(integer_list) <= 1: #2
        return integer_list #1
    else:
        mid = len(integer_list) // 2 #3
        left_side = integer_list[:mid] #2
        right_side = integer_list[mid:] #2

    return merge(mergesort(left_side), mergesort(right_side)) 
        



"""
RUNTIME COMPLEXITY

To keep it simple I count each allocation, function call and operation as
one "unit of effort". At the end of each line I write down the total number of
"units of efforts" the line contains.

n = length of list

WORST CASE: (which is basically average case and best case as well) 
O(n) = 3 + 2 + 2 + (7n + 9) * (log n * (3 + 2 + 2)* 2)
     = 7 + (7n + 9) * (log n * 14)
     ~ n * log n (quasilinear time)
"""



    


                     

   
