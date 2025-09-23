class BMICalculator:
 #  A class to calculate BMI (Body Mass Index) using either metric or imperial units.

    weight_TO_KG = 0.45359237
    INCHES_TO_METERS = 0.0254
    INCHES_PER_FOOT = 12

    def __init__(self, *, weight=None, feet=None, inches=None, kilograms=None, meters=None):

  # Initialize a BMICalculator instance with either metric or imperial values.
  # Raises TypeError or ValueError if input is invalid.

        if kilograms is not None:
            if not isinstance(kilograms, (int, float)):
                raise TypeError("Kilograms must be a number.")
            if kilograms <= 0 or kilograms > 700:
                raise ValueError("Kilograms must be between 1 and 700.")
            self._kilograms = kilograms
            self._weight = None
        elif weight is not None:
            if not isinstance(weight, (int, float)):
                raise TypeError("Weight (pounds) must be a number.")
            if weight <= 0 or weight > 1500:
                raise ValueError("Weight in pounds must be between 1 and 1500.")
            self._weight = weight
            self._kilograms = None
        else:
            raise ValueError("Either kilograms or weight must be provided.")

        if meters is not None:
            if not isinstance(meters, (int, float)):
                raise TypeError("Meters must be a number.")
            if meters < 0.5 or meters > 3:
                raise ValueError("Meters must be between 0.5 and 3.")
            self._meters = meters
            self._feet = None
            self._inches = None
        elif feet is not None and inches is not None:
            if not isinstance(feet, int):
                raise TypeError("Feet must be an integer.")
            if not isinstance(inches, int):
                raise TypeError("Inches must be an integer.")
            if feet < 0 or feet > 8:
                raise ValueError("Feet must be between 0 and 8.")
            if inches < 0 or inches >= 12:
                raise ValueError("Inches must be between 0 and 11.")
            self._feet = feet
            self._inches = inches
            self._meters = None
        else:
            raise ValueError("Either meters or feet and inches must be provided.")

        assert self.kilograms > 0, "Internal error: kilograms must be positive"
        assert self.meters > 0, "Internal error: meters must be positive"

    @property
    def weight(self):
# Returns weight in pounds (if used)
        return self._weight

    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be a number.")
        if value <= 0 or value > 1500:
            raise ValueError("Weight in pounds must be between 1 and 1500.")
        self._weight = value
        self._kilograms = None  

    @property
    def feet(self):
# Returns height in feet
        return self._feet

    @feet.setter
    def feet(self, value):
        if not isinstance(value, int) or value < 0 or value > 8:
            raise ValueError("Feet must be an integer between 0 and 8.")
        self._feet = value

    @property
    def inches(self):
# Returns height in inches.
        return self._inches

    @inches.setter
    def inches(self, value):
        if not isinstance(value, int) or value < 0 or value >= 12:
            raise ValueError("Inches must be an integer between 0 and 11.")
        self._inches = value

    @property
    def kilograms(self):
# Returns weight in kilograms (calculated from pounds if needed).
        if self._kilograms is not None:
            return self._kilograms
        elif self._weight is not None:
            return self._weight * self.weight_TO_KG
        return None

    @property
    def meters(self):
# Returns height in meters (calculated from feet/inches if needed)
        if self._meters is not None:
            return self._meters
        elif self._feet is not None and self._inches is not None:
            total_inches = (self._feet * self.INCHES_PER_FOOT) + self._inches
            return total_inches * self.INCHES_TO_METERS
        return None

    @property
    def bmi(self):
# Calculates and returns the BMI rounded to 1 decimal place.
        if self.kilograms is not None and self.meters is not None:
            return round(self.kilograms / (self.meters ** 2), 1)
        return None

    @property
    def category(self):
# Returns BMI category based on WHO classification.
        if self.bmi is None:
            return "Invalid"
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal weight"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self):
# Returns a human-readable string of BMI and category.
        return f"BMI: {self.bmi}, Category: {self.category}"
