def get_bucket(number, position): #total 11
    number = str(number) #2
    if len(number) < position: #2
        return 0 #1
    else:
        bucket = int(number[len(number) - position]) #5
        return bucket #1


def bucketsort(integer_list):
    largest_number = max(integer_list) #2
    counter = 1 #1

    for i in range(len(str(largest_number))): #3
        bucket_list = [[],[],[],[],[],[],[],[],[],[]] #1
        
        for integer in integer_list:
            bucket = get_bucket(integer, counter) #12
            bucket_list[bucket].append(integer) #2

        counter += 1 #1
        integer_list.clear() #1
        for j in range(10):
            integer_list += bucket_list[j] #2
            
    return integer_list #1


"""
RUNTIME COMPLEXITY

To keep it simple I count each allocation, function call and operation as
one "unit of effort". At the end of each line I write down the total number of
"units of efforts" the line contains.

n = length of list
m = digits of largest number

AVERAGE CASE: 
O(n, m) = 3 + 3 + m * (1 + n*(12+2) + 1 +1 + 10*2) + 1
        = 7 + m*( 23 + 14n)
        = 7 + 23m + 14mn
        ~ (O)m*n (in my case)

"""

