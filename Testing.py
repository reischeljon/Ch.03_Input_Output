# miles_driven = int(input("enter miles driven:"))
# gallons_used = float(input("enter gallons used:"))
# mpg = miles_driven / gallons_used
# print("Miles per gallon:", mpg)

# person_name = str(input("enter your name:"))
# print("Greetings",person_name) #code is finished

# base_triangle = int(input("enter base of triangle:"))
# height_triangle = float(input("enter height of triangle"))
# area = 1/2 * base_triangle * height_triangle
# print("area of triangle:", area) #code is finished

# radius_circle = int(input("enter radius of a circle"))
# circ = 2 * 3.14 * radius_circle
# print("circumference of circle:", circ) # pie was simplified to 3.14 code finished

# whole = int(input("enter a integer"))
# whole_sqrt = float(whole) ** 0.5
# print("square root of integer:", whole_sqrt)

# Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
# Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)

# print("May the mass times acceleration be with you!")
# mass = int(input("Enter the mass of an object"))
# accl = int(input("Enter the acceleration"))
# force = mass * accl
# print("Get it?", force)

# Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.
# fahrenheit = int(input("enter the temperature in Fahrenheit!"))
# celsius = (fahrenheit - 32) * 5/9
# print("the temperature converted to celsius is:", celsius)

# Create a new program that will ask the user for the information needed to find the area of a trapezoid
# and then print the area.
# base1 = int(input("Enter the first base fo the trapezoid"))
# base2 = int(input("Enter the second base of the trapezoid"))
# height = int(input("Enter the height of the trapezoid"))
# a = base1 + base2
# b = a / 2
# area = b * height
# print("your area is:", area)

# Create a program that asks the user for their semester grade, final exam grade,
# and final exam worth and then calculates the overall final grade.
# Ask your instructor if you don't know how to calculate weighted averages.
# You don't have to print out the letter grade. We will do that in the next chapter


semester_grade = float(input("Enter your semester grade:"))
final_exam = float(input("Enter you exam grade:"))
final_worth = float(input("Enter the final exam worth:"))

fworth=final_worth/100
sgworth = 1-fworth
og = fworth*final_exam+sgworth*semester_grade

