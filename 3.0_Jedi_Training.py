# 3.0 Jedi Training (20pts)  Name:Jonathan Reischel


# In all the short programs below, do a good job communicating with your end user!


# 1) Write a program that asks someone for their name and then prints a greeting that uses their name. (1pt)
person_name = str(input("enter your name:"))
print("Greetings", person_name)

# 2. Write a program where a user enters a base and height, and you print the area of a triangle. (1pt)
base_triangle = int(input("enter base of triangle:"))
height_triangle = float(input("enter height of triangle"))
area = 1/2 * base_triangle * height_triangle
print("area of triangle:", area)  # code is finished

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference. (1pt)
radius_circle = int(input("enter radius of a circle"))
circ = 2 * 3.14 * radius_circle
print("circumference of circle:", circ)  # pie was simplified to 3.14 code finished

# 4. Ask a user for an integer and then print the square root. (1pt)
whole = int(input("enter a integer"))
whole_sqrt = float(whole) ** 0.5
print("square root of integer:", whole_sqrt)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next. (1pt)
print("May the mass times acceleration be with you!")
mass = int(input("Enter the mass of an object"))
accl = int(input("Enter the acceleration"))
force = mass * accl
print("Get it?", force)
'''
6. TEMPERATURE PROGRAM (5pts)
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.
'''
fahrenheit = int(input("enter the temperature in Fahrenheit!"))
celsius = (fahrenheit - 32) * 5/9
print("the temperature converted to celsius is:", celsius)
'''

Test your program with the following data:
In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: -40 Please tell me what this output is!

'''


'''
7. TRAPEZOID PROGRAM (5pts)
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.
'''
base1 = int(input("Enter the first base of the trapezoid"))
base2 = int(input("Enter the second base of the trapezoid"))
height = int(input("Enter the height of the trapezoid"))
a = base1 + base2
b = a / 2
area = b * height
print("your area is:", area)
'''
Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''


'''
8. GRADING PROGRAM (5pts)
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
semester_grade = float(input("Enter your semester grade:"))
final_exam = float(input("Enter you exam grade:"))
final_worth = float(input("Enter the final exam worth:"))

fworth=final_worth/100
sgworth = 1-fworth
og = fworth*final_exam+sgworth*semester_grade
