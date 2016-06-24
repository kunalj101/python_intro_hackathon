---
title       : Introduction to Python for Data Analysis
description : This chapter will get you started with Python for Data Analysis. We will cover the reasons to learn Data Science using Python, provide an overview of the Python ecosystem and get you to write your first code in Python!
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
## Why learn Python for data analysis?

Python (an interpreted language) has gathered a lot of interest recently as a choice of language for data analysis. Here are some reasons which go in favour of learning Python:

* Open Source – free to install and use
* Awesome online community - latest algorithms come to Python in a matter of days
* Easy to learn
* Can become a common language for data science and production of web-based analytics products

####Which of the following is not a reason to learn Python for Data Analysis?


*** =instructions
- Python is easy to learn.
- Python is interpreted language, hence the computation times can be high compared to compiler based languages in some cases.
- Python has good libraries for data science.
- It is production ready language (from web & software perspective).

*** =hint
Interpreted languages are typically easier to learn, but take longer computational time than compiler based languages. 

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "That is a good reason to learn Python! Think again"
msg_success = "Exactly! Since Python is an interpreted language, the computation times can be on the higher side compared to other compiler based language."

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(2, [msg_bad1, msg_success, msg_bad1, msg_bad1]) 
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:db5fe12eff
## Python 2.7 vs. Python 3.5?

You will come across this question soon after you start using Python. Both the ecosystems have their pros and cons.

**Benefits of Python 2.7**

* Awesome online community. Easier to find answers when you get stuck at places.
* Tonnes of third party libraries

**Benefits of Python 3.5**

* Cleaner and faster
* It is the future!

####Which version of Python would you recommend if you need to use several third party libraries?


*** =instructions
- Python 2.7
- Python 3.5
- Should work on both

*** =hint
If you need several third party tools, you should look for a version which has higher community support and integrations.

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "Python 3.5 is newer and has lesser third party packages"
msg_success = "Python 2.7 has much higher compatibility with third party libraries."
msg_bad2 = "Think again! One of them is better than the other in this scenario"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(1, [msg_success, msg_bad1, msg_bad2]) 
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:2f83694db6
## How to install Python?

While DataCamp provides an awesome interface to get you started, you will need to run a local instance of Python for any serious Data Science work. The simplest way would be to download <a href="https://www.continuum.io/downloads"> Anaconda</a>. It consists of most of the libraries you would need and removes any version conflicts.
I strongly recommend this for beginners. For this course, we will be using Python 3.x


####Have you installed a local instance of Python on your machine?


*** =instructions
- Yes
- No
- I need some help

*** =hint
Download <a href="https://www.continuum.io/downloads"> Anaconda</a>

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad = "You should install a Python instance locally before going forward"
msg_success = "Great! You are all set to go ahead"
msg_help = "Drop us a line at help@analyticsvidhya.com"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(1, [msg_success, msg_bad, msg_help]) 
```

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## Run a few simple programs in Python

Time to get our hands dirty now. We will use Python to run some simple programs!

*** =instructions
- The first line just adds 2 numbers (1 & 2). Write a simple program to add number 3 and number 4 and assign it to a variable addition2
- Print "Hello World!" on the console


*** =hint
- Think how would you write simple addition.
- Make sure you assign the sum to the variable 'addition2'
- Remember that the message to be printed should be enclosed in " "
- Remember - Python is case sensitive. Check your cases and white spaces

*** =pre_exercise_code
```{python}
# The pre-exercise code runs code to initialize the user's workspace. You can use it for several things:
```

*** =sample_code
```{python}
# Add 1 & 2 and assign it to addition
addition = 1 + 2
# Now write a code to add 3 & 4 and assign to addition2


# Print a message
print("Welcome to the joint course from Analytics Vidhya and DataCamp")

# Now write a code to Print "Hello World!"

```


*** =solution
```{python}
# Add 1 & 2 and assign it to addition
addition = 1 + 2
# Now write a code to add 3 & 4 and assign to addition2
addition2 = 3 + 4

# Print a message
print("Welcome to the joint course from Analytics Vidhya and DataCamp")

# Now write a code to Print "Hello World!"
print("Hello World!")
```

*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check if the student typed 3 + 4
test_object("addition2")

# Check if the student printed "Hello World!"
test_output_contains("Hello World!", pattern = False, incorrect_msg = “Your output wasn’t exactly what we were looking for.")
success_msg("Great work!")
```
