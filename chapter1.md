---
title       : Introduction to Python for Data Analysis
description : This chapter will get you started with Python for Data Analysis. We will cover the basics of the language you will need and an overview of the Python ecosystem.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
## Why learn Python for data analysis?

Python has gathered a lot of interest recently as a choice of language for data analysis. Here are some reasons which go in favour of learning Python:

* Open Source – free to install
* Awesome online community
* Easy to learn
* Can become a common language for data science and production of web based analytics products

Which of the following is not a reason to learn Python for Data Analysis?


*** =instructions
- Python is easy to learn
- Python is interpreted language, hence the computation times can be high compared to compiler based languages in some cases.
- Python has good libraries for data science
- It is production ready language (from web & softare perspective)

*** =hint
Have a look at the text. Do you see your answer?

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad = "That is not correct!"
msg_success = "Exactly! Since Python is an interpretted language, the computation times can be on the higher side."

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(2, [msg_bad, msg_bad, msg_bad, msg_success]) 
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
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
Have a look at the text. Do you see your answer?

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad = "That is not correct!"
msg_success = "Python 2.7 has much higher compatibility with third party libraries."

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(1, [msg_bad, msg_bad, msg_bad, msg_success]) 
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
## How to install Python?

While DataCamp provides an awesome interface to get you started, you will need to run local instance of Python for any serious Data Science work. The simplest way would be to download <a href="https://www.continuum.io/downloads"> Anaconda</a>. It consists of most of the libraries you would need and removes any version conflicts.
I strongly recommend this for beginners.


####Have you installed a local instance of Python on your machine?


*** =instructions
- Yes
- No
- I need some help

*** =hint
Have a look at the text. Do you see your answer?

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad = "You should install a Python instance locally"
msg_success = "Great! You are all set to go ahead"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(1, [msg_bad, msg_bad, msg_bad, msg_success]) 
```

