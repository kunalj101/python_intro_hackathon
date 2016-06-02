---
title       : Data Munging in Python using Pandas
description : Pandas are the heart of data analysis in Python. This chapter get you started with Data Munging in Python using Pandas
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## Dealing with missing values

There are missing values in some variables. We should estimate those values wisely depending on the amount of missing values and the expected importance of variables.

### Identifying missing values

Imputing missing values in all the variables is important because most of the models don’t work with missing data and even if they do, imputing them helps more often than not. So, let us check the number of nulls / NaNs in the dataset for all variables.

```{python}

train.apply(lambda x: sum(x.isnull()),axis=0) 

```

Read more about lambda <a href="http://www.python-course.eu/lambda.php">here</a>.

### Imputing missing values
There are numerous ways to fill the missing values of loan amount – the simplest being replacement by mean for continuous variables, which can be done by following code:

```{python}

train['LoanAmount'].fillna(train['LoanAmount'].mean(), inplace=True)

```
And for categorical variables, we look at the frquency table and impute with value has higher frequency because there is a high probability of success. For example, if you look at distribution of Self_Employed 500 out of 582 which is ~86% of total values falls under category "No". Here we will replace missing values of Self_Employed with "No".

```{python}

df['Self_Employed'].fillna('No',inplace=True)

```

*** =instructions
- Use train.apply(lambda x: sum(x.isnull()),axis=0) with comparison operator to check variable has missing values
- Look at frequency distribution of Gender to identify more frequent category


*** =hint
- Use len(dataframe) to return the total observations in the dataframe 
- Use len(dataframe.columns) to return the total available columns in the dataframe


*** =pre_exercise_code

```{python}

# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:

# Import library pandas
import pandas as pd

# Import training file
train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")

# Import testing file
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

```

*** =sample_code

```{python}

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Number of variables with missing values
variables_missing_value = 


# Impute missing value of Loan_Amount_Term with median


# Impute missing value of Gender with more frequent category

 

```

*** =solution

```{python}

import pandas as pd

# Import training data as train
train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")

# Import testing data as test
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

# Print top 5 observation of test dataset
print (train.head(5))

# Store total number of observation in training dataset
train_length = len(train)

# Store total number of columns in testing data set
test_col = len(test.columns)

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
