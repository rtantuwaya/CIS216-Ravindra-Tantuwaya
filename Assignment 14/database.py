# Step1  creating a new class called Database
class Database:
    # A class is a blueprint to create objects

# Step 2  # the constructor method __init__
    def __init__(self): 
        # stores a method named __init__.
        # This method will run automatically every time we create a Database object.
        self.customers = {}  # card_number  Customer
        # create an empty dictionary to store customers

# Step 3  Python reads the add_customer method
    def add_customer(self, card_number, customer):
        # Python stores another method in the class
        self.customers[card_number] = customer
        # Put a customer object into the dictionary using the card number as the key

# Step 4  Python reads the get_customer method
    def get_customer(self, card_number):
        # stores this method too
        return self.customers.get(card_number)
    # This method returns

# run from gui.py
# db = Database()

# Step1 create a new Database object.

# Step2 python automatically calls the constructor  
# __init__(self)

# Step3 inside __init__, Python creates
# self.customers = {}

# the database is now empty

#========================#
# Exampe If we add a cusomer
# db.add_customer("1111", CustomerObject)

#step1 Python calls.
#  add_customer(self, "1111", CustomerObject)

#step2 inside the method
#  self.customers["1111"] = CustomerObject

#step3 The database now contains
# {"1111": CustomerObject}

#========================#
# Example if we get customer
# db.get_customer(current_card)
# db.get_customer(1111)

#step1 python looks inside the dictionary
#Step2 Find "1111" key
#Step3 Retrun the stored Customer object





