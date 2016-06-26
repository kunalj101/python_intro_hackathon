---
title       : Building a Predictive model in Python
description : We build our predictive models and make submissions to the AV DataHack platform in this section.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
## First Step of Model Building

In Python, Scikit-Learn (sklearn) is the most commonly used library for model building. I encourage you to get a refresher on sklearn through this <a href="http://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/">article</a>. It has gathered a lot of interest recently for model building. There are few pre-requisite before jumping into a model building exercise:

* Treat missing values
* Treat outlier/ exponential observation
* All inputs must be numeric array ( Requirement of scikit learn library) 


####We can build a model without treating missing values of data set


*** =instructions
- True
- False

*** =hint
Missing value tratment is compulsary step of model building

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "Try again"
msg_success = "Yes! We should always treat missing value"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(2, [msg_bad1, msg_success]) 
```



--- type:NormalExercise lang:python xp:100 skills:1 key:2c1cf7aa90
## Label categories of Gender to number

Library "Scikit Learn" only works with numeric array hence, we need to label all the character variable into a numeric array. For example Variable "Gender" has two labels "Male" and "Female", here our objective is to label "Male" and "Female" to number as 1 for "Male" and 0 for "Female".

"Scikit Learn" library has a module called "LabelEncoder" which helps to label character labels into numbers so first import module "LabelEncoder".

```{python}

from sklearn.preprocessing import LabelEncoder

number = LabelEncoder()

train['Gender'] = number.fit_transform(train['Gender'])

```

*** =instructions
Perform Label encoding for categories of variable "Married" 


*** =hint
Use number.fit_transform() to perform label encoding


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

#import module for label encoding
from sklearn.preprocessing import LabelEncoder

#train and test dataset is already loaded in the enviornment
# Perform label encoding for Married
number = LabelEncoder()
train['Married'] = number.________(train['Property_Area'])


```

*** =solution

```{python}

#import module for label encoding
from sklearn.preprocessing import LabelEncoder

#train and test dataset is already loaded in the enviornment
# Perform label encoding for Married
number = LabelEncoder()
train['Married'] = number.fit_transform(train['Property_Area'])
```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Perform label encoding for Married
test_data_frame("train", columns=["Married"], incorrect_msg='Have you used write methds to perform label encoding for variable Married?')

success_msg("Great work!")
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:ee5ed17633
## Selecting the right algorithm

The basic principle behind selecting the right algorithm is to look at the dependent variable (or target variable). In this challenge "Loan Prediction", we need to classify a customer's Loan status as "Y" or "N" based on the available information about the customer. Here the dependent variable is categorical and our task is to classify the customer in two groups; eligible for the loan amount and not eligible for the loan amounts.

This is a classification challenge so we will import module of classification algorithms of sklearn library, below are the few classification algorithms:
* Logistic Regression
* Decision Tree
* Random Forest


####Is this e-mail is spam or not? Is it a classification challenge or regression?


*** =instructions
- Classification
- Regression

*** =hint
- Regression: When we model for continuous variables
- Classification: When we model to classify in different categories

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "Try again"
msg_success = "Yes! We should always treat missing value"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(1, [msg_success, msg_bad1]) 
```

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:bd9b384210
## Have you performed data preprocessing step?

As I discussed, you should perform some data pre processing steps for both train and test dataset before jumping into model building exercise:
* Missing value imputation
* Outlier treatment
* Label encoding for character variables
* Algorithm selection


####Which of th following steps have you performed till now with both train and test data set?


*** =instructions
- Impute missing values of all variables
- Treat outlier and influential observations
- Label encoding for character variables
- All of the above

*** =hint
All steps are necessary anc could impact your model performance

*** =pre_exercise_code


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad1 = "You should first perform the pre processing steps"
msg_success = "Great! Go ahead with modeling exercise"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(4, [msg_bad1, msg_bad1, msg_bad1, msg_success ]) 
```

--- type:NormalExercise lang:python xp:100 skills:1 key:f4c3fbee79

## Logistic Regression Introduction

Logistic Regression is a classification algorithm. It is used to predict a binary outcome (1 / 0, Yes / No, True / False) given a set of independent variables. To represent binary / categorical outcome, we use dummy variables. You can also think of logistic regression as a special case of linear regression when the outcome variable is categorical, where we are using log of odds as the dependent variable. 

In simple words, it predicts the probability of occurrence of an event by fitting data to a logit function, read more about <a href="http://www.analyticsvidhya.com/blog/2015/11/beginners-guide-on-logistic-regression-in-r/"> Logistic Regression </a>. 


