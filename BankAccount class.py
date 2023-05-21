class BankAccount:
    def __init__(self, cus_name, account_number, balance, date):
        self.cus_name = cus_name
        self.account_number = account_number
        self.balance = balance
        self.date = date
        
        
    def deposit(self, new):
       self.balance = self.balance + new
       return self.balance
        
        
    def withdraw (self, w):
       self.balance = self.balance - w
       return self.balance

        
    def chack_balance(self):
            return self.balance
        
ac1 = BankAccount("Maather", 13246355, 2000, "13-01-2024")
print("Balance:", ac1.chack_balance())
ac1.deposit( 300)
print("After deposit", ac1.chack_balance())
ac1.withdraw( 100)
print("After withdraw", ac1.chack_balance())

            
            
            

        