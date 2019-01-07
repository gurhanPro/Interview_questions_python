A, C, G , T = 1, 2, 3 , 4
#d = {'A':1, 'C':2, 'G':3, 'T':4}
#s ,p,q= "AC" , [0, 0, 1], [0, 1, 1]
s ,p,q= "CAGCCTA" , [2, 5, 0], [4, 5, 6]

def sol(s,p,q):
    d = {'A':1, 'C':2, 'G':3, 'T':4}
    result = []
    sliced = []
    lenghts = []
    for i,j in zip(p,q):
        if j == i:
            k = s[i]
        else:
            k = (s[i:j+1])
        print k +"\n"
        sliced.append(k)
        lenghts.append(len(k))
    print sliced
    print lenghts
    for m in k:
        hh = d[k[0]]  
        hh=min(hh,d[m])
        result.append(hh)
    print result
# [1,1,2]
#[2, 4, 1]
sol(s,p,q)
#A AC C [1, 2, 2]        
