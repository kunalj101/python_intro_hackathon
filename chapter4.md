---
title       : Data Munging in Python using Pandas
description : Pandas are the heart of data analysis in Python. This chapter get you started with Data Munging in Python using Pandas
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## Credit History has missing value or not ?

There are missing values in variables. We should first identify the variables have missing value then estimate those values wisely depending on the amount of missing values and the expected importance of variables. So, here our first task is to check the variable has missing values in the data set and how many observation has missing values.

```{python}

train['Credit_History'].isnull().sum()

```

* isnull() helps to check the observation has missing value or not (It returns a boolean value TRUE or FALSE)
* sum() used to return the number of records have missing values

*** =instructions
- Apply isnull() to check the observation has null value or not 
- Check number of missing values is greater then 0 or not


*** =hint
Use train['Self_Employed'].isnull().sum() to check number of missing values



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

# How many missing values in variable "Self_Employed" ?
n_missing_value_Self_Employed = train['Self_Employed']._____.sum()

# Variable Loan amount has missing values or not?
LoanAmount_have_missing_value = train['LoanAmount'].isnull().sum() > ____


```

*** =solution

```{python}

# How many missing values in variable "Self_Employed" ?
n_missing_value_Self_Employed = train['Self_Employed'].isnull().sum()

# Variable Loan amount has missing values or not?
LoanAmount_have_missing_value = train['LoanAmount'].isnull().sum() > 0


```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# How many missing values in variable "Self_Employed" ?
test_object("n_missing_value_Self_Employed")

# Variable Loan amount has missing values or not?
test_object("LoanAmount_have_missing_value")

success_msg("Great work!")
```



--- type:NormalExercise lang:python xp:100 skills:1 key:4abbcb0b8d
## How many variables have missing values?

Till now, we have checked the variable has missing value or not? Next action is to check how many variables has missing value. One way of doing this check for each individual variable but it would not be easy if we have hundred of columns. This action can be performed simply by using isnull() on dataframe object.

```{python}

train.isnull().sum()

```

This statement will return the columns names with number of observation having missing (null) values.

<center><img src="http://www.analyticsvidhya.com/wp-content/uploads/2016/06/Missing_Values.png"></center>

*** =instructions
Apply isnull().sum() with test dataset



*** =hint
Use test.isnull().sum() to check number of missing values



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

# Check variables have missing values in test data set
number_missing_values_test_data = _____.isnull()._____()

```

*** =solution

```{python}

# Check variables have missing values in test data set
number_missing_values_test_data = test.isnull().sum()

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Check variables have missing values in test data set
test_object("number_missing_values_test_data")


success_msg("Great work!")
```


--- type:NormalExercise lang:python xp:100 skills:1 key:fd3cdcb726
## Impute missing values of LoanAmount?

There are multiple ways to fill the missing values of continuous variables, you can go with mean, median or estimate values based on other features of data set. Here to impute missing values of loan amount, we would go with imputing by mean value (Mean of available values of LoanAmount).

```{python}

train['LoanAmount'].fillna(train['LoanAmount'].mean(), inplace=True)

```

*** =instructions
- Impute missing values with a specific value 168
- Impute missing value with median



*** =hint
Use test['LoanAmount'].fillna(test['LoanAmount'].median(), inplace=True)


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

# Impute missing value of LoanAmount with 168
train['LoanAmount'].fillna(______, inplace=True)

# Impute missing value of LoanAmount with median for test data set
test['LoanAmount'].fillna(test['LoanAmount']._______, inplace=True)


```

*** =solution

```{python}

# Impute missing value of LoanAmount with 168
train['LoanAmount'].fillna(168, inplace=True)

# Impute missing value of LoanAmount with median for test data set
test['LoanAmount'].fillna(test['LoanAmount'].median(), inplace=True)

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Impute missing value of LoanAmount with 168
#test_object(“train['LoanAmount']”)

# Impute missing value of LoanAmount with median for test data set
#test_object(“test['LoanAmount']”)

success_msg("Great work!")
```




--- type:NormalExercise lang:python xp:100 skills:1 key:c0f63b52d5
## Dealing with missing values

There are missing values in some variables. We should estimate those values wisely depending on the amount of missing values and the expected importance of variables.

#### Identifying missing values

Imputing missing values in all the variables is important because most of the models don’t work with missing data and even if they do, imputing them helps more often than not. So, let us check the number of nulls / NaNs in the dataset for all variables.

```{python}

train.isnull().sum()

```

#### Imputing missing values
There are numerous ways to fill the missing values of loan amount – the simplest being replacement by mean for continuous variables, which can be done by following code:

