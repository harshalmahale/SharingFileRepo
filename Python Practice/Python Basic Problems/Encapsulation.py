class BankAccount:
    def __init__(self,acc_no,balance):
        self._acc_no = acc_no
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance = self.__balance + amount
    
    def withdraw(self,amount):
        if (self.__balance>=amount):
            self.__balance = self.__balance - amount
        
        else:
            print("Insufficient Balance")
        
    def display_Acc_info(self):
        print(f"Balance is :{self.__balance}")
        print(f"Account No. is : {self._acc_no}")
        
        
bnk_amt = BankAccount("123456789", 190000)

bnk_amt.deposit(500)
bnk_amt.withdraw(200)
bnk_amt.display_Acc_info()
