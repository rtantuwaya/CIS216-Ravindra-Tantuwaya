class ATM:
 # Step 1 Python sees class ATM
    # Sets up ATM class blueprint
    def __init__(self, database, security, logger=None):
    #Step 2 Read __init__ Thos constructor expects
        self.db = database
        # a Database object
        self.security = security
        # a Security object
        self.logger = logger
        # a Logger object
 
    def _log(self, msg):
        if self.logger:
            self.logger.log(msg)

    #Step 3 Read  authenticate method
    def authenticate(self, card_number, pin):
        customer = self.db.get_customer(card_number)
        if not customer:
            return False
        
        valid = self.security.validate_pin(card_number, pin, customer.pin)
        self._log(f"Authentication attempt for {card_number}: {valid}")
        return valid

    #Step 4 Read  check_balance method
    def check_balance(self, card_number):
        customer = self.db.get_customer(card_number)
        return customer.account.get_balance()

    #Step 5 Read  deposit method
    def deposit(self, card_number, amount):
        customer = self.db.get_customer(card_number)
        customer.account.deposit(amount)
        self._log(f"Deposit: {amount} to {card_number}")

    #Step 6 Read  withdraw method
    def withdraw(self, card_number, amount):
        customer = self.db.get_customer(card_number)
        success = customer.account.withdraw(amount)
        self._log(f"Withdraw: {amount} from {card_number} success={success}")
        return success


# When we create the ATM object
# atm = ATM(db, security, logger)

# 1 Create a new ATM object
# 2 calls 
        # __init__(self, db, security, logger)
 
# Sets.
    #self.db = db
    #self.security = security
    #self.logger = logger

# The ATM now has
    # access to the customer database
    # security check
    # ability to log
    # ability to modify balances