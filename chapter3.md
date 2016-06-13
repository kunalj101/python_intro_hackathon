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
- train.head(n) helps to look at top n observation
- len(DataFrame) returns the total number of observations
- DataFrame.columns returns the total columns heading of the data set


*** =hint
- Use len(dataframe) to return the total observations
- Use len(dataframe.columns) to return the total available columns


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

# import library pandas
import pandas as pd

# Import training data as train
train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")

# Import testing data as test
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

# Print top 5 observation of training dataset in top5


# Store total number of observation in training dataset
train_length =

# Store total number of columns in testing data set
test_col = 

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
test_function("print", incorrect_msg = "Don't forget to print the first 5 observations of `train`!")

# Test for total observation in training dataset
test_object("train_length")

# Test for total columns in testing dataset
test_object("test_col")

success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:36c3190b26
## Understanding Data?

You can look at summary of numerical fields by using dataframe.describe(). It provides count, mean, standard deviation (std), min, quartiles and max in its output.

```{python}

dataframe.describe() 

```
For the non-numeric values (e.g. Property_Area, Credit_History etc.), we can look at frequency distribution. The frequency table can be printed by following command:

```{python}

df[column_name].value_counts()

```

*** =instructions

- Use `dataframe.describe()` to understand the distribution of numerical variables 
- Look at unique values of non-numeric values using `df[column_name].value_counts()`


*** =hint
- Store the output of `train.describe()` in a variable df
- Use `train['PropertyArea'].value_counts()` to look at frequency distribution


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

#Training and Testing data set are loaded in train and test dataframe respectively

# Look at the summary of numerical variables for train data set
df= train.________()
print (df)

# Print the unique values and their frequency of variable Property_Area
df1=train['Property_Area'].________()
print (df1)

```

*** =solution

```{python}

# Look at the summary of numerical variables for train data set
df = train.describe()
print (df)

# Print the unique values and their frequency of variable Property_Area
df1=train['Property_Area'].value_counts()
print (df1)

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for describe
test_object("df")

# Test for value_counts
test_object("df1")

success_msg("Great work!")
```


--- type:NormalExercise lang:python xp:100 skills:1 key:85c5d3a079
## Understanding distribution of numerical variables?

Now that we are familiar with basic data characteristics, let us study distribution of numerical variables. Let us start with numeric variable "ApplicantIncome".

Lets start by plotting the histogram of ApplicantIncome using the following commands:

```{python}

train['ApplicantIncome'].hist(bins=50)

```
Next, we can also look at box plots to understand the distributions. Box plot for ApplicantIncome can be plotted by


```{python}

train.boxplot(column='ApplicantIncome')

```

*** =instructions

- Use hist() with train['LoanAmount'] to plot histogram
- Use by=categorical_variable with box plot to look at distribution by categories

```{python}

train.boxplot(column='ApplicantIncome', by='Gender')

```

*** =hint
- train['LoanAmount'].hist()
- train.boxplot(column='LoanAmount', by = 'Gender' )


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

# Training and Testing dataset are loaded in train and test dataframe respectively
# Plot histogram for variable LoanAmount
train['LoanAmount']._____

# Plot a box plot for variable LoanAmount by variable Gender of training data set
train.boxplot(column='LoanAmount', by = ____)

```

*** =solution

```{python}


# Assumed training and testing dataset are loaded in train and test dataframe respectively
# Plot histogram for variable LoanAmount
train['LoanAmount'].hist()

# Plot a box plot for variable LoanAmount by variable Gender of training data set
train.boxplot(column='LoanAmount', by ='Gender' )

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for evaluating histogram


# Test for evaluating box plot


success_msg("Great work!")
```



--- type:NormalExercise lang:python xp:100 skills:1 key:708e937aea
## Understanding distribution of categorical variables?

We have looked at the distributions of ApplicantIncome and LoanIncome, now time for categorical variables in more details. For instance, lets see that Gender is affecting the loan status or not. This can be tested using cross-tabulation as shown below:

```{python}

pd.crosstab( train ['Gender'], train ["Loan_Status"], margins=True)

```
Next, we can also look at proportions can be more intuitive in making some quick insights. We can do this using the apply function. You can read more about cross tab and apply functions <a href="http://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/"> here</a>. 


```{python}

def percentageConvert(ser):
  return ser/float(ser[-1])

pd.crosstab(train ["Gender"], train ["Loan_Status"], margins=True).apply(percentageConvert, axis=1)

```

*** =instructions

- Use value_counts() with train['LoanStatus'] to look at the frequency distribution
- Use crosstab with Loan_Status and Credit_History to perform bi-variate analysis
 


*** =hint
- train['Loan_Status'].value_counts()['Y'] will return the loan approval rate





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

# Training and Testing dataset are loaded in train and test dataframe respectively

# Approved Loan in absolute numbers
loan_approval = train['Loan_Status'].________()['Y']

# Two-way comparison: Credit History and Loan Status
pd.________(train ["Credit_History"], train ["Loan_Status"], margins=True)



```

*** =solution

```{python}

# Assumed training and testing dataset are loaded in train and test dataframe respectively

# Approved Loan in absolute numbers
loan_approval = train['Loan_Status'].value_counts()['Y']

# Two-way comparison: Credit_History and Loan_Status
pd.crosstab(train ["Credit_History"], train ["Loan_Status"], margins=True)

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for Approved Loan in absolute numbers
test_object("loan_approval")


# Test for two way comparison Credit_History and Loan_Status




success_msg("Great work!")

```



