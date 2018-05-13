import random

def quicksort(integer_list):
    
    if len(integer_list) < 2: #2
        return integer_list #1
    
    pivot_element = random.choice(integer_list) #2
    smaller, greater, equal = [], [], [] #3
    
    for i in integer_list:
        if i < pivot_element: #1
           smaller.append(i) #1
        elif i == pivot_element: #1
            equal.append(i) #1
        else:
            greater.append(i) #1

    return quicksort(smaller) + equal + quicksort(greater)  #5
 


"""
RUNTIME COMPLEXITY

To keep it simple I count each allocation, function call and operation as
one "unit of effort". At the end of each line I write down the total number of
"units of efforts" the line contains.

n = length of list

WORST CASE: (if pivot element is always the smallest element in the list)
O(n) = (n-1) * (2 + 2 + 3 + n*3 + 5) + 3
     = (n-1) * (3n + 12) + 3
     = 3 n^2 + 12n - 3n - 9
     = 3 n^2 + 9n - 9
     ~ O(n^2) quadratic time

BEST CASE: (if pivot element divides the list always in half)
O(n) = (log n) * (2 + 2 + 3 +3 + (n/2 * 2) + (n/2 * 3) + 5 + 3) (log n because loop is being executed n, n/2, n/4 ... times)
     = (log n) * (18 + n + n/2 * 3)
     ~ n(log n) quasilinear time
"""
