# Find the starting index of the minimal average of any slice containing at least two elements.

def sol(a):
    l = len(a)
    minA = (a[0] + a[1])/2.0
    idx = 0
    for i in range(0,l):
        if i < l-2:
            
            av1 = (a[i] + a[i+1]+ a[i+2])/3.0
            av2 = (a[i] + a[i+1])/2.0
            if av1 < minA:
                idx = i
            elif av2 < minA:
                idx = i
            
            minA = min(minA,av1,av2)
    return idx
