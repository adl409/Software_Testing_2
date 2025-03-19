import pytest
from BMI_Calculator import Calculate_Bmi

def test_underweight_upper_boundary():
    assert Calculate_Bmi(108, 5, 5) == (18.4, "Underweight")

def test_normal_lower_boundary():
    assert Calculate_Bmi(108.5, 5, 5) == (18.5, "Normal Weight")

def test_normal_upper_boundary():
    assert Calculate_Bmi(146, 5, 5) == (24.9, "Normal Weight")

def test_overweight_lower_boundary():
    assert Calculate_Bmi(147, 5, 5) == (25.1, "Overweight")

def test_overweight_upper_boundary():
    assert Calculate_Bmi(175, 5, 5) == (29.8, "Overweight")

def test_obese_lower_boundary():
    assert Calculate_Bmi(176, 5, 5) == (30.0, "Obese")