```{python}

train['LoanAmount'].fillna(train['LoanAmount'].mean(), inplace=True)


```

And for categorical variables, we look at the frquency table and impute with value has higher frequency because there is a high probability of success. For example, if you look at distribution of Self_Employed 500 out of 582 which is ~86% of total values falls under category "No". Here we will replace missing values of Self_Employed with "No".

```{python}

df['Self_Employed'].fillna('No',inplace=True)

```

*** =instructions
- Check output of train.isnull().sum() is > 0 or not and apply sum over it to return number of variable(s) having missing values 
- Use median() to impute with  median values of numeric variables
- Look at frequency distribution of Self_Employed to identify more frequent category


*** =hint
- Use sum( train.isnull().sum()) > 0) to check count of variable having missing values 
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

# Number of variables with missing values
variables_missing_value = sum( train._____().sum() > 0 )


# Impute missing value of Loan_Amount_Term with median
train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].______(), inplace=True)

# Impute missing value of Self_Employed with more frequent category
train['Self_Employed']._____('No',inplace=True)

 

```

*** =solution

```{python}

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Number of variables with missing values
variables_missing_value = sum( train.isnull().sum() > 0 )


# Impute missing value of Loan_Amount_Term with median
train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].median(), inplace=True)

# Impute missing value of Self_Employed with more frequent category
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


# Impute missing value of Self_Employed with more frequent category


success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:2607b0ce32

## Treat extreme values of LoanAmount and ApplicantIncome?

Let’s analyze LoanAmount first. Since the extreme values are practically possible, i.e. some people might apply for high value loans due to specific needs. 

```{python}

train ['LoanAmount'].hist(bins=20)

```
<center><img src="http://www.analyticsvidhya.com/wp-content/uploads/2016/06/Capture_LoanAmount.png"></center>

So instead of treating them as outliers, let’s try a log transformation to nullify their effect:

```{python}

import numpy as np
train ['LoanAmount_log'] = np.log(train['LoanAmount'])
train ['LoanAmount_log'].hist(bins=20)

```
<center><img src="http://www.analyticsvidhya.com/wp-content/uploads/2016/01/7.-loan-log.png"></center>


Now the distribution looks much closer to normal and effect of extreme values has been significantly subsided.

*** =instructions
- Add both ApplicantIncome and CoapplicantIncome as TotalIncome
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


--- type:NormalExercise lang:python xp:100 skills:1 key:2c1cf7aa90
## Data preparation for building a predictive model?

In Python, Scikit-Learn (sklearn) is the most commonly used library for model building. I encourage you to get a refresher on sklearn through this <a href="http://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/">article</a>. It has gathered a lot of interest recently as a choice of language for data analysis. There are few pre-requisite for scikit learn library:

* Treat missing values
* All inputs must be numeric
 
To convert all non-numeric variables to number, following code will help:

```{python}

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

train['Gender'] = le.fit_transform(train['Gender'])

```

*** =instructions
- Impute missing values of categorical variables with higher frequent categories of variable
- Impute missing values of continuous variables with mean
- Convert all non-numeric variables to numbers using LabelEncoder() 


*** =hint
- Use similar expression like train['Gender'].fillna('Male',inplace=True) for categorial variable
- Use similar expressin like train['LoanAmount'].fillna(train['LoanAmount'].mean(), inplace=True) for continuous


*** =pre_exercise_code

```{python}

# The pre exercise code runs code to initialize the user's workspace. You can use it for several things:

# Import library pandas
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Import training file
train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")

# Import testing file
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

```

*** =sample_code

```{python}

from sklearn.preprocessing import LabelEncoder

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Impute missing values for Gender
train['Gender'].fillna('_____',inplace=True)

# Impute missing values for Loan_Amount
train['LoanAmount'].fillna(train['LoanAmount'].______(), inplace=True)

# Perform label encoding for Property_Area
le = LabelEncoder()
train['Property_Area'] = le.________(train['Property_Area'])

```

*** =solution

```{python}

# Training and Testing data set is loaded in variable train and test dataframe respectively

# Impute missing values for Gender
train['Gender'].fillna('Male',inplace=True)

# Impute missing values for Loan_Amount
train['LoanAmount'].fillna(train['LoanAmount'].mean(), inplace=True)

# Perform label encoding for Property_Area
le = LabelEncoder()
train['Property_Area'] = le.fit_transform(train['Property_Area'])


```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Impute missing values for Gender


# Impute missing values for Loan_Amount


# Perform label encoding for Property_Area


success_msg("Great work!")
```
