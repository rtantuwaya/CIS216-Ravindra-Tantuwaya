
# Assignemnt 2
# Create a program that asks users for theirweight in pounds and their height in feet and inches.
# Calculate and display their BMI

# This program calculates the Body Mass (BMI) based on user input:
# weight in pounds, and height in feet and inches:

# BMI Formula (metric): BMI = weight (kg) / [height (m)] ^ 2

# Unit Conversions:
# 1 pound = 0.45359237 kilograms
# 1 inch = 0.0254 meters
# 1 feet = 12 inch

class BMICalculator:
    # Conversion constants
    POUNDS_TO_KG = 0.45359237
    INCHES_TO_METERS = 0.0254
    INCHES_PER_FOOT = 12

    def __init__(self, weightPounds, heightFeet, heightInches):
        self.weightPounds = weightPounds
        self.heightFeet = heightFeet
        self.heightInches = heightInches

    def calculate_bmi(self):
        totalInches = (self.heightFeet * self.INCHES_PER_FOOT) + self.heightInches
        heightMeters = totalInches * self.INCHES_TO_METERS
        weightKg = self.weightPounds * self.POUNDS_TO_KG
        bmi = weightKg / (heightMeters ** 2)
        return round(bmi, 1)

    def get_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"