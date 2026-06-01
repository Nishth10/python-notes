# Day 1 - Python Basics

## Day 1 Topics Covered

What is Programming

What is Python

High Level Language

Compiler vs Interpreter

Python Installation

VS Code Setup

Running Python Programs

Python Character Set

print() Function

Variables

Variable Naming Rules

Data Types

Keywords

Python Case Sensitivity

Operators

Type Conversion

Input Function

Conditional Statements

Ternary Operator



# What is Programming?

Programming is the process of writing instructions that tell a computer what to do.

A computer understands only machine language (0 and 1). Therefore, programming



# High Level Language (HLL)

A High Level Language is a programming language that is easy for humans to read, write, and understand.

Examples:

* Python
* Java
* C++
* JavaScript

Advantages:

* Easy to learn
* Easy to write
* Easy to debug
* Platform independent

Disadvantages:

* Slower than machine language
* Requires translation before execution



# Compiler vs Interpreter

A computer understands only machine language.

Therefore, source code must be translated into machine code.

## Compiler

A compiler translates the entire program at once.

Examples:

* C
* C++

Advantages:

* Faster execution
* Creates executable file

Disadvantages:

* Errors shown after compiling the whole program

## Interpreter

An interpreter translates and executes one line at a time.

Example:

* Python

Advantages:

* Easier debugging
* Immediate error detection

Disadvantages:

* Slightly slower execution



# Python Character Set

Python uses characters to write programs.

Character categories:

### Letters

A-Z
a-z

### Digits

0-9

### Special Symbols

* * * / % = < > ! @ # $ etc.

### White Spaces

Space, Tab, New Line



# First Python Program

```python
print("Hello World")
```

Output:

```text
Hello World
```

Explanation:

* print() is a built-in Python function.
* It displays information on the screen.
* "Hello World" is a string.



# Understanding print()

## Printing Text

```python
print("My name is Nishtha")
```

Output:

```text
My name is Nishtha
```

## Printing Numbers

```python
print(23)
```

Output:

```text
23
```

## Printing Multiple Values

```python
print("Age =", 23)
```

Output:

```text
Age = 23
```

## Arithmetic Inside print()

```python
print(23 + 58)
```

Output:

```text
81
```



# Variables

A variable is a named memory location used to store data.

Example:

```python
name = "Nishtha"
age = 23
price = 25.99
```

Variables help store information that can be used later.



# Variables and Memory

When a variable is created:

```python
age = 23
```

Python stores:

* Variable name → age
* Value → 23
* Memory address internally

The variable points to the stored value in memory.



# Rules for Variable Names

Valid:

```python
name
student_name
age1
_price
```

Invalid:

```python
1name
my-name
class
```

Rules:

1. Cannot start with a number.
2. Cannot contain spaces.
3. Cannot use Python keywords.
4. Can contain letters, digits and underscore.
5. Python is case-sensitive.



# Data Types

Python supports multiple data types.

## Integer

```python
age = 23
```

Type:

```python
int
```



## Float

```python
price = 25.99
```

Type:

```python
float
```



## String

```python
name = "Nishtha"
```

Type:

```python
str
```



## Boolean

```python
is_student = True
```

Possible values:

```python
True
False
```



## None

```python
x = None
```

Represents absence of value.



# Checking Data Types

```python
name = "Nishtha"

print(type(name))
```

Output:

```python
<class 'str'>
```

Example:

```python
print(type(23))
print(type(25.99))
print(type(True))
```



# Python Keywords

Keywords are reserved words with special meanings.

Examples:

```python
if
else
elif
for
while
break
continue
True
False
None
return
def
class
```

Keywords cannot be used as variable names.



# Python Case Sensitivity

Python treats uppercase and lowercase differently.

Example:

```python
age = 23
Age = 50
```

These are two different variables.


# Operators in Python

Operators are symbols used to perform operations on variables and values.

-

## Arithmetic Operators

| Operator | Meaning             | Example |
|          |                     |         |
| +        | Addition            | a + b   |
| -        | Subtraction         | a - b   |
| *        | Multiplication      | a * b   |
| /        | Division            | a / b   |
| %        | Modulus (Remainder) | a % b   |
| //       | Floor Division      | a // b  |
| **       | Exponentiation      | a ** b  |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

Output:

```text
13
7
30
3.3333
1
3
1000
```



## Division Operator (/)

The division operator always returns a float value.

Example:

```python
a = 5
b = 2

print(a / b)
```

Output:

```text
2.5
```



## Floor Division Operator (//)

Returns the largest integer less than or equal to the result.

Example:

```python
print(5 // 2)
```

Output:

```text
2
```

Example:

```python
print(-5 // 2)
```

Output:

```text
-3
```



## Modulus Operator (%)

Returns the remainder.

Example:

```python
print(10 % 3)
```

Output:

```text
1
```

Example:

```python
print(12 % 5)
```

Output:

```text
2
```



## Exponentiation Operator (**)

Used to calculate powers.

Example:

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```



# Comments in Python

Comments are ignored by Python.

They are used to explain code.

Example:

```python
# This is a comment

