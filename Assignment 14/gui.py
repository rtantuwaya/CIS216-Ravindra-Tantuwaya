#Step 1 Imports
import tkinter as tk
from tkinter import messagebox
from bank_account import BankAccount
from customer import Customer
from database import Database
from security import Security
from logger import Logger
from atm import ATM

# Python loaded all modules andd class into memory
# tkinter is the GUI toolkit. messagebox allows pop-up messages.

# -----------------------------
# # Step 2 Setup Object
# -----------------------------
db = Database()
security = Security()
logger = Logger()
atm = ATM(db, security, logger)
# create a Object
# db = Database() database object to store customers.
# security = Security() security object for pin verification
# logger = Logger() logs actions like deposites or withdrawals.
# atm = ATM(db, security, logger) ATM object that connect db, security, and logger.

# Step 3 Add default customers
db.add_customer("1111", Customer("Alice", "1234", BankAccount(100)))
db.add_customer("2222", Customer("Bob", "5678", BankAccount(250)))
# Create BankAccount(100) for Alice
# Create Customer("Alice", "1234", BankAccount(100))
# Calls db.add_custom("1111", Customer("Alice", "1234", BankAccount(100)))
# Create BankAccount(100) for Bob
# Create Customer("Bob", "5678", BankAccount(250))
# Calls db.add_custom("1111", Customer("Bob", "5678", BankAccount(250)))

# add_customer("1111", CustomerObject)
# CustomerObject = Customer("Alice", "1234", BankAccount(100))
# Customer("Alice", "1234", BankAccount(100)) it will go to Customer class

# Step 4 Global Variable

current_card = None
# create a variable current_card in memory
# it will track the currently logged-in user


# -----------------------------
# GUI Windows
# -----------------------------

# Step 5 Function Definitions
#def main_menu(): 
#def add_customer_screen(): 
#def login_screen(): 
#def atm_menu(): 
#def deposit_screen(parent): 
#def withdraw_screen(parent):

#==============Step 1====main_menu()=======================
# Main menu
def main_menu():
    # Execution moves inside main_nemu
    # Step 1 
    window = tk.Tk()
    # Python creates the main application window
    # this is the root GUI window

    # Step 2
    window.title("ATM System")
    #Sets the window title bar text.

    # Step 3 Creates the “ATM Main Menu” label
    tk.Label(window, text="ATM Main Menu", font=("Arial", 16)).pack(pady=10)
    # Python creates a label widget.
    # .pack() places it in the window 

    # Step 4 Add “Add Customer” button
    tk.Button(window, text="Add Customer", width=20, command=lambda: [window.destroy(), add_customer_screen()]).pack(pady=5)
    # Python creates a button
    # The button's command destroys this window and open add_customer_screen()

    # Step 5 Add “Use ATM” button
    tk.Button(window, text="Use ATM", width=20, command=lambda: [window.destroy(), login_screen()]).pack(pady=5)
    # Causes login window to appear.

    # Step 6 Add "Exit" button
    tk.Button(window, text="Exit", width=20, command=window.destroy).pack(pady=5)
    # Destroys the window (close the program)

    # Step 7 
    window.mainloop()
    # Tkinter stop the program here
    # It waits for user interactions
    # Nothing else runs until user clicks a button

 #==============Step 2=============add_customer_screen()=================

# Add customer screen

# Step 1 Creates a new TK window
def add_customer_screen():
    window = tk.Tk()
    window.title("Add Customer")
    
# Step 2  Add labels
    tk.Label(window, text="Name:").grid(row=0, column=0)
    tk.Label(window, text="Card Number:").grid(row=1, column=0)
    tk.Label(window, text="PIN:").grid(row=2, column=0)
    tk.Label(window, text="Starting Balance:").grid(row=3, column=0)
# Python creates text fields: Name, Card Number, PIN, Balance

# Step 3 Create entry boxes
    name_entry = tk.Entry(window)
    card_entry = tk.Entry(window)
    pin_entry = tk.Entry(window)
    balance_entry = tk.Entry(window)
# Python creats empty text input boxes.

# Step 4 Place them using grid()
    name_entry.grid(row=0, column=1)
    card_entry.grid(row=1, column=1)
    pin_entry.grid(row=2, column=1)
    balance_entry.grid(row=3, column=1)
# .grid() positions each widget in row/column

# Step 5 Define a nested function
    def add_customer_action():
        # This function executes only when the user clicks "Add Customer"
        name = name_entry.get()
        card = card_entry.get()
        pin = pin_entry.get()
        balance = float(balance_entry.get()) # Converts balance to float.
        # Reads the text from the entry fields.

        db.add_customer(card, Customer(name, pin, BankAccount(balance)))
        # Create new Customer object 
        # Add customer to the database.
        messagebox.showinfo("Success", "Customer added!")
        # Show success message.
        window.destroy()
        # Close window
        main_menu()
        # open main menu again
        
# Step 6 Create the “Add Customer” button
    tk.Button(window, text="Add Customer", command=add_customer_action).grid(row=4, column=0, columnspan=2)
    # When clicked  runs add_customer_action

# Step 7 — window.mainloop()
    window.mainloop()
    # Waits for the user to finish entering data

#===================Step 3=====================login_screen()=================

# Login screen
def login_screen():
# Step 1 Create window
    window = tk.Tk()
    window.title("Customer Login")

