def solution(a,b,k):
    m = ((a +k -1)//k)*k
    
    if m > b:
        return 0
    else:
        return ((b-m)//k)+1
