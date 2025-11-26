class Customer:
    def __init__(self, name, pin, account):
        self.name = name
        self.pin = pin
        self.account = account

#Step1 Python sees 
  # class Customer
  # Python motice we are creating a new class named Customer
  # It prepares a structure to store its methods and attributes

#Step2 Python reads 
#__init__
# This is the constructor
# Python stores it inside the class
# def __init__(self, name, pin, bank_account):
# This method will run each time a Customer is created

#Step3 Python stores variable assignment lines
# self.name = name
# self.pin = pin
# self.bank_account = bank_account

#Step4 Class definition is complete

# When we create a customer
# Customer("Alice", "1234", BankAccount(100))

# Python does.
  #1 Allocate memory for a new Customer

  #2 Call
    # __init__(self, "Alice", "1234", BankAccountObject)

  #3 Set attributes
    # self.name = "Alice"
    # self.pin = "1234"
    # self.bank_account = BankAccountObject

    # A complete customer object is ready 


