
def my_func():
   print("spam")
   print("spam")
   print("spam")

#------------

def hello():
    print("Hello world!")

hello()
hello()
hello()

#------------

'''
Write the function so that it will take the name of the user as input and output the welcome message with it.
'''
def welcome():
    name = input()
    print('Welcome,', name)

welcome()

#------------

def exclamation(word):
    print(word + "!")

exclamation("spam")

#------------

def exclamation(word):
    print(word + "!")

exclamation("spam")
exclamation("eggs")
exclamation("python")

#------------

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

#------------

'''
Write the function printBill(), which takes one string argument and outputs formatted text.
You need to take the user input and call the function by passing the input as its argument.
'''
def printBill():
    text = input()
    print("======")
    print(text)
    print("======")

printBill()

#------------

def sum(x, y):
  return x+y

res = sum(42, 7)
print(res)

#------------

def max(x, y):
    if x >= y:
        return x
    else:
        return y


if (max(6, 4) > 10):
    print("Yes")
else:
    print("Nope")

#------------

def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))

#------------

def double(a, b):
   return [a*2, b*2]

x = double(6, 9)
print(x)

#------------

'''
Write the area function, which takes the length and width as arguments, to calculate and return the area.
'''


def area(x, y):
    return (x * y)

w = int(input())
h = int(input())

print(area(w, h))

#------------

'''
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.
'''
def search(text, word):
  if word in text:
    return "Word found"
  else:
    return "Word not found"
text = input()
word = input()

print(search(text, word))

#------------



