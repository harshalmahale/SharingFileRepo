def deco(func):
    def inner():
        print("Excecuting now")
        func()
        print("Exceuted")
    return inner
@deco 
def who_is_harsh():
    print("harsh is smart boy")
# who_is_harshal = deco(who_is_harshal)
who_is_harsh()