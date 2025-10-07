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

def demonstratePolymorphism():
    print(" Employee Payroll System ")

    # Input for all employees 

    name1 = input("Enter manager's name: ")
    salary = float(input("Enter Salary: "))
    manager = Manager(name1, salary)
    #emp = Manager(name, salary)
    #print(emp.getDetails())
    #print(emp.calculatePay())

    name2 = input("Enter salesperson's name: ")
    commission = float(input("Enter commision rate: "))
    salesAmount = float(input("Enter total sales amount: "))
    salesPerson = SalesPerson(name2, commission, salesAmount)
    #emp = SalesPerson(name, commission, salesAmount)
    #print(emp.getDetails())
    #print(emp.calculatePay())

    name3 = input("Enter hourly employee's name: ")
    hourlyRate = float(input("Enter the hourly rate: "))
    hoursWorked = float(input("Enter the hours worked: "))
    hourlyEmployee = HourlyEmployee(name3, hourlyRate, hoursWorked)
    #emp = HourlyEmployee(name, hourlyRate, hoursWorked)
    #print(emp.getDetails())
    #print(emp.calculatePay())

    # Store in a list of Employee reference
    employees = [manager, salesPerson, hourlyEmployee]

    for emp in employees:
        print(f"\n{emp.getDetails()}")
        print(f"Calculated Pay:${emp.calculatePay():.2f}")
        print(f"Actual Type: {type(emp).__name__}")

if __name__ == "__main__":
    demonstratePolymorphism()