# Assignemnt 3
# Create a program that asks users for theirweight in pounds and their height in feet and inches.
# Calculate and display their BMI

# This program calculates the Body Mass (BMI) based on user input:
# weight in weight, and height in feet and inches:

# BMI Formula (metric): BMI = weight (kg) / [height (m)] ^ 2


from bmi_calculator import BMICalculator

def main():
 
    print("Welcome to the BMI Calculator\n")

    try:
        weight = float(input("Enter your weight in pounds: "))
        feet = int(input("Enter your height - feet: "))
        inches = int(input("Enter your height - additional inches: "))

        bmi_calculator = BMICalculator(weight=weight, feet=feet, inches=inches)

        bmi = bmi_calculator.bmi
        category = bmi_calculator.category

        print(f"\nYour BMI is: {bmi}")
        print("\nBMI Categories (WHO Reference):") 
        print("Underweight   : BMI < 18.5")
        print("Normal weight : 18.5 ≤ BMI < 25")
        print("Overweight    : 25 ≤ BMI < 30")
        print("Obese         : BMI ≥ 30")
        print(f"\nYou are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
