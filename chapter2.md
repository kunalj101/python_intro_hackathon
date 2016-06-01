
title       : Python Libraries and data structures
description : In this chapter, we will take you through the libraries we commonly use in data analysis and introduce some of the most common data structures to you.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3

## Create a list

List is one of the most versatile data structure in Python. A list can simply be defined by writing a list of comma separated values in square brackets. Lists might contain items of different types. Python lists are mutable and individual elements of a list can be changed.

*** =instructions
- Individual elements of a list can be accessed by writting an index number in square bracket. First index of list starts with 0 (zero) not 1.
- A range of element can be accessed by having start index and end index


*** =hint
- Use AV[0] to select the first element of a list AV. 
- Use AV[-1] to select the last element of a list AV. 
- Use AV[1:3] to select second to fourth elements of a list AV.


*** =pre_exercise_code
```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}

# Create a list of squared numbers
squares_list = [0, 1, 4, 9, 16, 25]

# Now write a code to create list of odd numbers and store it into a variable odd_numbers
odd_numbers=

# Print first element of squares_list
print (squares_list[0])

# Write a code to store fouth element of squares_list in variable fourth_value
fourth_value=

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

# Write a code to store fouth element of squares_list in variable fourth_value
fourth_value=squares_list[3]

# Print second to fourth elements of squares_list
print (squares_list[1:3])
```

*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check list odd_numbers
test_object("odd_numbers")

# Check fourth value of squares_list
test_object("fourth_value")

# Check second to fourth elements"
test_output_contains("[1, 4]", pattern = False)
success_msg("Great work!")
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:92d2fb80bf
## A really bad movie

Have a look at the plot that showed up in the viewer to the right. Which type of movies have the worst rating assigned to them?

*** =instructions
- Long movies, clearly
- Short movies, clearly
- Long movies, but the correlation seems weak
- Short movies, but the correlation seems weak

*** =hint
Have a look at the plot. Do you see a trend in the dots?

*** =pre_exercise_code
```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:

# 1. Pre-load packages, so that users don't have to do this manually.
import pandas as pd
import matplotlib.pyplot as plt

# 2. Preload a dataset. The code below will read the csv that is stored at the URL's location.
# The movies variable will be available in the user's console.
movies = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv")

# 3. Create a plot in the viewer, that students can check out while reading the exercise
plt.scatter(movies.runtime, movies.rating)
plt.show()
```

*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the
# pythonwhat Python package

msg_bad = "That is not correct!"
msg_success = "Exactly! The correlation is very weak though."

# Use test_mc() to grade multiple choice exercises.
# Pass the correct option (option 4 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(4, [msg_bad, msg_bad, msg_bad, msg_success])
```

## Create a String

Strings can simply be defined by use of single ( ‘ ), double ( ” ) or triple ( ”’ ) inverted commas. Strings enclosed in tripe quotes ( ”’ ) can span over multiple lines and are used frequently in docstrings (Python’s way of documenting functions). \ is used as an escape character. Please note that Python strings are immutable, so you can not change part of strings.

*** =instructions

- Strings can be simply defined by single ('), double (") or triple (''') quotation.
- Strings characters can be accessed using index number (similar like list)
- Strings can be concatenated with other strings



*** =hint

- Use str[2] to select the third element of string str. 
- Use len(str) to return the length of string
- Use str1 + str2 to return the concatenated result of both strings str1 and str2



*** =pre_exercise_code

```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code

```{python}
# Create a string str
str = "Introduction with strings"

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
str = "Introduction with strings"

# Now store the length of string in varible str_len 
str_len=len(str)

# Print last seven characters of strings str
print (str[18:25])

str1 = "I am doing a course "Introduction to Hackathon using "
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




--- type:NormalExercise lang:python xp:100 skills:1 key:a7ff25d1f4
## Plot the movies yourself

Do you remember the plot of the last exercise? Let's make an even cooler plot!

A dataset of movies, `movies`, is available in the workspace.

*** =instructions
- The first function, `np.unique()`, uses the `unique()` function of the `numpy` package to get integer values for the movie genres. You don't have to change this code, just have a look!
- Import `pyplot` in the `matplotlib` package. Set an alias for this import: `plt`.
- Use `plt.scatter()` to plot `movies.runtime` onto the x-axis, `movies.rating` onto the y-axis and use `ints` for the color of the dots. You should use the first and second positional argument, and the `c` keyword.
- Show the plot using `plt.show()`.

*** =hint
- You don't have to program anything for the first instruction, just take a look at the first line of code.
- Use `import ___ as ___` to import `matplotlib.pyplot` as `plt`.
- Use `plt.scatter(___, ___, c = ___)` for the third instruction.
- You'll always have to type in `plt.show()` to show the plot you created.

*** =pre_exercise_code
```{python}
# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:

# 1. Preload a dataset. The code below will read the csv that is stored at the URL's location.
# The movies variable will be available in the user's console.
import pandas as pd
movies = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/introduction_to_r/movies.csv")

# 2. Preload a package
import numpy as np
```

*** =sample_code
```{python}
# Get integer values for genres
_, ints = np.unique(movies.genre, return_inverse = True)

# Import matplotlib.pyplot


# Make a scatter plot: runtime on  x-axis, rating on y-axis and set c to ints


# Show the plot

```

*** =solution
```{python}
# Get integer values for genres
_, ints = np.unique(movies.genre, return_inverse = True)

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Make a scatter plot: runtime on  x-axis, rating on y-axis and set c to ints
plt.scatter(movies.runtime, movies.rating, c=ints)

# Show the plot
plt.show()
```

*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check if the student changed the np.unique() call
# If it's not called, we know the student removed the call.
# If it's called incorrectly, we know the student changed the call.
test_function("numpy.unique",
              not_called_msg = "Don't remove the call of `np.unique` to define `ints`.",
              incorrect_msg = "Don't change the call of `np.unique` to define `ints`.")
# Check if the student removed the ints object
test_object("ints",
            undefined_msg = "Don't remove the definition of the predefined `ints` object.",
            incorrect_msg = "Don't change the definition of the predefined `ints` object.")

# Check if the student imported matplotlib.pyplot like the solution
# Let automatic feedback message generation handle the feedback messages
test_import("matplotlib.pyplot", same_as = True)

# Check whether the student used the scatter() function correctly
# If it's used, but incorrectly, tell them to check the instructions again
test_function("matplotlib.pyplot.scatter",
              incorrect_msg = "You didn't use `plt.scatter()` correctly, have another look at the instructions.")

# Check if the student called the show() function
# Let automatic feedback message generation handle all feedback messages
test_function("matplotlib.pyplot.show")

success_msg("Great work!")
```
