#given an array A consisting of N integers, returns the number of distinct values in array A.


from collections import defaultdict
def solution(a):
    d = defaultdict(int)
    
    for i in a:
        d[i] +=1
   
    distinct = len(d
    
    return distinct

