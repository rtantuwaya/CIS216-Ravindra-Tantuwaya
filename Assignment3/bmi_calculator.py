
# In this program, I used class properties instead of methods.
# Unit Conversions:
# 1 pound = 0.45359237 kilograms
# 1 inch = 0.0254 met
# 1 INCHES_PER_FOOT = 12

class BMICalculator:

    weight_TO_KG = 0.45359237
    INCHES_TO_METERS = 0.0254
    INCHES_PER_FOOT = 12

    def __init__(self, *, weight=None, feet=None, inches=None):
       
        self._weight = weight
        self._feet = feet
        self._inches = inches

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def feet(self):
        return self._feet

    @feet.setter
    def feet(self, value):
        self._feet = value

    @property
    def inches(self):
        return self._inches

    @inches.setter
    def inches(self, value):
        self._inches = value

    @property
    def kilograms(self):
        if self._weight is not None:
            return self._weight * self.weight_TO_KG
        return None

    @property
    def meters(self):
        if self._feet is not None and self._inches is not None:
            total_inches = (self._feet * self.INCHES_PER_FOOT) + self._inches
            return total_inches * self.INCHES_TO_METERS
        return None

    @property
    def bmi(self):
        if self.kilograms is not None and self.meters is not None:
            return round(self.kilograms / (self.meters ** 2), 1)
        return None

    @property
    def category(self):
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
