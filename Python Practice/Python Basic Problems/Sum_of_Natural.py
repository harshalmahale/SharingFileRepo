def getsum(num):
    if num == 1:
        return 1
    return num + getsum(num-1)
num = 5
print(getsum(num))