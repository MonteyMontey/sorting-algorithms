from copy import deepcopy

                
def bubblesort(integer_list):
    for i in range (len(integer_list)-1): #2
        index = 0 #1
        for j in range(len(integer_list)-1): #2
            if integer_list[index] > integer_list[index+1]: #4
                first_number = deepcopy(integer_list[index]) #3
                integer_list[index] = integer_list[index+1] #3
                integer_list[index+1] = first_number #3
            index += 1 #1
    return integer_list #1



"""
RUNTIME COMPLEXITY

To keep it simple I count each allocation, function call and operation as
one "unit of effort". At the end of each line I write down the total number of
"units of efforts" the line contains.

n = length of list

WORST CASE: 
O(n) = 2 + (n-1) * (1 + 2 + ((n-1)*4 + 3 + 3 +3 +1)) +1
     = 3 + (n-1) * (3 + ((n-1)*4 + 10)
     = 3 + (n-1) * (4n + 9)
     = 3 + 4n^2 + 9n - 4n -9
     = 4n^2 + 5n -6
     ~ O(n^2) quadratic time 
"""

