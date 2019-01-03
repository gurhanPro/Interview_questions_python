# given a list of intergers and a target number, write a function 
#that returns a boolean indicating if its possible to sum two ingergs from the list ot reach the target number
def sol(arr,tar):
    seen = set()
    for num in arr:
        num2 = tar - num
        if num2 in seen:
            print("{} = {} + {}".format(tar,num,num2))
            return True
        seen.add(num)
    print(seen)
    return False
