---
title       : Building a Predictive model in Python
description : We build our predictive models and make submissions to the AV DataHack platform in this section.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## First Step of Model Building

Till now, we have looked at the data exploartion, cleaning, feature engineering and pre processing steps of model building. Now, we will look at the methods of building a model. 

In this challengs "Loan Prediction", we need to classify customer in Loan status "Y" or "N" category based on available information about customer. Before jumping into model building steps, we need to follow below steps:
- Impute missing values of the data set
- Import required library (In python, we mostly use sklearn), this is a classification challenge so we will import module of classification algorithms
```{python}
    * from sklearn.linear_model import LogisticRegression #Logistic Rgression 
    * from sklearn.tree import DecisionTreeClassifier #Decision Tree
    * from sklearn.ensemble import RandomForestClassifier #Random Forest
```
- Convert categorical variables to numeric array because sklearn requires all inputs in numeric array


*** =instructions
- Import sklearn library and required model for model building
- Dataframes train_modified and test_modified are available in the enviorment


*** =hint
- Write statement from sklearn.tree import DecisionTreeClassifier to import Decision tree
- Use len(train_modified) to return the length


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
