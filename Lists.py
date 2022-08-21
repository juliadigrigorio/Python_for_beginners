words = ["Hello", "world", "!"]

#-------

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

#-------

x = ["a", "b", "c"]
y = [1, 2, 3, 4, 5]

print(x[1])
print(y[3])

#-------

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]

#-------

m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(m[1][2])

#-------

str = "Hello world!"
print(str[6])


#-------
'''
Write a program that takes an input string and outputs the 3rd character of the string.
'''
my_string = input()
print(my_string[2])

#------------

nums = [5, 8, 2]
nums[1] = 42

print(nums)

#------------

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

#------------

nums = [1, 2, 3]
print(nums + [4, 5, 6])

#------------

x = [2, 4]
x += [6, 8]
print(x[2]//x[0])

#------------

nums = [1, 2, 3]
print(nums * 3)

#------------

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#------------

x = "hello world"

if "world" in x:
  print("Yes")

#------------

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#------------

'''
Given a list of numbers, output "bingo" if it contains the input number.
'''
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

num = int(input())

if num in x:
    print('bingo')

#------------

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

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

'''
Given a list of numbers, calculate their sum using a for loop.
'''
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
sum = 0
for current_number in x:
    sum += current_number
print(sum)

#------------

numbers = list(range(10))
print(numbers)

#------------

numbers = list(range(3, 8))
print(numbers)

#------------

numbers = list(range(5, 20, 2))
print(numbers)

#------------

x = list(range(7, 3, -1))
print(x)

#------------

for i in range(5):
  print("hello!")

#------------

'''
Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
'''
a = int(input())
b = int(input())
list = list(range(a,b))
print(list)

#------------

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#------------

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])

#------------

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])

#------------

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

#------------

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

#------------

nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

#------------

'''
Write a program that takes a string as input and outputs the last character of that string.
'''
my_string = input()
print(my_string[-1])

#------------

'''
Take a number N as input and output the sum of all numbers from 1 to N (including N).
'''
N = int(input())
print(N * (N + 1) // 2)

#------------

nums = [1, 3, 5, 2, 4]
print(len(nums))

#------------

nums = [1, 2, 3]
nums.append(4)
print(nums)

#------------

words = ["Python", "fun"]
words.insert(1, "is")
print(words)

#------------

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))

#------------

x = [1, 8, 42, 3]

print(min(x))
print(max(x))

#------------

x = [2, 4, 6, 2, 7, 2, 9]
print(x.count(2))

x.remove(4)
print(x)

x.reverse()
print(x)

#------------

'''
Write a program to take an input, add it to the end of the queue, and output the resulting list.
'''
queue = ['John', 'Amy', 'Bob', 'Adam']
name = input()
queue.append(name)
print(queue)

#------------

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#------------

x = ", ".join(["spam", "eggs", "ham"])
print(x)

#------------

str = "some text goes here"
x = str.split(' ')
print(x)

#------------

nums = [1, 3, 5, 2, 4]
print(len(nums))

#------------











