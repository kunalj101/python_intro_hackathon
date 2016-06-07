---
title       : Expert advice to imporove model performance
description : This chapter will help to understand the approach of data science experts, "How they do approach a challenge ?", "How to select a right algorithm ?", "How to combine outputs of multiple algorithms ?" and "How to select the right value of model parameter also known as parameter tuning ?".
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
## How to approach a challenge?

The model development cycle goes through various stages, starting from data collection to model building. Most of us admits that data exploration needs more attention to unleasehed the hidden story of data but before exploring the data to understand relationships (in variables), It’s always recommended to perform hypothesis generation. (To know more  about hypothesis generation, refer to <a href =" http://discuss.analyticsvidhya.com/t/why-and-when-is-hypothesis-generation-important/2109"> this link</a>). 

It is important that you spend time thinking on the given problem and gaining the domain knowledge. So, how does it help?

This practice usually helps in building better features later on, which are not biased by the data available in the data-set. This is a crucial step which usually improves a model’s accuracy.

At this stage, you are expected to apply structured thinking to the problem i.e. a thinking process which takes into consideration all the possible aspects of a particular problem.


####Which of the following has the right order of model building life cycle?


*** =instructions
- Data Collection --> Data Exploration --> Hypothesis Generation --> Model Building --> Prediction
- Data Collection --> Hypothesis Generation --> Data Exploration --> Model Building --> Prediction
- Hypothesis Generation --> Data Collection --> Data Exploration --> Model Building --> Prediction

*** =hint
Always perform hypothesis generation before data collection and exploration, it also helps you to collect right data

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "Think again!"
msg_success = "Exactly! we always do Hypothesis generation before data collection and exploration"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(3, [msg_bad1, msg_bad1, msg_success]) 
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:01167ddb1f
## Feature Engineering

This step helps to extract more information from existing data. New information is extracted in terms of new features. These features may have a higher ability to explain the variance in the training data. Thus, giving improved model accuracy.

Feature engineering is highly influenced by hypotheses generation. Good hypothesis results into good feature. That’s why, experts always suggest to invest quality time in hypothesis generation. Feature engineering process can be divided into two steps:

* Feature Transformation
* Feature Creation

##### Feature Transformation: 

There are various scenarios where feature transformation is required:
* Changing the scale of a variable from original scale to scale between zero and one.
* Some algorithms works well with normally distributed data. Therefore, we must remove skewness of variable(s). There are methods like log, square root or inverse of the values to remove skewness
* Binning of numerical variables

##### Feature Creation: 

Deriving new variable(s) from existing variables is known as feature creation. It helps to unleash the hidden relationship of a data set. Let’s say, we want to predict the number of transactions in a store based on transaction dates. Here transaction dates may not have direct correlation with number of transaction, but if we look at the day of a week, it may have a higher correlation. In this case, the information about day of a week is hidden. We need to extract it to make the model better.

#### Creating a variable based on mathematical computation of existing three variables is a method of?


*** =instructions
- Feture Transformation
- Feature Creation
- Feature Selection


*** =hint
Always perform hypothesis generation before data collection and exploration, it also helps you to collect right data

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "Think again!"
msg_success = "Yes! Creating a new feature out of existing ones is known as feature creation"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(2, [msg_bad1, msg_success, msg_bad1]) 
```
