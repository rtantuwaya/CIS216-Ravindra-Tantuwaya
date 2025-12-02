
# Python reading the file from the top.
# Imports:

import tkinter as tk
#Python loads the tkinter module and messagebox class.
from tkinter import messagebox
# These are required for creating GUI elements and showing error messages.
import unittest
# used to run tests

 # Class Definition:

class CalculatorApp:
    # Python defines the class CalculatorApp but does not execute its methods yet
    # methods __init__
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        # ------------------------
        # Input Labels & Fields
        # Creates labels, entry fields, buttons, text box
        tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)

        self.num1 = tk.Entry(root)
        self.num2 = tk.Entry(root)
        self.num1.grid(row=0, column=1)
        self.num2.grid(row=1, column=1)

        # ------------------------
        # Operation Buttons
        # Buttons are linked to the respective methods
        tk.Button(root, text="Add", command=self.add).grid(row=2, column=0, pady=10)
        # clicks a Add button Tkinter calls the add method
        tk.Button(root, text="Subtract", command=self.subtract).grid(row=2, column=1)
        # clicks a Subtract button Tkinter calls the Subtract method
        tk.Button(root, text="Multiply", command=self.multiply).grid(row=3, column=0)
        # clicks a Multiply button Tkinter calls the multiply method
        tk.Button(root, text="Divide", command=self.divide).grid(row=3, column=1)
        # clicks a Divide button Tkinter calls the divide method

        # ------------------------
        # Output Textbox
        # ------------------------
        tk.Label(root, text="Result:").grid(row=4, column=0, pady=10)
        self.output = tk.Text(root, height=3, width=30)
        self.output.grid(row=4, column=1)

    # ------------------------
    # Methods get_numbers
    # ------------------------
    def get_numbers(self):
        # Retrieve to read and convert the user input into two floats.
        try:
            return float(self.num1.get()), float(self.num2.get())
            # A tuple containing two floating-point numbers
        except ValueError:
            #  Error Handling:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return None

     # Methods display
    def display(self, text):
        #  Display a message in the text output box
        #  Parameters text 
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)

    # Methods add
    def add(self):
        # Perform addition and display the result
        nums = self.get_numbers()
        # get_numbers() reads input
        if nums:
            self.display(f"Result: {nums[0] + nums[1]}")
            # display() shows the result

    # Methods subtract
    def subtract(self):
        # Perform subtraction and display the result.
        nums = self.get_numbers()
        # get_numbers() reads input
        if nums:
            self.display(f"Result: {nums[0] - nums[1]}")
             # display() shows the result

     # Methods multiply
    def multiply(self):
        # Perform multiplication and display the result
        nums = self.get_numbers()
        # get_numbers() reads input
        if nums:
            self.display(f"Result: {nums[0] * nums[1]}")
             # display() shows the result

    # Methods divide
    def divide(self):
        # Perform division and display the result
        nums = self.get_numbers()
        # get_numbers() reads input
        if nums:
            if nums[1] == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                #  Shows an error message if attempting to divide by zero
            else:
                self.display(f"Result: {nums[0] / nums[1]}")
                 # display() shows the result

# =====================================================
# Unit Tests
# =====================================================

class TestCalculatorApp(unittest.TestCase):
 # Tests for CalculatorApp methods

    def setUp(self):
        # GUI not displayed during tests
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)
        self.root.withdraw()
        # Prevent window from appearing on screen

    def test_valid_number_input(self):
        self.app.num1.insert(0, "10")
        self.app.num2.insert(0, "5")
        nums = self.app.get_numbers()
        self.assertEqual(nums, (10.0, 5.0))

    def test_invalid_number_input(self):
        self.app.num1.insert(0, "ten")
        self.app.num2.insert(0, "5")
        nums = self.app.get_numbers()
        self.assertIsNone(nums)

    def test_addition(self):
        self.app.num1.insert(0, "3")
        self.app.num2.insert(0, "7")
        self.app.add()
        result = self.app.output.get("1.0", tk.END).strip()
        self.assertEqual(result, "Result: 10.0")

    def test_subtraction(self):
        self.app.num1.insert(0, "10")
        self.app.num2.insert(0, "4")
        self.app.subtract()
        result = self.app.output.get("1.0", tk.END).strip()
        self.assertEqual(result, "Result: 6.0")

    def test_multiplication(self):
        self.app.num1.insert(0, "6")
        self.app.num2.insert(0, "3")
        self.app.multiply()
        result = self.app.output.get("1.0", tk.END).strip()
        self.assertEqual(result, "Result: 18.0")

    def test_division(self):
        self.app.num1.insert(0, "12")
        self.app.num2.insert(0, "3")
        self.app.divide()
        result = self.app.output.get("1.0", tk.END).strip()
        self.assertEqual(result, "Result: 4.0")

    def test_divide_by_zero(self):
        self.app.num1.insert(0, "4")
        self.app.num2.insert(0, "0")
        # divide by zero triggers GUI popup; cannot check messagebox, but ensure no crash
        try:
            self.app.divide()
        except Exception:
            self.fail("divide() raised an exception on divide-by-zero!")

# ------------------------
# Run the program
# ------------------------
if __name__ == "__main__":
# if __name__ == "__main__" ensures this code runs only if the file is executed directly.
    print("\nRunning unit tests...\n")
    test_results = unittest.main(exit=False)

    if not test_results.result.failures and not test_results.result.errors:
         print("\nAll tests passed. Starting GUI...\n")
    root = tk.Tk()
    # root = tk.Tk()  creates the main Tkinter window
    CalculatorApp(root)
    # CalculatorApp(root)  creates an instance of CalculatorApp
    # Calls the __init__ method
    root.mainloop()
# root.mainloop() starts the Tkinter event loop, waiting for user actions (button clicks).
