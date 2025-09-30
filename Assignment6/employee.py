class Employee:
 # A base class to represent an employee.
 # Attributes: 
 #  name (str): The name of the employee.

    def __init__(self, name: str):
# Initializes the Employee with a name.
# Args:
#   name (str): The name of the employee.

        self.name = name

    def getDetails(self) -> str:
# Returns a string with the employee's details.
# Returns:  
#   str: A string containing the employee's name.

        return f"Employee Name: {self.name}"

class Manager(Employee): 
# A class to represent a manager, inheriting from Employee.
# Attributes: 
#   salary (float): The fixed salary of the manager.

    def __init__(self, name: str, salary: float):
 #Initializes the Manager with a name and salary.
 # Args - name (str): The name of the manager.
 #      -  salary (float): The salary of the manager.

        super().__init__(name)
        self.salary = salary

    def calculatePay(self) -> float:
# Calculates and returns the manager's salary.
# Returns: 
#   float: The manager's salary
 
        return self.salary

class SalesPerson(Employee):
# A class to represent a salesperson, inheriting from Employee.
# Attributes:
#   commission (float): The commission rate
#   salesAmount (float): The total amount of sales made.
    def __init__(self, name: str, commission: float, salesAmount: float):
# Initializes the SalesPerson with a name, commission rate, and sales amount.
# Args:
#   name (str): The name of the salesperson.
#   commission (float): The commission rate (percentage).
#   salesAmount (float): The total sales made by the salesperson.
        super().__init__(name)
        self.commission = commission/100
        self.salesAmount = salesAmount

    def calculatePay(self) -> float:
# Calculates and returns the salesperson's pay based on commission.
# Returns:
#   float: The pay calculated from commission and sales amount.
        return self.commission * self.salesAmount

class HourlyEmployee(Employee):
# A class to represent an hourly-paid employee, inheriting from Employee.
# Attributes:
#    hourlyRate (float): The rate per hour.
#    hourlyWorked (float): The number of hours worked.

    def __init__(self, name: str, hourlyRate: float, hoursWorked: float):
#  Initializes the HourlyEmployee with name, hourly rate, and hours worked.
#  Args: 
#   name (str): The name of the hourly employee.
#   hourlyRate (float): The hourly pay rate.
#   hoursWorked (float): Total number of hours worked.

        super().__init__(name)
        self.hourlyRate = hourlyRate
        self.hourlyWorked = hoursWorked

    def calculatePay(self) -> float:
#  Calculates and returns the total pay based on hours worked and rate.
#  Returns:
#    float: The total pay.

        return self.hourlyRate * self.hourlyWorked

def main():
# Main function to run the employee payroll system.

# It prompts the user to input details for:
#   - A Manager
#   - A SalesPerson
#   - An HourlyEmployee

# For each employee, it displays their details and calculated pay.

    print(" Employee Payroll System ")
        
    name = input("Enter manager's name: ")
    salary = float(input("Enter Salary: "))
    emp = Manager(name, salary)
    print(emp.getDetails())
    print(emp.calculatePay())

    name = input("Enter salesperson's name: ")
    commission = float(input("Enter commision rate: "))
    salesAmount = float(input("Enter total sales amount: "))
    emp = SalesPerson(name, commission, salesAmount)
    print(emp.getDetails())
    print(emp.calculatePay())

    name = input("Enter hourly employee's name: ")
    hourlyRate = float(input("Enter the hourly rate: "))
    hoursWorked = float(input("Enter the hours worked: "))
    emp = HourlyEmployee(name, hourlyRate, hoursWorked)
    print(emp.getDetails())
    print(emp.calculatePay())

# Unit Testing Section
import unittest
    
class TestEmployee(unittest.TestCase):

    def test_employee_initialization(self):
        e = Employee("Alice")
        self.assertEqual(e.name, "Alice")

    def test_employee_getDetails(self):
        e = Employee("Bob")
        self.assertEqual(e.getDetails(), "Employee Name: Bob")

class TestManager(unittest.TestCase):

    def test_manager_initialization(self):
        m = Manager("John", 5000.0)
        self.assertEqual(m.name, "John")
        self.assertEqual(m.salary, 5000.0)

    def test_manager_calculatePay(self):
        m = Manager("John", 5000.0)
        self.assertEqual(m.calculatePay(), 5000.0)

class TestSalesPerson(unittest.TestCase):

    def test_salesperson_initialization(self):
        s = SalesPerson("Jane", 10, 20000)
        self.assertEqual(s.name, "Jane")
        self.assertAlmostEqual(s.commission, 0.10)
        self.assertAlmostEqual(s.salesAmount, 20000)

    def test_salesperson_calcualatePay(self):
        s = SalesPerson("Jane", 10, 20000)
        self.assertEqual(s.calculatePay(), 2000.0)

class TestHourlyEmployee(unittest.TestCase):

    def test_hourlyemployee_initialization(self):
        h = HourlyEmployee("Tom", 20.0, 40)
        self.assertEqual(h.name, "Tom")
        self.assertEqual(h.hourlyRate, 20.0)
        self.assertEqual(h.hourlyWorked, 40)

    def test_hourlyemployee_calculatePay(self):
        h = HourlyEmployee("Tom", 20.0, 40)
        self.assertEqual(h.calculatePay(), 800.0)

if __name__ == "__main__":
    unittest.main()
