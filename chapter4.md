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
- Use train.apply(lambda x: sum(x.isnull()),axis=0) with comparison operator to check variable has missing value or not
- Look at frequency distribution of Gender to identify more frequent category


*** =hint
- Use sum(train.apply(lambda x: sum(x.isnull()),axis=0) > 0) to check count of variable having missing values 
- Use median() inplace of mean() in expression train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].median(), inplace=True) to impute with median


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

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Number of variables with missing values
variables_missing_value = sum(train.apply(lambda x: sum(x.isnull()),axis=0) > 0)


# Impute missing value of Loan_Amount_Term with median
train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].median(), inplace=True)

# Impute missing value of Gender with more frequent category
train['Self_Employed'].fillna('No',inplace=True)

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Number of variables with missing values
test_object("variables_missing_value")

# Impute missing value of Loan_Amount_Term with median


# Impute missing value of Gender with more frequent category


success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:2607b0ce32

## Treat extreme values of LoanAmount and ApplicantIncome?

Let’s analyze LoanAmount first. Since the extreme values are practically possible, i.e. some people might apply for high value loans due to specific needs. So instead of treating them as outliers, let’s try a log transformation to nullify their effect:

```{python}

import numpy as np
train ['LoanAmount_log'] = np.log(train['LoanAmount'])
train ['LoanAmount_log'].hist(bins=20)

```
<center><img src="http://www.analyticsvidhya.com/wp-content/uploads/2016/01/7.-loan-log.png"></center>


Now the distribution looks much closer to normal and effect of extreme values has been significantly subsided.

*** =instructions
- Combine both ApplicantIncome and CoapplicantIncome as TotalIncome
- Take log transformation of TotalIncome to deal with extreme values


*** =hint
- df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
- df['TotalIncome_log'] = np.log(df['TotalIncome'])


*** =pre_exercise_code

```{python}

# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:

# Import library pandas
import pandas as pd
import numpy as np

# Import training file
train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")

# Import testing file
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

```

*** =sample_code

```{python}

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Add both ApplicantIncome and CoapplicantIncome to TotalIncome
train['TotalIncome'] = 

# Perform log transformation of TotalIncome to make it closer to normal
train['TotalIncome_log']=


```

*** =solution

```{python}

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Add both ApplicantIncome and CoapplicantIncome to TotalIncome
train['TotalIncome'] = train['ApplicantIncome'] + train['CoapplicantIncome']

# Perform log transformation of TotalIncome to make it closer to normal
train['TotalIncome_log'] = np.log(train['TotalIncome'])


```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Add both ApplicantIncome and CoapplicantIncome to TotalIncome
#test_object("train['TotalIncome']")

# Perform log transformation of TotalIncome to make it closer to normal


success_msg("Great work!")
```