*** =instructions
- Import Linear model of sklearn
- Create object of sklearn



*** =hint
Import linear_model of sklearn


*** =pre_exercise_code

```{python}
import sklearn.linear_model 

```

*** =sample_code

```{python}

# Import linear model of sklearn
import ______.linear_model

# Create object of Logistic Regression
model=sklearn.______.LogisticRegression()

```

*** =solution

```{python}
# Import linear model of sklearn
import sklearn.linear_model

# Create object of Logistic Regression
model=sklearn.linear_model.LogisticRegression()

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for library import
test_import("sklearn.linear_model", same_as = False)

# Test for logistic regression
test_object("model", incorrect_msg='Have you created Logistic Regression object from linear model of sklearn?')

success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:6eb60851bc

## Build your first logistic regression model

Let’s make our first Logistic Regression model. One way would be to take all the variables into the model but this might result in overfitting (don’t worry if you’re unaware of this terminology yet). In simple words, taking all variables might result in the model understanding complex relations specific to the data and will not generalize well.

We can easily make some intuitive hypothesis to set the ball rolling. The chances of getting a loan will be higher for:

* Applicants having a credit history
* Applicants with higher applicant and co-applicant incomes
* Applicants with higher education level
* Properties in urban areas with high growth perspectives

Ok, time for you to build your first logistics regression model! The pre processed train_modified and test_modifed data are available in your workspace.

*** =instructions
- Store input variable in list "predictors"
- Create an object of logistic regression
- Train model on training data set (x_train, y_train)


*** =hint
- Use predictors =['Credit_History','Education','Gender'] as predictor variable

*** =pre_exercise_code

```{python}
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

#Combining both train and test dataset

train['Type']='Train' #Create a flag for Train and Test Data set
test['Type']='Test'
fullData = pd.concat([train,test],axis=0)

#Identify categorical and continuous variables

ID_col = ['Loan_ID']
target_col = ["Loan_Status"]
cat_cols = ['Credit_History','Dependents','Gender','Married','Education','Property_Area','Self_Employed']

other_col=['Type'] #Test and Train Data set identifier
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col)-set(other_col))

#Imputing Missing values with mean for continuous variable
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(),inplace=True)


#Imputing Missing values with mode for categorical variables
cat_imput=pd.Series(fullData[cat_cols].mode().values[0])
cat_imput.index=cat_cols
fullData[cat_cols] = fullData[cat_cols].fillna(cat_imput,inplace=True)

#Create a new column as Total Income
fullData['TotalIncome']=fullData['ApplicantIncome']+fullData['CoapplicantIncome']

#Take a log of TotalIncome + 1, adding 1 to deal with zeros of TotalIncome it it exists
fullData['Log_TotalIncome']=np.log(fullData['TotalIncome'])

#create label encoders for categorical features
for var in cat_cols:
    number = LabelEncoder()
    fullData[var] = number.fit_transform(fullData[var].astype('str'))

train_modified=fullData[fullData['Type']=='Train']
test_modified=fullData[fullData['Type']=='Test']
train_modified["Loan_Status"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))
```

*** =sample_code

```{python}

#train_modified and test_modified already loaded in the workspace
#Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Select three predictors Credit_History, Education and Gender
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = _________
model.fit(x_train, y_train)

```

*** =solution

```{python}
# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History','Education','Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = LogisticRegression()
model.fit(x_train, y_train)

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for predictor selection
test_object("predictors")

# Test for model
#test_object("model")

success_msg("Great work!")
```



--- type:NormalExercise lang:python xp:100 skills:1 key:207a5629cc

## Prediction and submit to DataHack

To send a submission to DataHack you need to predict the loan approval rate for the observations in the test set using ".predict()" method with logistic regression object (model). To extract the test features we will need to create a numpy array of input features of test data set in the same way as we did when training the model for training data.

Next, you need to make sure your output is in line with the submission requirements of DataHack: a csv file with exactly 367 entries and two columns: Loan_ID and Loan_Status. Then create a csv file using to_csv() method from Pandas.


*** =instructions
- Store input variable in list "predictors"
- Use .predict() method for prediction


*** =hint
- Use predictors =['Credit_History','Education','Gender'] as predictor variable
- Use model.predict(x_test) for prediction of test dataset

*** =pre_exercise_code

```{python}
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

#Combining both train and test dataset

train['Type']='Train' #Create a flag for Train and Test Data set
test['Type']='Test'
fullData = pd.concat([train,test],axis=0)

#Identify categorical and continuous variables

