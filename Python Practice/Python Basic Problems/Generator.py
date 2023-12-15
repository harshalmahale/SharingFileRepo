# Square of Number
def my_gen(n):
    for nums in range(1,n+1):
        yield nums*nums
    
my_generator = my_gen(5)
for nums in my_generator:
    x = nums
print(x)
    
# Print 1 to 10

def gen():
    for num in range(1,11):
        yield num
        

my_gen = gen()
for num in my_gen:
    print(num)