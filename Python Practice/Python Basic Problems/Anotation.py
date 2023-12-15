def check_anno(name:str) -> str:
    return f"Hello {name}"

print(check_anno("Harshal"))


# Alternate method

def check_ano(name:str,age:int)->str:
    return f"Hello {name} my age is {age}" 

# print(check_ano.__annotations__)
xy = check_ano("Harshal" , 21)
print(xy)