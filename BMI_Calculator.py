import pytest

def Calculate_Bmi(weight, height):
    total_weight = weight * 0.45
    total_height = (height * 0.025)**2
    
    total = total_weight / total_height


    if total < 18.5:
        print("Underweight")
    elif total <= 18.5 and total >= 24.9:
        print("Normal Weight")
    elif total >= 25 and total <= 29.9:
        print("Overweight")
    elif total >= 30:
        print("Obese")

def test_under():
    
def test_over():

def test_normal():

def test_obese():



def main():
    weight = float(input("Enter weight in lbs: "))
    height = float(input("Enter height in inches: "))
    bmi = Calculate_Bmi(weight, height)