def to_power(nums,*args):
    if args:
        return[i**nums for i in args]
    else:
        return "you didn't pass any args"
        
nums = [2,3,4]
print(to_power(3,*[2,3]))