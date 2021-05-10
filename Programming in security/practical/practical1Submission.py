#Question 1
str1 = input('Enter the length of the square: ')
length = int(str1)
area,perimeter = length**2,length*4
print(f"Area of square {area} \nPerimeter of square {perimeter}")

#Question 2
number1 = input('Enter your weight: ')
number2 = input('Enter your height: ')
weight,height=int(number1),int(number2)
bmitest=weight/(height**2)
bmi = round(bmitest, 1)
print(f'Your bmi is {bmi}')

#End of practical 1