ID_col = ['Loan_ID']
target_col = ["Loan_Status"]
cat_cols = ['Credit_History','Dependents','Gender','Married','Education','Property_Area','Self_Employed']

other_col=['Type'] #Test and Train Data set identifier
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col)-set(other_col))

#Imputing Missing values with mean for continuous variable
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(),inplace=True)


#Imputing Missing values with mode for categorical variables
cat_imput=pd.Series(fullData[cat_cols].mode().values[0])
cat_imput.index=cat_cols
fullData[cat_cols] = fullData[cat_cols].fillna(cat_imput,inplace=True)

#Create a new column as Total Income

fullData['TotalIncome']=fullData['ApplicantIncome']+fullData['CoapplicantIncome']

#Take a log of TotalIncome + 1, adding 1 to deal with zeros of TotalIncome it it exists
fullData['Log_TotalIncome']=np.log(fullData['TotalIncome'])

#create label encoders for categorical features
for var in cat_cols:
    number = LabelEncoder()
    fullData[var] = number.fit_transform(fullData[var].astype('str'))

train_modified=fullData[fullData['Type']=='Train']
test_modified=fullData[fullData['Type']=='Test']
train_modified["Loan_Status"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))

# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History','Education','Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = LogisticRegression()
model.fit(x_train, y_train)
```

*** =sample_code

```{python}

#test_modified already loaded in the workspace

