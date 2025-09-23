import unittest
from bmi_calculator import BMICalculator

class TestBMICalculator(unittest.TestCase):

# Unit tests for the BMICalculator class, covering:
# - Valid/invalid metric and imperial inputs
# - Property behaviors (setters, conversions)
# - BMI calculation and WHO category classification

      # --- Metric  Tests ---

    def test_valid_metric_input(self):
# Should correctly calculate BMI and category with valid metric input.
        bmi = BMICalculator(kilograms=70, meters=1.75)
        self.assertAlmostEqual(bmi.bmi, 22.9)
        self.assertEqual(bmi.category, "Normal weight")
        #self.assertAlmostEqual(bmi.bmi, 25.9)

    def test_invalid_kilograms_type(self):
# Should raise TypeError for non-numeric kilograms.
        with self.assertRaises(TypeError):
            BMICalculator(kilograms="seventy", meters=1.75)
            #BMICalculator(kilograms=70, meters=1.75)

    def test_invalid_kilograms_value(self):
# Should raise ValueError for negative kilograms.
        with self.assertRaises(ValueError):
            BMICalculator(kilograms=-5, meters=1.75)
            #BMICalculator(kilograms= 5, meters=1.75)

    def test_invalid_meters_type(self):
# Should raise TypeError for non-numeric meters.
        with self.assertRaises(TypeError):
            BMICalculator(kilograms=70, meters="one point seven five")
            #BMICalculator(kilograms=70, meters= 1.75)


    def test_invalid_meters_value(self):
# Should raise ValueError for meters outside valid range.
        with self.assertRaises(ValueError):
            BMICalculator(kilograms=70, meters=0.3)
            #BMICalculator(kilograms=70, meters=3)

     # --- Imperial Initialization Tests ---

    def test_valid_imperial_input(self):
# Should correctly calculate BMI and category with valid imperial input.
        bmi = BMICalculator(weight=150, feet=5, inches=10)
        self.assertAlmostEqual(bmi.bmi, 21.5)
        self.assertEqual(bmi.category, "Normal weight")

    def test_invalid_weight_type(self):
# Should raise TypeError for non-numeric weight.
        with self.assertRaises(TypeError):
            BMICalculator(weight="one-fifty", feet=5, inches=10)

    def test_invalid_weight_value(self):
# Should raise ValueError for weight <= 0
        with self.assertRaises(ValueError):
             BMICalculator(weight=0, feet=5, inches=10)
             #BMICalculator(weight=150, feet=5, inches=10)

    def test_invalid_feet_type(self):
# Should raise TypeError for non-integer feet.
        with self.assertRaises(TypeError):
            BMICalculator(weight=150, feet=5.5, inches=10)
            #BMICalculator(weight=150, feet=5, inches=10)

    def test_invalid_feet_value(self):
# Should raise ValueError for feet > 8
        with self.assertRaises(ValueError):
            BMICalculator(weight=150, feet=9, inches=10)
            #BMICalculator(weight=150, feet=8, inches=10)

    def test_invalid_inches_type(self):
# Should raise TypeError for non-integer inches.
        with self.assertRaises(TypeError):
            BMICalculator(weight=150, feet=5, inches="ten")
            #BMICalculator(weight=150, feet=5, inches=10)

    def test_invalid_inches_value(self):
# Should raise ValueError for inches >= 12."
        with self.assertRaises(ValueError):
            BMICalculator(weight=150, feet=5, inches=12)
            #BMICalculator(weight=150, feet=5, inches=11)
           
     # --- Property Tests ---

    def test_kilograms_conversion(self):
# Should correctly convert weight in pounds to kilograms.
        bmi = BMICalculator(weight=220, feet=6, inches=0)
        self.assertAlmostEqual(bmi.kilograms, 99.7903214)

    def test_meters_conversion(self):
# Should correctly convert height in feet and inches to meters.
        bmi = BMICalculator(weight=150, feet=5, inches=9)
        self.assertAlmostEqual(bmi.meters, 1.7526)
   
    def test_weight_setter(self):
# Should correctly update weight using the setter.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        bmi.weight = 160
        self.assertEqual(bmi.weight, 160)
        #self.assertEqual(bmi.weight, 150)

    def test_feet_setter(self):
# Should correctly update feet using the setter.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        bmi.feet = 6
        self.assertEqual(bmi.feet, 6)
        #self.assertEqual(bmi.feet, 5)

    def test_inches_setter(self):
# Should correctly update inches using the setter.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        bmi.inches = 11
        self.assertEqual(bmi.inches, 11)
        #self.assertEqual(bmi.inches, 10)

    def test_weight_setter_invalid(self):
# Should raise ValueError for invalid weight via setter.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        with self.assertRaises(ValueError):
            bmi.weight = -10
            #bmi.weight = 10

    def test_feet_setter_invalid(self):
# Should raise ValueError for invalid feet via setter.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        with self.assertRaises(ValueError):
            bmi.feet = 10
            #bmi.feet = 8

    def test_inches_setter_invalid(self):
# Should raise ValueError for invalid inches via setter.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        with self.assertRaises(ValueError):
            bmi.inches = 13
            #bmi.inches = 11


     # --- Category Tests ---

    def test_underweight_category(self):
# Should return 'Underweight' category for low BMI.
        bmi = BMICalculator(kilograms=45, meters=1.75)
        self.assertEqual(bmi.category, "Underweight")
        #self.assertEqual(bmi.category, "Normal weight")

    def test_normal_category(self):
# Should return 'Normal weight' category for normal BMI.
        bmi = BMICalculator(kilograms=68, meters=1.75)
        self.assertEqual(bmi.category, "Normal weight")
        #self.assertEqual(bmi.category, "Underweight")

    def test_overweight_category(self):
# Should return 'Overweight' category for BMI >= 25.
        bmi = BMICalculator(kilograms=80, meters=1.75)
        self.assertEqual(bmi.category, "Overweight")
        #self.assertEqual(bmi.category, "Normal weight")

    def test_obese_category(self):
# Should return 'Obese' category for BMI >= 30.
        bmi = BMICalculator(kilograms=95, meters=1.75)
        self.assertEqual(bmi.category, "Obese") 
        #self.assertEqual(bmi.category, "Normal weight")

    def test_invalid_category(self):
# Should return 'Invalid' category if height is missing.
        bmi = BMICalculator(weight=150, feet=5, inches=5)
        bmi._feet = None  # Invalidate height
        self.assertEqual(bmi.category, "Invalid")
        #self.assertEqual(bmi.category, "Normal weight")

     # --- String Representation ---

    def test_str_output(self):
# Should return correct string representation.
        bmi = BMICalculator(kilograms=70, meters=1.75)
        self.assertEqual(str(bmi), "BMI: 22.9, Category: Normal weight")
        #self.assertEqual(str(bmi), "BMI: 25.9, Category: Normal weight")
        #self.assertEqual(str(bmi), "BMI: 22.9, Category: Overweight")

if __name__ == "__main__": 
    unittest.main()