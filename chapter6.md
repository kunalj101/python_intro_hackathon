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

msg_bad1 = "That is a good reason to learn Python! Think again"
msg_success = "Exactly! Since Python is an interpretted language, the computation times can be on the higher side compared to other compiler based language."

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(3, [msg_bad1, msg_bad1, msg_success]) 
```