# Select three predictors Credit_History, Education and Gender
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model._____(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified.to_csv("Submission1.csv",columns=['Loan_ID','Loan_Status'])

```

*** =solution

```{python}
#test_modified already loaded in the workspace

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History','Education','Gender']

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model.predict(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified.to_csv("Submission1.csv",columns=['Loan_ID','Loan_Status'])

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for predictor selection
test_object("predictors")

# Test for model
test_object("predicted")

success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:0f04d6b3e1

## Decision Tree Introduction

Decision trees are mostly used in classification problems. It works for both categorical and continuous input and output variables. In this technique, we split the population or sample into two or more homogeneous sets (or sub-populations) based on most significant splitter / differentiator in input variables, read more about <a href="http://www.analyticsvidhya.com/blog/2015/01/decision-tree-simplified/"> Decision Tree </a>.


*** =instructions
Create a object of DecisionTreeClassifier


*** =hint
You can use from sklearn.tree import DecisionTreeClassifier command

*** =pre_exercise_code

```{python}
from sklearn.tree import DecisionTreeClassifier

```

*** =sample_code

```{python}

# Import module for DecisionTreeClassifier
from sklearn.tree import __________

```

*** =solution

```{python}
# Import module for Logistic regression
from sklearn.tree import DecisionTreeClassifier

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for predictor selection
test_import("DecisionTreeClassifier", same_as = False)

success_msg("Great work!")
```



--- type:NormalExercise lang:python xp:100 skills:1 key:dcf5c3e2c2

## Train model and do prediction using Decision Tree

Let’s make first Decision Tree model. Similar to Logistic regression, here we also first select the input features, train model and finally perform prediction on test data set.

Ok, time for you to build your first Decision Tree model! The pre processed train_modified and test_modifed data are available in your workspace.


*** =instructions
- Store input variable in list "predictors"
- Create a object of DecisionTreeClassifier
- Train model on training data set (x_train, y_train)
- Use .predict() method for prediction
- Use to_csv() to export csv file


*** =hint
- Use predictors =['Credit_History','Education','Gender'] as predictor variable
- Use from sklearn.tree import DecisionTreeClassifier


*** =pre_exercise_code

```{python}
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

#Combining both train and test dataset

train['Type']='Train' #Create a flag for Train and Test Data set
test['Type']='Test'
fullData = pd.concat([train,test],axis=0)

#Identify categorical and continuous variables

ID_col = ['Loan_ID']
target_col = ["Loan_Status"]
cat_cols = ['Credit_History','Dependents','Gender','Married','Education','Property_Area','Self_Employed']

other_col=['Type'] #Test and Train Data set identifier
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col)-set(other_col))

#Imputing Missing values with mean for continuous variable
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(),inplace=True)


#Imputing Missing values with mode for categorical variables
cat_imput=pd.Series(fullData[cat_cols].mode().values[0])
cat_imput.index=cat_cols
fullData[cat_cols] = fullData[cat_cols].fillna(cat_imput,inplace=True)

#Create a new column as Total Income
fullData['TotalIncome']=fullData['ApplicantIncome']+fullData['CoapplicantIncome']

#Take a log of TotalIncome + 1, adding 1 to deal with zeros of TotalIncome it it exists
fullData['Log_TotalIncome']=np.log(fullData['TotalIncome'])

#create label encoders for categorical features
for var in cat_cols:
    number = LabelEncoder()
    fullData[var] = number.fit_transform(fullData[var].astype('str'))

train_modified=fullData[fullData['Type']=='Train']
test_modified=fullData[fullData['Type']=='Test']
train_modified["Loan_Status"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))
```

*** =sample_code

```{python}

#train_modified and test_modified already loaded in the workspace
#Import module for Decision tree
from sklearn.tree import __________

# Select three predictors Credit_History, Education and Gender
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = _________
model.fit(x_train, y_train)

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model._____(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified._____("Submission1.csv",columns=['Loan_ID','Loan_Status'])


```

*** =solution

```{python}
#train_modified and test_modified already loaded in the workspace
#Import module for Decision tree
from sklearn.tree import DecisionTreeClassifier

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History','Education','Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model.predict(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified.to_csv("Submission1.csv",columns=['Loan_ID','Loan_Status'])


```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for predictor selection
test_object("predictors")

# Test for model
#test_object("model")

# Test for predicted
#test_object("predicted")


success_msg("Great work!")
```





--- type:NormalExercise lang:python xp:100 skills:1 key:ff4ced6565

## Random Forest Introduction

Random Forest is a versatile machine learning method capable of performing both regression and classification tasks. It also undertakes dimensional reduction methods, treats missing values, outlier values and other essential steps of data exploration, and does a fairly good job. It is a type of ensemble learning method, where a group of weak models combine to form a powerful model, read more about <a href="http://www.analyticsvidhya.com/blog/2015/09/random-forest-algorithm-multiple-challenges/"> Random Forest </a>.


*** =instructions
Create a object of DecisionTreeClassifier


*** =hint
You can use from sklearn.ensemble import RandomForestClassifier command

*** =pre_exercise_code

```{python}
from sklearn.ensemble import RandomForestClassifier
```

*** =sample_code

```{python}

# Import module for Random Forest Classifiers
from sklearn.ensemble import ________


```

*** =solution

```{python}
# Import module for Random Forest classifier
from sklearn.ensemble import RandomForestClassifier

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for predictor selection
test_import("RandomForestClassifier", same_as = False)


success_msg("Great work!")
```


--- type:NormalExercise lang:python xp:100 skills:1 key:f0d1f62bb1

## Train model and do prediction using Random Forest

Let’s make first Random Forest model. Similar to Logistic regression and Decision Tree, here we also first select the input features, train model and finally perform prediction on test data set.

Ok, time for you to build your first Random Forest model! The pre processed train_modified and test_modifed data are available in your workspace.


*** =instructions
- Store input variable in list "predictors"
- Create a object of RandomForestClassifier
- Train model on training data set (x_train, y_train)
- Use .predict() method for prediction
- Use to_csv() to export csv file


*** =hint
- Use predictors =['Credit_History','Education','Gender'] as predictor variable
- Use from sklearn.tree import RandomForestClassifier


*** =pre_exercise_code

```{python}
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

#Combining both train and test dataset

train['Type']='Train' #Create a flag for Train and Test Data set
test['Type']='Test'
fullData = pd.concat([train,test],axis=0)

#Identify categorical and continuous variables

ID_col = ['Loan_ID']
target_col = ["Loan_Status"]
cat_cols = ['Credit_History','Dependents','Gender','Married','Education','Property_Area','Self_Employed']

other_col=['Type'] #Test and Train Data set identifier
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col)-set(other_col))

#Imputing Missing values with mean for continuous variable
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(),inplace=True)


#Imputing Missing values with mode for categorical variables
cat_imput=pd.Series(fullData[cat_cols].mode().values[0])
cat_imput.index=cat_cols
fullData[cat_cols] = fullData[cat_cols].fillna(cat_imput,inplace=True)

#Create a new column as Total Income
fullData['TotalIncome']=fullData['ApplicantIncome']+fullData['CoapplicantIncome']

#Take a log of TotalIncome + 1, adding 1 to deal with zeros of TotalIncome it it exists
fullData['Log_TotalIncome']=np.log(fullData['TotalIncome'])

#create label encoders for categorical features
for var in cat_cols:
    number = LabelEncoder()
    fullData[var] = number.fit_transform(fullData[var].astype('str'))

train_modified=fullData[fullData['Type']=='Train']
test_modified=fullData[fullData['Type']=='Test']
train_modified["Loan_Status"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))
```

*** =sample_code

```{python}

