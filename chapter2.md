
title       : Python Libraries and data structures
description : In this chapter, we will take you through the libraries we commonly use in data analysis and introduce some of the most common data structures to you.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## Create a list

List is one of the most versatile data structure in Python. A list can simply be defined by writing a list of comma separated values in square brackets. Lists might contain items of different types. Python lists are mutable and individual elements of a list can be changed.

```{python}
Country =['INDIA','USA','GERMANY','UK','AUSTRALIA']

Temperature =[44, 28, 20, 18, 25, 45, 67]
```
Above, we have created two lists, one for Country names and other one for temarature. 

*** =instructions
- Individual elements of a list can be accessed by writting an index number in square bracket. First index of list starts with 0 (zero) not 1.
- A range of element can be accessed by having start index and end index but it does not return the value available at end index,


*** =hint
- Use AV[0] to select the first element of a list AV. 
- Use AV[1:3] to select second to third element of a list AV.


*** =pre_exercise_code
```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}

# Create a list of squared numbers
squares_list = [0, 1, 4, 9, 16, 25]

# Now write a code to create list of first five odd numbers and store it into a variable odd_numbers
odd_numbers=

# Print first element of squares_list
print (squares_list[0])

# Print second to fourth elements of squares_list

```

*** =solution
```{python}

# Create a list of squared numbers
squares_list = [0, 1, 4, 9, 16, 25]

# Now write a code to create list of first five odd numbers and store it into a variable odd_numbers
odd_numbers = [1, 3, 5, 7, 9]

# Print first element of squares_list
print (squares_list[0])

# Print second to fourth elements of squares_list
print (squares_list[1:4])
```

*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for list of odd_numbers
test_object("odd_numbers")

# Check second to fourth elements"
test_output_contains("[1, 4, 9]", pattern = False)
success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:c7f91e389f
## Create a String

Strings can simply be defined by use of single ( ‘ ), double ( ” ) or triple ( ”’ ) inverted commas. Strings enclosed in triple quotes ( ”’ ) can span over multiple lines. Please note that Python strings are immutable, so you can not change part of strings.

```{python}
String =" Strings elements can also be accessed using index number like list"

print (String[0:8])

#Above print command display Strings on screen.

```


*** =instructions

- len function returns the lenght of string
- Strings characters can be accessed using index number (similar like list)
- Strings can be concatenated with other strings using '+' operator



*** =hint

- Use str[2] to select the third element of string str 
- Use len(str) to return the length of string
- Use str1 + str2 to return the concatenated result of both strings str1 and str2



*** =pre_exercise_code

```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}
# Create a string str
str1 = "Introduction with strings"

# Now store the length of string in varible str_len 
str_len =

# Print last seven characters of strings str


str1 = "I am doing a course Introduction to Hackathon using "
str2 = "Python"

# Write a code to store concatenated string of str1 and str2 into variable str3
str3 =

```

*** =solution

```{python}

# Create a string str
str1 = "Introduction with strings"

# Now store the length of string in varible str_len 
str_len=len(str1)

# Print last seven characters of strings str
print (str1[18:25])

str1 = "I am doing a course Introduction to Hackathon using "
str2 = "Python"

# Write a code to store concatenated string of str1 and str2 into variable str3
str3= str1 + str2
```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check length of strings
test_object("str_len")

# Check last seven characters
test_output_contains("strings", pattern = False)

# Check concatenated strings"
test_object("str3")
success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:377e9324f2
## Create a Dictionary

Dictionary is an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.

```{python}
DICT = {'Name':'Kunal', 'Company':'Analytics Vidhya'}

#Dictionary elements can be accessed by "keys"

print (DICT['Name'])

#Above print statement will print Kunal

```

In dictonary "DICT", Name and Company are dictionary keys where as "Kunal" and "Analytics Vidhya" are values.

*** =instructions

- To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value
- Dictionary can be updated by adding a new entry or a key-value pair, modifying or deleting an existing entry

*** =hint

- Use dict['Keys'] = new_value to update the existing value
- Use dict.keys() to access all keys of dictionary dict
- Use dict.values() to access all values of dictionary dict


*** =pre_exercise_code

```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}

# Create a dictionary
dict1 = {'Name': 'Max', 'Age': 16, 'Sports': 'Cricket'}

# Update the value of Age to 18


# Print the value of Age


# Print all the keys of dictionary dict1


```

*** =solution

