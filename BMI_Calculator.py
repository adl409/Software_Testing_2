import pytest

def Calculate_Bmi(weight, feet, inches):
    
    total_weight = weight * 0.45
    total_height = ((feet * 12) + inches) * 0.025
    total = round((total_weight / (total_height ** 2)), 1)  


    if total < 18.5:
        type = "Underweight"

    elif total >= 18.5 and total <= 24.9:
        type = "Normal Weight"

    elif total >= 25 and total <= 29.9:
        type = "Overweight"

    else:
        type = "Obese"

    return total, type
    



def main():
    weight = float(input("Enter weight in lbs: "))
    feet = float(input("Enter height in feet: "))
    inches = float(input("Enter height in inches: "))

    total, type = Calculate_Bmi(weight, feet, inches)
    print("This is your BMI:", total, type)

main()