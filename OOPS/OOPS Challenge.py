class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,d_amount):
        self.balance = self.balance + d_amount
        print("money has been deposited")

    def withdrawal(self,w_amount):
        if self.balance >= w_amount:
            self.balance = self.balance - w_amount
            print("withdrawal accepted")
        else:
            
            print("Funds Unavailable")

    '''def withdrawal(self,w_amount):
        if w_amount > self.balance:
            
            print("Funds Unavailable")
        else:
            self.balance = self.balance - w_amount
            print("withdrawal accepted")'''
    

    def __str__(self):
        return f"Account Owner = {self.owner}\nAccount Balance = {self.balance}"



acct1 = BankAccount('Mike',100)
print(acct1)
#print(acct1.owner)
#print(acct1.balance)
acct1.deposit(200)
print(acct1)
acct1.withdrawal(100)
print(acct1)
acct1.withdrawal(200)
print(acct1)
acct1.withdrawal(0)