```{python}

# Create a dictionary
dict1 = {'Name': 'Max', 'Age': 16, 'Sports': 'Cricket'}

# Update the value of Age to 18
dict1['Age'] = 18

# Print the value of Age
print (dict1['Age'])

# Print all the keys of dictionary dict
print (dict1.keys())

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check value of Age
test_output_contains("18", pattern = False)

# Check keys of dictionary
test_output_contains("dict_keys(['Name', 'Age', 'Sports'])", pattern = False)

success_msg("Great work!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
## Why python libraries are useful?

Lets take one step ahead in our journey to learn Python by getting acquainted with some useful libraries. The first step is obviously to learn to import them into our environment. There are several ways of doing so in Python:

```{python}
import math as m

from math import *
```

In the first manner, we have defined an alias m to library math. We can now use various functions from math library (e.g. factorial) by referencing it using the alias m.factorial().

In the second manner, you have imported the entire name space in math i.e. you can directly use factorial() without referring to math.

Following are a list of libraries, you will need for any scientific computations and data analysis:

* <a href="http://www.numpy.org/"> Numpy </a>
* <a href="https://www.scipy.org/"> Scipy </a>
* <a href="http://pandas.pydata.org/pandas-docs/stable/"> Pandas </a>
* <a href="http://matplotlib.org/"> Matplotlib </a>
* <a href="http://scikit-learn.org/"> Scikit Learn </a>



##### Which of the following is a valid import statement for below code?
```{python}
print (factorial(5))
```

*** =instructions
- import math
- from math import factorial
- import math.factorial

*** =hint
Python's from statement lets you import specific attributes from a module into the current namespace.

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad = "Read about importing libraries in python"
msg_success = "Good Job!"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(2, [msg_bad, msg_success, msg_bad]) 
```


--- type:NormalExercise lang:python xp:100 skills:1 key:50c9218dac
## Why conditional statement is required?

Conditional statements, these are used to execute code fragments based on a condition. The most commonly used construct is if-else, with following syntax:

```{python}

if [condition]:
  __execution if true__
else:
  __execution if false__ 
```

*** =instructions

- Store the length of squares_list to square_len
- Use the if statement to perform one action if one thing is true,or any other actions, if something else is true


*** =hint

- Use <, >, <=, >=, == and != for comparison
- Use len(list) to return  length of string


*** =pre_exercise_code

```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}
# Create a two integer variables a and b
a=3
b=4

# if a is greater than b print a-b else a+b
if a > b:
    print (a-b)
else:
    print (a+b)

# Create a list of squared numbers
squares_list = [0, 1, 4, 9, 16, 25]

# Store the length of squares_list in square_len
square_len = 

# if square_len is less than 5 then print "Less than 5" else "Greater than 5"
if square_len < ___:
    print ("__________")
else:
    print ("__________")


```

*** =solution

```{python}
# Create a two integer variables a and b
a=3
b=4

# if a is greater than b print a-b else a+b
if a > b:
    print (a-b)
else:
    print (a+b)

# Create a list of squared numbers
squares_list = [0, 1, 4, 9, 16, 25]

# Store the length of squares_list in square_len
square_len = len(squares_list)

# if square_len is less than 5 then print "Less than 5" else "Greater than 5"
if square_len < 5:
    print ("Less than 5")
else:
    print ("Greater than 5")

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check length of strings
test_object("square_len")

# Check last seven characters
test_output_contains("Greater than 5", pattern = False)

success_msg("Great work!")
```


--- type:NormalExercise lang:python xp:100 skills:1 key:c1b7c2fd5c
## How iterative statement does help?

Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well. Repeated execution of a set of statements is called iteration.

Like most languages, Python also has a FOR-loop which is the most widely used method for iteration. It has a simple syntax:

```{python}

for i in [Python Iterable]:
  expression(i)

```
“Python Iterable” can be a list or other advanced data structures which we will explore in later sections. Let’s take a look at a simple example, determining the factorial of a number.

*** =instructions

- Use list.append(<element>) to append values in a list
- Iterate over list to access each element of list



*** =hint

- Use <, >, <=, >=, == and != for comparison
- Use len(list) to return  length of string
- % operator helps to return remainder e.g. 4 % 3 would be 1

*** =pre_exercise_code

```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}
# Create a list with first five numbers
ls=[]
for x in range(5):
    ls.append(x)
    
sum=0
# Store sum all even numbers of the list ls in sum

for x in ls: 
    if ______: 
        sum += x

```

*** =solution

```{python}
# Create a list with first five numbers
ls=[]
for x in range(5):
    ls.append(x) # append a value to a list
    
sum=0
# Store sum all even numbers of the list ls in sum

for x in ls: 
    if x%2==0: 
        sum += x

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check length of strings
test_object("sum")

success_msg("Great work!")
```
