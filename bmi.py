def calculate_bmi(height, weight):
    print("Height= "+ str(height))
    print("Weight= "+ str(weight))
    print("Height= ", height)
    print("Weight= ", weight)
    BMI = weight/(height**2)
    print("BMI = ", round(BMI,2))
    print("Weight classification : ", end="")
    if(BMI < 18.5):
      print("Underweight")
      return -1
    elif BMI > 25.0:
       print("Overweight")
       return 1
    else:
       print("Normal weight")
       return 0
    


result = calculate_bmi(weight=57, height=1.73)
print("Result = ",result)
calculate_bmi(weight=97, height=1.63)
print("Result = ",result)
calculate_bmi(weight=37, height=1.89)
print("Result = ",result)