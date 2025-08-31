# main.py

from bmi_calculator import BMICalculator

def main():
    print("Welcome to the BMI Calculator\n")

    try:
        weight = float(input("Enter your weight in pounds: "))
        feet = int(input("Enter your height - feet: "))
        inches = int(input("Enter your height - additional inches: "))

        bmi_calculator = BMICalculator(weight, feet, inches)

        bmi = bmi_calculator.calculate_bmi()
        category = bmi_calculator.get_category()

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