#train_modified and test_modified already loaded in the workspace
#Import module for Random Forest
from sklearn.ensemble import __________

# Select three predictors Credit_History, Education and Gender
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = _________
model.fit(x_train, y_train)

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model._____(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified._____("Submission1.csv",columns=['Loan_ID','Loan_Status'])


```

*** =solution

```{python}
#train_modified and test_modified already loaded in the workspace
#Import module for Random Forest 
from sklearn.ensemble import RandomForestClassifier

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History','Education','Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values

# Model Building
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Converting predictors and outcome to numpy array
x_test = test_modified[predictors].values

#Predict Output
predicted= model.predict(x_test)

#Reverse encoding for predicted outcome
predicted = number.inverse_transform(predicted)

#Store it to test dataset
test_modified['Loan_Status']=predicted

#Output file to make submission
test_modified.to_csv("Submission1.csv",columns=['Loan_ID','Loan_Status'])


```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for predictor selection
test_object("predictors")

# Test for model
#test_object("model")

# Test for predicted
#test_object("predicted")


success_msg("Great work!")
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:4621632d2a
## Selecting important variables for model building

One of the benefits of Random forest is the power of handle large data set with higher dimensionality. It can handle thousands of input variables and identify most significant variables so it is considered as one of the dimensionality reduction methods. Further, the model outputs the importance of the variables, which can be a very handy feature. 

```{python}

featimp = pd.Series(model.feature_importances_, index=predictors).sort_values(ascending=False)

print (featimp)

```
I have selected all the features available in the train data set and model it using random forest:

```{python}
predictors=['ApplicantIncome', 'CoapplicantIncome', 'Credit_History','Dependents', 'Education', 'Gender', 'LoanAmount',
            'Loan_Amount_Term', 'Married', 'Property_Area', 'Self_Employed', 'TotalIncome','Log_TotalIncome']


```

Run feature importance command and identify Which variable has the highest impact on the model??


*** =instructions
- LoanAmount
- Dependents
- Gender
- Education

*** =hint
Run feature importance command

*** =pre_exercise_code
```{python}
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv")
test = pd.read_csv("https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv")

#Combining both train and test dataset

train['Type']='Train' #Create a flag for Train and Test Data set
test['Type']='Test'
fullData = pd.concat([train,test],axis=0)

#Identify categorical and continuous variables

ID_col = ['Loan_ID']
target_col = ["Loan_Status"]
cat_cols = ['Credit_History','Dependents','Gender','Married','Education','Property_Area','Self_Employed']

other_col=['Type'] #Test and Train Data set identifier
num_cols= list(set(list(fullData.columns))-set(cat_cols)-set(ID_col)-set(target_col)-set(other_col))

#Imputing Missing values with mean for continuous variable
fullData[num_cols] = fullData[num_cols].fillna(fullData[num_cols].mean(),inplace=True)


#Imputing Missing values with mode for categorical variables
cat_imput=pd.Series(fullData[cat_cols].mode().values[0])
cat_imput.index=cat_cols
fullData[cat_cols] = fullData[cat_cols].fillna(cat_imput,inplace=True)

#Create a new column as Total Income

fullData['TotalIncome']=fullData['ApplicantIncome']+fullData['CoapplicantIncome']

#Take a log of TotalIncome + 1, adding 1 to deal with zeros of TotalIncome it it exists
fullData['Log_TotalIncome']=np.log(fullData['TotalIncome'])

#create label encoders for categorical features
for var in cat_cols:
    number = LabelEncoder()
    fullData[var] = number.fit_transform(fullData[var].astype('str'))

train_modified=fullData[fullData['Type']=='Train']
test_modified=fullData[fullData['Type']=='Test']
train_modified["Loan_Status"] = number.fit_transform(train_modified["Loan_Status"].astype('str'))

# Import module for Random Forest classifier
from sklearn.ensemble import RandomForestClassifier

# Select three predictors Credit_History, LoanAmount and Log_TotalIncome 
predictors=['ApplicantIncome', 'CoapplicantIncome', 'Credit_History','Dependents', 'Education', 'Gender', 'LoanAmount',
            'Loan_Amount_Term', 'Married', 'Property_Area', 'Self_Employed', 'TotalIncome','Log_TotalIncome']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values
x_test = test_modified[predictors].values

# Model Building
model = RandomForestClassifier()
model.fit(x_train, y_train)

```


*** =sct
```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package

msg_bad = "That is not correct!"
msg_success = "You got it right!"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(1, [msg_success, msg_bad, msg_bad, msg_bad]) 
```
