import pytest
from BMI_Calculator import Calculate_Bmi

def test_under():
    assert Calculate_Bmi(100, 5, 5) == (16.6, "Underweight")

def test_normal():
    assert Calculate_Bmi(150, 5, 8) == (22.8, "Normal weight")

def test_over():
    assert Calculate_Bmi(180, 5, 8) == (27.4, "Overweight")

def test_obese():
    assert Calculate_Bmi(220, 5, 8) == (33.4, "Obese")