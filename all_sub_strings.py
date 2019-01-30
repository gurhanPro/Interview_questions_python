#uglier for quicker - list comprehension
def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]
  
  
def sol(s):
    ls = len(s)
    k = []
    for i in range(ls):
        for j in range(i,ls):
            print i,j
            k.append(s[i:j+1])
            print s[i:j+1]
    print sorted(k)         # sorted alphapeticaly
    k.sort(key = lambda s: len(s)) # sorted the string list in length
    print k
    print(max(k))
sol("abc")
