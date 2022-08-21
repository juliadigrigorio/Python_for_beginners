my_boolean = True
print(my_boolean)

print(2 == 3)

print("hello" == "hello")

#---------

open = True
closed = False

print(open)
print(closed)

#---------

x = 7

print(x != 8)
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)

#---------

print('a' > 'b')

print("Bob" > "Dave")

#---------

x = (7 > 5)
print(int(x))

#--------

x = 42
if x > 5:
   print("x is greater than 5")

#--------

age = 24

if age > 18:
   print("Cool")

#--------

num = 200
if num > 5:
   print("Bigger than 5")
   if num <= 47:
      print("Between 5 and 47")

#--------

num = 7
if num > 3:
   print("3")
   if num < 5:
      print("5")
      if num ==7:
         print("7")

#--------

'''
Write a program that checks if the water is boiling.
Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.
'''
temp = int(input())
if temp >= 100:
    print('Boiling')

#--------

x = 4
if x == 5:
   print("Yes")
else:
   print("No")

#--------

num = 3
if num == 1:
  print("One")
else:
  if num == 2:
    print("Two")
  else:
    if num == 3:
      print("Three")
    else:
      print("Something else")

#--------

num = 3
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3:
  print("Three")
else:
  print("Something else")

#--------

num = 8
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3:
  print("Three")
else:
  print("Something else")

#--------

'''
Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age of the person who tries to enter, and outputs "Allowed" if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.
'''
age = int(input())
if age >= 18:
    print('Allowed')
else:
    print('Sorry')

#--------

print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(2 < 1 and 3 > 6)

#--------

print(1 == 1 or 2 == 2)
print(1 == 1 or 2 == 3)
print(1 != 1 or 2 == 2)
print(2 < 1 or 3 > 6)

#--------

age = 24
limit = 18
height = 191

if (age > limit and height > 180):
  print("Yes")

#--------

print(not 1 == 1)
print(not 1 > 7)

#--------

country = "US"
age = 42

if(country == "US" or country == "GB") and (age > 0 and age < 100):
  print("Cool")

#--------

'''
Given the age of a person as an input, output their age group.

Here are the age groups you need to handle:
Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64
'''
age = int(input())
if(age >= 0 and age <= 11):
    print("Child")
elif(age >= 12 and age <= 17):
    print("Teen")
elif(age >= 18 and age <= 64):
    print("Adult")

#--------

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

#--------

x = 0
while x<10:
  print(x)
  x += 1

#--------

sum = 0
x = 10
while x > 0:
  sum += x
  x -= 1

print(sum)

#--------

x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

#--------

#INFINITE LOOP
x = 8

while x > 3:
  print(x)

#--------

'''
Write a program that outputs all the numbers from 0 to 10.
Only the even numbers.
'''
x = 0
while x<=10:
  if x % 2 == 0:
    print(x)
  x+=1

#--------

i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")

#--------

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)

#--------

'''
You are making a ticketing system. 
The price of a single ticket is $100.
For children under 3 years of age, the ticket is free.

Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.
'''
total = 0
i = 0
age = [0, 0, 0, 0, 0]
while i < 5:
    age[i] = int(input())
    i += 1

x = 0
while x < 5:
    if age[x] < 3:
        x += 1
        continue
    x += 1
    total += 100

print(total)

#--------

'''
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more
Write a program that takes a person's weight and height as input and outputs the corresponding BMI category.
'''
weight = float(input())
height = float(input())
BMI = (weight / (height**2))
if BMI < 18.5:
    print('Underweight')
elif (BMI >= 18.5) and (BMI < 25.0):
    print('Normal')
elif (BMI >= 25.0) and (BMI < 30.0):
    print('Overweight')
elif BMI >= 30.0:
        print('Obesity')

#--------




