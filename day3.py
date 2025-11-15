# Exercises - Day 3
"""
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.(skip)
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
15. There is no 'on' in both dragon and python(skip)
16. Find the length of the text python and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10 (skip)
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years(skip)
23. Write a Python script that displays the following table
          1 1 1 1 1
          2 1 2 4 8
          3 1 3 9 27
          4 1 4 16 64
          5 1 5 25 125

"""

#1. Declare your age as integer variable
age = 69

#2. Declare your height as a float variable
#height = 1.70 

#3. Declare a variable that store a complex number
complex_num = 6 + 9j

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter base:"))
height = float(input("Enter height:"))
area_triangle = 0.5*base*height
print(f"The area of triangle: {area_triangle:.2f} sq meter")

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = float(input("Enter a:"))
side_b = float(input("Enter b:"))
side_c = float(input("Enter c:"))
perimeter_triangle = side_a + side_b + side_c
print(f"The perimetter of triangle: {perimeter_triangle:.2f} meter")

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length:"))
width = float(input("Enter width:"))
area_rectangle = length*width
perimeter_rectangle = 2*(length + width)
print(f"The area of rectangle: {area_rectangle:.2f} sq meter")
print(f"The perimetter of rectangle: {perimeter_rectangle:.2f} meter")

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# here you can use a variable pi = 3.14 but i prefer to used module
import math
pi = math.pi
radiius_circle = float(input("radius:"))
area_circle = pi*radiius_circle**2
perimeter_circle = 2*pi*radiius_circle
print(f"The area of circle: {area_circle:.2f} sq meter")
print(f"The perimetter of circle: {perimeter_circle:.2f} meter")

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
#The equation is in slope-intercept form: y = mx + b
m = 2
b = -2

# Calculate x-intercept: set y = 0
# 0 = 2(x) -2 ; x = 1
x_intercept = 1

slope = m
y_intercept = b

print(f"the slope is : {slope}")
print(f"the x-intercept is : {(x_intercept,0)}")
print(f"the y-intercept is : {(0,y_intercept)}")


#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10
m = (y_2 - y_1)/(x_2 - x_1)
d = math.sqrt((y_2 - y_1)**2 + (x_2 - x_1)**2)

print(f"the slope is: {m}")
print(f"the euclidean distance is: {d:.2f}")

#10. Compare the slopes in tasks 8 and 9.
if slope == m: 
  print ('they are the same slope')
else:
  print('not the same slope')


#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_python = len('python')
len_dragon = len('dragon')

if len_python != len_dragon:
  print(True)
else:
  print(False)

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in "python" and "on" in "dragon":
  print(True)
else:
  print(False)


#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
if "jargon" in sentence:
  print(True)
else:
  print(False)

#16. Find the length of the text python and convert the value to float and convert it to string
len_python = len("python")
python_float = float(len_python)
python_string = str(python_float)
type_of_python = type(python_string)
print(python_string)
print(type_of_python)


#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numbers = int(input("Enter any number:"))

if numbers % 2 == 0:
  print("this is even number")
else:
  print("this is not even number")

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
if floor_division == int(2.7):
  print(True)
else:
  print(False)

#19. Check if type of '10' is equal to type of 10
print(type("10") is type(10))

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter no. of hours:"))
rate_per_hour = float(input("Enter rate per hour:"))
person_salary = (hours*rate_per_hour)
print(f"My salary is: ${person_salary:.2f}")

#23. Write a Python script that displays the following table
"""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
# Step 1: Create an empty list to collect rows
row_num = []
# Step 2: Loop through numbers 1 to 5
for number in range(1,6): 
  squared = number**2       
  cube = number**3
# Add the row to the accumulator
  result = [number, 1, number, squared, cube]
  row_num.append(result)       

# Step 3: Print all rows after collection
for row in row_num:
    print(*row)