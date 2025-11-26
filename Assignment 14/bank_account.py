class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance


#Step 1 Python reads the class header
     # Creates a blueprint named BankAccount

#Step 2 Reads __init__
    # Stores the constructor 
    # Create self.balance

#Step 3 Reads deposite and stores its code
    # Adds money to the accont 

#step 4 REads withdraw and stores its code
    # Checks if enough money exits
    # Subtracts and return True or Flase

# When we create a banl account
# BankAccount(100)

# Python runs:
    #__init__(self, 100)
    #self.balance = 100
