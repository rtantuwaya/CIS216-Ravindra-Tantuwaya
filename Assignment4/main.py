#Create a program that asks users for their weight in pounds and their height in feet and inches.
#Calculate and display their BMI (Body Mass Index).

#This program calculates the BMI based on user input:
#Weight in pounds
#Height in feet and inches

#BMI Formula (metric): BMI = weight (kg) / [height (m)] ^ 2

#Unit Conversions:
# 1 pound = 0.45359237 kilograms
# 1 inch  = 0.0254 meters
# 1 foot  = 12 inches

#Assignment 4 Requirements:
# Input validation for correct data types and reasonable value ranges
# Parameter validation in class methods and properties
# Raise exceptions for invalid inputs


from bmi_calculator import BMICalculator

def safe_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Please try again.")

def safe_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("Welcome to the BMI Calculator\n")
    
    while True:
        print("Choose input type:")
        print("1. Imperial (pounds, feet, inches)")
        print("2. Metric (kilograms, meters)")

        choice = input("Enter 1 or 2: ").strip()

        try:
            if choice == "1":
                print("\n-- Imperial Units --")
                weight = safe_float("Enter your weight in pounds: ")
                feet = safe_int("Enter your height - feet: ")
                inches = safe_int("Enter your height - additional inches: ")

                bmi_calculator = BMICalculator(weight=weight, feet=feet, inches=inches)

            elif choice == "2":
                print("\n-- Metric Units --")
                kilograms = safe_float("Enter your weight in kilograms: ")
                meters = safe_float("Enter your height in meters: ")

                bmi_calculator = BMICalculator(kilograms=kilograms, meters=meters)

            else:
                print("Error: Invalid choice. Please enter 1 or 2.\n")
                continue  

            bmi = bmi_calculator.bmi
            category = bmi_calculator.category

            print(f"\nYour BMI is: {bmi}")
            print("\nBMI Categories (WHO Reference):") 
            print("Underweight   : BMI < 18.5")
            print("Normal weight : 18.5 ≤ BMI < 25")
            print("Overweight    : 25 ≤ BMI < 30")
            print("Obese         : BMI ≥ 30")
            print(f"\nYou are classified as: {category}")
            break  

        except (ValueError, TypeError) as e:
            print(f"\nInput error: {e}\nPlease try again.\n")

if __name__ == "__main__":
    main()
