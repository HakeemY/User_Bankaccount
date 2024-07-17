class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate 
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds")
            return self
        # withdraw(self, amount) 
        # - decreases the account balance by the given amount if there are sufficient funds; 
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        
    def display_account_info(self):
            print(f"Current account balance: ${self.balance}.")
            return self
    
    def yield_interest(self):
        if self.balance > 0:
           self.balance += self.balance * self.int_rate
        return self
        
class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0 )

    def make_deposit(self, amount):
    # Call the deposit method of the associated bank account
        self.account.deposit(amount)
        return self

    def make_withdrawal (self, amount):
    # Call the withdrawal  method of the associated bank account
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self

    def transfer_money(self, amount, other_user):
        #giving  account decrease by amount
        self.make_withdrawal(amount)
        #receiving account increases by amount
        other_user.make_deposit(amount)
        return self

user1 = User("hakeem", "hakeem@gmail.com")
user2 = User("boyle", "boyle@gmail.com" )
user3 = User("antonie", "antonie@gmail.com")

user1.make_deposit(100000).display_user_balance().transfer_money(1,user3)

user3.display_user_balance()