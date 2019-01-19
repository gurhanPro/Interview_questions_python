""" Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros
. Your list of queries is as follows: 
    a b k
    1 5 3
    4 8 7
    6 9 1
    Add the values of k between the indices a and b inclusive:
    
 index->	 1 2 3  4  5 6 7 8 9 10
          [0,0,0, 0, 0,0,0,0,0, 0]
          [3,3,3, 3, 3,0,0,0,0, 0]
          [3,3,3,10,10,7,7,7,0, 0]
          [3,3,3,10,10,8,8,8,1, 0]
          
   The largest value is 10 after all operations are performed. 
   
   
Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

    n - the number of elements in your array
    queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
"""

def arrayManipulation(n, d):
    arr = [0]*(n+2) # initializing my empty array with zeroes, n+2 is to avoid array of out range later when I am updating
    
    for a in d:
        # initializing the first index and last plus one index further of the range, and then the value 
        first ,last,value= a[0] ,a[1]+1,a[2]
        
        # updating the start index which is i and end index which is k+1
        arr[first]+=value
        arr[last] = arr[last]-value
        
    # converting the array to prefix sum
    for i in range(1,len(arr)-1):
        arr[i] = arr[i] + arr[i-1]

    return max(arr)
