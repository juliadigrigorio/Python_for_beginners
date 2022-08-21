print("Python is fun!")

print('Always look on the bright side of life')

#-----------

print("42")

#-----------

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')

#-----------

print("He said: \"cool!\".")

#-----------

print('I\'m learning Python. It\'s easy.')

#-----------

print('One \nTwo \nThree')

#-----------

print("\t hey \t there")

#-----------

print("Hi \r there")

#-----------

print("Newline is \\n")

#-----------

print('''
I'm learning.
Python's syntax is easy.
''')

#-----------

'''
Write a program to output the letters A B C D, each on a separate line.
'''
print("""A
B
C
D""")

#-----------

print("Spam" + 'eggs')

#-----------

print("2" + "2")

#-----------

print("spam" * 3)
print(4 * '2')

#-----------

print("test" * "hi") #ERROR

#-----------

'''
Create a program to output "hi" 42 times, without any separators, on the same line.
'''
print('hi' * 42)

#-----------

'''
You need to make a program for a leaderboard. 
The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
1.
2.
3.
'''
print("""1.
2.
3.
4.
5.
6.
7.
8.
9.""")

#------------

str = "Hello world!"
print(str[6])

#------------

x = "Python"
print(x[1] + x[4])

#------------

'''
Write a program that takes an input string and outputs the 3rd character of the string.
'''
my_string = input()
print(my_string[2])

#------------

x = "hello world"

if "world" in x:
  print("Yes")

#------------

str = "testing for loops"
count = 0

for x in str:
  if(x == 't'):
    count += 1

print(count)

#------------

text = "some text"
for x in text:
  if x == 'e':
    break
  print(x)

#------------

str = "some text"
x = len(str)
print(x)

#------------

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#------------

a = "{x}, {y}".format(x=5, y=12)
print(a)

#------------

x = ", ".join(["spam", "eggs", "ham"])
print(x)

#------------

str = "some text goes here"
x = str.split(' ')
print(x)

#------------

x = "Hello ME"
print(x.replace("ME", "world"))

#------------

print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())

#------------

'''
Replace all of the # characters in the given input with spaces and output the result.
'''
msg = input()
x = msg.replace('#', ' ')
print(x)

#------------