print("Hello")
```



## Multi-Line Comments

```python
"""
This is
a multi-line
comment
"""
```



# Input Function

The input() function is used to take input from the user.

Example:

```python
name = input("Enter your name: ")

print(name)
```

Input:

```text
Nishtha
```

Output:

```text
Nishtha
```



# Taking Integer Input

input() always returns a string.

Therefore we must convert it.

Example:

```python
age = int(input("Enter age: "))
```



# Taking Float Input

Example:

```python
price = float(input("Enter price: "))
```



# Type Conversion

Type conversion means changing one data type into another.



## Automatic Type Conversion

Python automatically converts compatible data types.

Example:

```python
a = 2
b = 4.5

print(a + b)
```

Output:

```text
6.5
```

Python converts integer to float automatically.


## Type Casting

Manual conversion by programmer.

### int()

```python
x = int("25")
```

### float()

```python
x = float("25")
```

### str()

```python
x = str(25)
```


# Strings

A string is a sequence of characters.

Examples:

```python
name = "Nishtha"
city = 'Delhi'
```



## Creating Strings

```python
str1 = "Hello"
str2 = 'Hello'
str3 = """Hello"""
```

All are valid.



## Escape Sequences

### New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab Space

```python
print("Hello\tWorld")
```

Output:

```text
Hello    World
```


## String Concatenation

Joining strings together.

Example:

```python
first = "Hello"
second = "World"

print(first + second)
```

Output:

```text
HelloWorld
```



## Length of String

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```



## String Indexing

Each character has an index.

```text
P Y T H O N
0 1 2 3 4 5
```

Example:

```python
name = "Python"

print(name[0])
```

Output:

```text
P
```



## Negative Indexing

```text
P Y T H O N
-6 -5 -4 -3 -2 -1
```

Example:

```python
print(name[-1])
```

Output:

```text
N
```


# String Slicing

Slicing is used to access a part of a string.

Syntax:

```python
string[start:end]
```

The character at the start index is included, while the character at the end index is excluded.

Example:

```python
name = "PYTHON"

print(name[0:3])
```

Output:

```text
PYT
```



## Examples of String Slicing

```python
name = "PYTHON"

print(name[0:2])
print(name[2:5])
print(name[:4])
print(name[1:])
```

Outputs:

```text
PY
THO
PYTH
YTHON
```



## Negative Slicing

Python also supports negative indexing.

```python
name = "PYTHON"

print(name[-4:-1])
```

Output:

```text
THO
```



# String Functions

Python provides built-in functions for string manipulation.



## len()

Returns the length of the string.

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```



## endswith()

Checks whether a string ends with a specific value.

```python
name = "I am learning Python"

print(name.endswith("Python"))
```

Output:

```text
True
```



## capitalize()

Capitalizes the first character.

```python
name = "python"

print(name.capitalize())
```

Output:

```text
Python
```



## replace()

Replaces one value with another.

```python
name = "I like Java"

print(name.replace("Java", "Python"))
```

Output:

```text
I like Python
```



## find()

Returns the first occurrence of a value.

```python
name = "I am learning Python"

print(name.find("learning"))
```

Output:

```text
5
```

If the value is not found:

```text
-1
```

---

## count()

Counts occurrences of a value.

```python
name = "hello"

print(name.count("l"))
```

Output:

```text
2
```

---

# Conditional Statements

Conditional statements help a program make decisions.



## if Statement

Syntax:

```python
if condition:
    statement
```

Example:

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```



## if-else Statement

Syntax:

```python
if condition:
    statement1
else:
    statement2
```

Example:

```python
num = 5

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```



## if-elif-else Statement

Used when multiple conditions need to be checked.

Example:

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
```



## Nested if

An if statement inside another if statement.

Example:

```python
age = 20

if age >= 18:
    if age <= 60:
        print("Eligible")
```



# Ternary Operator

Used to write if-else in a single line.

Syntax:

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Output:

```text
Adult
```



# Practice Programs Completed

## Program 1

Hello World

```python
print("Hello World")
```



## Program 2

Sum of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```



## Program 3

Average of Two Numbers

```python
a = int(input())
b = int(input())

print((a + b) / 2)
```



## Program 4

Area of Square

```python
side = float(input())

print(side * side)
```



## Program 5

Comparison Program

```python
a = int(input())
b = int(input())

print(a >= b)
```



## Program 6

String Length

```python
name = input()

print(len(name))
```



## Program 7

Count Occurrences

```python
name = input()

print(name.count("$"))
```



## Program 8

Odd or Even

```python
num = int(input())

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```



## Program 9

Greatest of Three Numbers

```python
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)
```


## Program 10

Multiple of 7

```python
num = int(input())

if num % 7 == 0:
    print("Multiple of 7")
else:
    print("Not Multiple of 7")
```



# Day 1 Summary

Topics Covered:

* Python Basics
* Variables
* Data Types
* Operators
* Input Function
* Type Conversion
* Strings
* String Functions
* Conditional Statements
* Ternary Operator

Practice Programs Completed: 10



Status:

Day 1 Completed Successfully