# Step 2 Add labelsfor "Card Number" and "PIN"
    tk.Label(window, text="Card Number:").grid(row=0, column=0)
    tk.Label(window, text="PIN:").grid(row=1, column=0)
    
# Step 3 Create entry boxes
    card_entry = tk.Entry(window)
    pin_entry = tk.Entry(window, show="*")
    card_entry.grid(row=0, column=1)
    pin_entry.grid(row=1, column=1)

# Step 4 Define login_action()===  # Adds login button
    def login_action():
        # Called when login button is clicked
        global current_card
    #1 Get card and PIN
        card = card_entry.get()
        pin = pin_entry.get()
        
     #2 Calls atm.authenticate(card, pin)

     #3 checks authentication,
        if atm.authenticate(card, pin):
        # if authentication is True
            # Set current_card = card
            current_card = card
            window.destroy()
            # close login window
            
            atm_menu()
            # Opens ATM menu if login is successful
        else:
            messagebox.showerror("Error", "Invalid card or PIN.")

#Step 5 Create "Login" button
    tk.Button(window, text="Login", command=login_action).grid(row=2, column=0, columnspan=2)
  
# Step 6  Wait using mainloop
    window.mainloop()
    

#==================Step 4==============atm_menu()==============
# ATM Menu
def atm_menu(): # atm_menu Execution 
    # First Create window for ATM Menu
    window = tk.Tk()
    window.title("ATM Menu")

    # Step1 Get current customer
    customer = db.get_customer(current_card)

    # Step 2 Display Welcome Label
    tk.Label(window, text=f"Welcome, {customer.name}", font=("Arial", 14)).pack(pady=10)


    # Step 3 Creats buttons for Check Balance, Deposit, Withdraw, and Logout
        # 1 Check Balance === Shows a popup=======messagebox.showinfo()
    tk.Button(window, text="Check Balance", width=20, command=lambda: messagebox.showinfo("Balance", f"Balance: ${atm.check_balance(current_card)}")).pack(pady=5)

        # 2 Deposit =====Open====deposit_screen()
    tk.Button(window, text="Deposit", width=20, command=lambda: deposit_screen(window)).pack(pady=5)

        # 3 Withdraw=========Open=========withdraw_screen()==========
    tk.Button(window, text="Withdraw", width=20, command=lambda: withdraw_screen(window)).pack(pady=5)

        # 4 Logout==========Close=======[window.destroy(), main_menu()])===
    tk.Button(window, text="Logout", width=20, command=lambda: [window.destroy(), main_menu()]).pack(pady=5)

    # Show ATM menu with buttons: Check Balance, Deposit, Withdraw, Logout

    # Step 4 Wait for user
    window.mainloop()
    # It waits for user click in event loop

#====================Step 5==========deposit_screen()=============
# Deposit screen
# calls from Deposit buttons deposit_screen(window)
def deposit_screen(parent):
     # Step 1 Create popup window Deposit Money
    window = tk.Toplevel(parent)
    window.title("Deposit Money")

     # Step 2 Add “Deposit Amount” label
    tk.Label(window, text="Deposit Amount:").pack()

     # Step 3 Entry box for amount
    amount_entry = tk.Entry(window)
    amount_entry.pack()
    # Creates popup window attached to parent

    def deposit_action():
        # Depodit action
        amount = float(amount_entry.get())
        #read amount
        atm.deposit(current_card, amount)
        # update ATM balance
        messagebox.showinfo("Success", "Deposit complete!")
        # Shoe success message
        window.destroy()
        # Close popup

    tk.Button(window, text="Deposit", command=deposit_action).pack()

#====================Step 6=======withdraw_screen()============
# Withdraw screen
 # calls from Deposit buttons Withdraw withdraw_screen(window)
def withdraw_screen(parent):
    # 1 Create popup window Withdraw Money
    window = tk.Toplevel(parent)
    window.title("Withdraw Money")

    # 2 Add label and entry
    tk.Label(window, text="Withdraw Amount:").pack()
    amount_entry = tk.Entry(window)
    amount_entry.pack()
    # Creates popup window attached to parent

    # Step 3 Define withdraw_action():
    def withdraw_action():
         # Read amount
        amount = float(amount_entry.get())

         # Calls atm.withdraw(current_card, amount)
        if atm.withdraw(current_card, amount):
            messagebox.showinfo("Success", "Withdrawal complete!")
        else:
            messagebox.showerror("Error", "Insufficient funds.")
        window.destroy()
    
    # Step 4 Button triggers the function
    tk.Button(window, text="Withdraw", command=withdraw_action).pack()


# Start program
main_menu()

#Execution
# Load imports (tkinter + custom classes).
# Create objects: db, atm, logger, security.
# Add default customers to database.
# Create global variable current_card.
# Store function definitions in memory.
# Call main_menu(): creates GUI and enters event loop.
# Wait for user clicks.
# Button click triggers a callback → executes function line by line.
# GUI updates dynamically as Python executes function code.
# Program loops through menus until user exits.


# These are a class 

# Class Logger  Responsibility Prints log messages

# Class Database Responsibility Stores customer accounts

# Class Customer Responsibility Holds user info + account

# Class BankAccount Responsibility Stores balance + deposit/withdraw

# Class Security Responsibility PIN checking

# Class_ATM Responsibility  Controls authentication & money operations
