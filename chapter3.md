---
title       : Exploratory analysis in Python using Pandas
description : We start with the first step of data analysis - the exploratory data analysis.
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

