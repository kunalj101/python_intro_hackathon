---
title       : Exploratory analysis in Python using Pandas
description : We start with the first step of data analysis - the exploratory data analysis.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## Who is eligible for loan?

Dream Housing Finance company deals in all home loans. They have presence across all urban, semi urban and rural areas. Customer first apply for home loan after that company validates the customer eligibility for loan. Company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form.  

Let's start with loading in the training and testing set into your python environment. You will use the training set to build your model, and the test set to validate it. The data is stored on the web as CSV files; their URLs are already available as character strings in the sample code. You can load this data with the pandas.read_csv() function, it converts the data set to python dataframe. Python dataframe likes a spreadsheet or SQL table.


*** =instructions
- After importing the library "Pandas" (import pandas as pd), you read the dataset using function pd.read_csv()
- You can use train_url to load training dataset in train (dataframe)
- You can use test_url to load training dataset in test (dataframe)
- train.head(n) helps to look at top n observation
- train.tail(n) helps to look at bottom n observation


*** =hint
- Use len(dataframe) to return the total observations in the dataframe 
- Use len(dataframe.columns) to return the total available columns in the dataframe


*** =pre_exercise_code

```{python}

# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:

# Import library pandas
import pandas as pd

# Import training file
train = pd.read_csv("https://drive.google.com/folderview?id=0BxdtQGPPnMfjUWpsY3NYQy1JV3c&usp=sharing/train.csv")

# Import testing file
test = pd.read_csv("https://drive.google.com/folderview?id=0BxdtQGPPnMfjUWpsY3NYQy1JV3c&usp=sharing/test.csv")

```

*** =sample_code

```{python}

# import library pandas
import pandas as pd

# Import training data as train
train = pd.read_csv("https://drive.google.com/folderview?id=0BxdtQGPPnMfjUWpsY3NYQy1JV3c&usp=sharing/train.csv")

# Import testing data as test
test = pd.read_csv("https://drive.google.com/folderview?id=0BxdtQGPPnMfjUWpsY3NYQy1JV3c&usp=sharing/test.csv")

# Print top 5 observation of training dataset


# Store total number of observation in training dataset
train_length =

# Store total number of columns in testing data set
test_col = 

```

*** =solution

```{python}

import pandas as pd

# Import training data as train
train = pd.read_csv("https://drive.google.com/folderview?id=0BxdtQGPPnMfjUWpsY3NYQy1JV3c&usp=sharing/train.csv")

# Import testing data as test
test = pd.read_csv("https://drive.google.com/folderview?id=0BxdtQGPPnMfjUWpsY3NYQy1JV3c&usp=sharing/test.csv")

# Print top 5 observation of test dataset
print (train.head(5))

# Store total number of observation in training dataset
train_length = len(train)

# Store total number of columns in testing data set
test_col = len(test.columns())

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for evaluating top 5 heading of dataframe


# Test for total observation in training dataset
test_object("train_length")

# Test for total columns in testing dataset
test_object("test_col")

success_msg("Great work!")
```

