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

Library "Scikit Learn" only works with numeric array hence we need to label all the character variable into numeric array. For Example: Variable "Gender" has two labels "Male" and "Female", here our objective is to label "Male" and "Female" to number as 1 for "Male" and 0 for "Female".

"Scikit Learn" library has module "LabelEncoder" which helps to label charater labels into numbers so first import module "LabelEncoder".

```{python}

from sklearn.preprocessing import LabelEncoder

number = LabelEncoder()

train['Gender'] = number.fit_transform(train['Gender'])

```

*** =instructions
- Import LabelEncoder 
- Label categories of variable "Married" to number 


*** =hint
Use expression train['Married'] = number.fit_transform(train['Married'])


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
from sklearn.preprocessing import ______

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

#import module for label encoding
test_import("LabelEncoder", same_as = False)

# Perform label encoding for Married
test_object(“train['Married']”)

success_msg("Great work!")
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:ee5ed17633
## Selecting the right algorithm

Basic principle behind selecting the right algorithm is look at the dependent variable (or target variable). In this challenge "Loan Prediction", we need to classify customer in Loan status "Y" or "N" category based on available information about customer. Here Dependent variable is categorical and our task is to classify the customer in two groups; eligible for loan amount and not eligible for loan amounts.

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

--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:ee5ed17633
## Have you performed data preprocessing?

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

msg_bad1 = "Try again"
msg_success = "Yes! We should always treat missing value"

# Use test_mc() to grade multiple choice exercises. 
# Pass the correct option (Action, option 2 in the instructions) to correct.
# Pass the feedback messages, both positive and negative, to feedback_msgs in the appropriate order.
test_mc(4, [msg_bad1, msg_bad1, msg_bad1, msg_success ]) 
```








--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## First Step of Model Building

Till now, we have looked at the data exploartion, cleaning, feature engineering and pre processing steps of model building. Now, we will look at the methods of building a model. 

In this challenge "Loan Prediction", we need to classify customer in Loan status "Y" or "N" category based on available information about customer. 

Before jumping into model building steps, we need to follow below steps:

* Impute missing values of the data set

* Import required library (In python, we mostly use sklearn), this is a classification challenge so we will import module of classification algorithms

```{python}
  #Logistic Rgression
  from sklearn.linear_model import LogisticRegression  
  
  #Decision Tree
  from sklearn.tree import DecisionTreeClassifier 
  
  #Random Forest
  from sklearn.ensemble import RandomForestClassifier 
```

* Convert categorical variables to numeric array because sklearn requires all inputs in numeric array


*** =instructions
- Import required library for decision tree and random forest
- Use len() function with dataframes train_modified and test_modified, these two dataframes are available in the enviorment after missing values imputation and label encoding for all categorical variables


*** =hint
- Use from sklearn.tree import DecisionTreeClassifier
- Use from sklearn.ensemble import RandomForestClassifier
- Use len(train_modified) to return the length


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
# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Import module for Decision Tree
from sklearn.tree import _________

# Import module for Random Forest
from _________ import RandomForestClassifier

# Number of observations in the dataframes train_modified and test_modified
train_modified_count = 
test_modified_count = 

```

*** =solution

```{python}
# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Import module for Decision Tree
from sklearn.tree import DecisionTreeClassifier

# Import module for Random Forest
from sklearn.ensemble import RandomForestClassifier

# Number of observations in train_modified and test_modified
train_modified_count = len(train_modified)
test_modified_count = len(test_modified)

```

*** =sct

```{python}
# The sct section defines the Submission Correctness Tests (SCTs) used to
# evaluate the student's response. All functions used here are defined in the 
# pythonwhat Python package. Documentation can also be found at github.com/datacamp/pythonwhat/wiki

# Test for import library


# Test number of observations in train_modiefied and test_modiefied
test_object("train_modified_count")
test_object("test_modified_count")


success_msg("Great work!")
```




--- type:NormalExercise lang:python xp:100 skills:1 key:f4c3fbee79

## Performing prediction using Logistic Regression

Logistic Regression is a classification algorithm. It is used to predict a binary outcome (1 / 0, Yes / No, True / False) given a set of independent variables, read more about <a href="http://www.analyticsvidhya.com/blog/2015/11/beginners-guide-on-logistic-regression-in-r/"> Logistic Regression </a>.

Let’s make our first Logistic Regression model. One way would be to take all the variables into the model but this might result in overfitting (don’t worry if you’re unaware of this terminology yet). In simple words, taking all variables might result in the model understanding complex relations specific to the data and will not generalize well.

We can easily make some intuitive hypothesis to set the ball rolling. The chances of getting a loan will be higher for:

* Applicants having a credit history
* Applicants with higher applicant and co-applicant incomes
* Applicants with higher education level
* Properties in urban areas with high growth perspectives

Build a logistic regression model for two predictors variable "Credit_History" and "Education"

* Importing libraries and feature selection

```{python}
  from sklearn.linear_model import LogisticRegression  
  
  predictors = ['Credit_History','Education']
```
  
* Converting predictors and outcome to numpy array

```{python}  
  x_train = train_modified[predictors].values
  y_train = train_modified['Loan_Status'].values
  x_test = test_modified[predictors].values
```  

* Model Building

```{python}    
  model = LogisticRegression()
  
  model.fit(x_train, y_train)
```  

* Predicting class and converting to original labels "Y" / "N"

```{python}      
  predicted= model.predict(x_test)
  
  #Remember number = LabelEncoder()
  predicted = number.inverse_transform(predicted)
```    

* Storing prediction to test data set and sumit solution to <a href="datahack.analyticsvidhya.com">datahack</a>

  ```{python}      
  test_modified['Loan_Status']=predicted
  
  test_modified.to_csv("Submission1.csv", columns=['Loan_ID','Loan_Status'])

```


*** =instructions
- Store input variable in list "predictors"
- Create a object of logistic regression
- Train model on training data set (x_train, y_train) and perform predition on test data (x_test)


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
# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Select three predictors Credit_History, Education and Gender
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values
x_test = test_modified[predictors].values

# Model Building
model = _________
model.fit(x_train, y_train)

# Predict class and converting to original labels
predicted= model.predict(____)
predicted = number.inverse_transform(predicted)

# Storing prediction to test data set and sumit solution to datahack
test_modified['Loan_Status']=predicted
test_modified.to_csv("Submission1.csv", columns=['Loan_ID','Loan_Status'])

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
x_test = test_modified[predictors].values

# Model Building
model = LogisticRegression()
model.fit(x_train, y_train)

# Predict class and converting to original labels
predicted= model.predict(x_test)
predicted = number.inverse_transform(predicted)

# Storing prediction to test data set and sumit solution to datahack
test_modified['Loan_Status']=predicted
test_modified.to_csv("Submission1.csv", columns=['Loan_ID','Loan_Status'])

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

# Test for prediction
test_object("predicted")

success_msg("Great work!")
```

--- type:NormalExercise lang:python xp:100 skills:1 key:0f04d6b3e1

## Performing prediction using Decision Tree

Decision tree is mostly used in classification problems. It works for both categorical and continuous input and output variables. In this technique, we split the population or sample into two or more homogeneous sets (or sub-populations) based on most significant splitter / differentiator in input variables, read more about <a href="http://www.analyticsvidhya.com/blog/2015/01/decision-tree-simplified/"> Decision Tree </a>.

Build a Decision Tree model for two predictors variable "Credit_History" and "Education"

* Importing libraries and feature selection

```{python}
  from sklearn.tree import DecisionTreeClassifier
  
  predictors = ['Credit_History','Education']
```
  
* Converting predictors and outcome to numpy array

```{python}  
  x_train = train_modified[predictors].values
  y_train = train_modified['Loan_Status'].values
  x_test = test_modified[predictors].values
```  

* Model Building

```{python}    
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
```  

* Predicting class and converting to original labels "Y" / "N"

```{python}      
  predicted = model.predict(x_test)
  
  #Remember number = LabelEncoder()
  predicted = number.inverse_transform(predicted)
```    

* Storing prediction to test data set and sumit solution to <a href="datahack.analyticsvidhya.com">datahack</a>

  ```{python}      
  test_modified['Loan_Status']=predicted
  
  test_modified.to_csv("Submission2.csv", columns=['Loan_ID','Loan_Status'])

```


*** =instructions
- Store input variable in list "predictors"
- Create a object of Decisiontreeclassifier
- Train model on training data set (x_train, y_train) and perform predition on test data (x_test)
- Perform an inverse transformation of predicted class


*** =hint
- Use predictors =['Credit_History','Loan_Amount_Term','Log_TotalIncome'] as predictor variable

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
# Import module for Decision Tree Classifiers
from sklearn.tree import DecisionTreeClassifier

# Select three predictors Credit_History, Education and Gender
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values
x_test = test_modified[predictors].values

# Model Building
model = _________
model.fit(______, ______)

# Predict class and converting to original labels
predicted= model.predict(x_test)
predicted = number._________(predicted)

# Storing prediction to test data set and sumit solution to datahack
test_modified['Loan_Status']=predicted
test_modified.to_csv("Submission2.csv", columns=['Loan_ID','Loan_Status'])

```

*** =solution

```{python}
# Import module for Decision Tree
from sklearn.tree import DecisionTreeClassifier

# Select three predictors Credit_History, Education and Gender
predictors =['Credit_History','Education','Gender']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values
x_test = test_modified[predictors].values

# Model Building
model = DecisionTreeClassifier()
model.fit(x_train, y_train)

# Predict class and converting to original labels
predicted= model.predict(x_test)
predicted = number.inverse_transform(predicted)

# Storing prediction to test data set and sumit solution to datahack
test_modified['Loan_Status']=predicted
test_modified.to_csv("Submission1.csv", columns=['Loan_ID','Loan_Status'])

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

# Test for prediction
test_object("predicted")

success_msg("Great work!")
```







--- type:NormalExercise lang:python xp:100 skills:1 key:ff4ced6565

## Performing prediction using Random Forest

Random Forest is a versatile machine learning method capable of performing both regression and classification tasks. It also undertakes dimensional reduction methods, treats missing values, outlier values and other essential steps of data exploration, and does a fairly good job. It is a type of ensemble learning method, where a group of weak models combine to form a powerful model, read more about <a href="http://www.analyticsvidhya.com/blog/2015/09/random-forest-algorithm-multiple-challenges/"> Random Forest </a>.

* Importing libraries and feature selection

```{python}
  from sklearn.ensemble import RandomForestClassifier
  
  predictors=['Credit_History','LoanAmount','Gender']
```
  
* Converting predictors and outcome to numpy array

```{python}  
  x_train = train_modified[predictors].values
  y_train = train_modified['Loan_Status'].values
  x_test = test_modified[predictors].values
```  

* Model Building

```{python}    
model = RandomForestClassifier()
model.fit(x_train, y_train)
```  

* Predicting class and converting to original labels "Y" / "N"

```{python}      
  predicted = model.predict(x_test)
  
  #Remember number = LabelEncoder()
  predicted = number.inverse_transform(predicted)
```    

* Storing prediction to test data set and submit solution to <a href="datahack.analyticsvidhya.com">datahack</a>

  ```{python}      
  test_modified['Loan_Status']=predicted
  
  test_modified.to_csv("Submission3.csv", columns=['Loan_ID','Loan_Status'])

```


*** =instructions
- Store input variable in list "predictors"
- Select the target variable
- Create a object of Random Forest Classifier
- Train model on training data set and perform prediction on test data
- Export only two columns ("Loan_ID", "Loan_Status") of test data set


*** =hint
- Use three predictors ['Credit_History','LoanAmount','Log_TotalIncome']

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
# Import module for Random Forest Classifiers
from sklearn.ensemble import RandomForestClassifier

# Select three predictors Credit_History, LoanAmount and Log_TotalIncome 
predictors =[____,_____,_____]

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified[________].values
x_test = test_modified[predictors].values

# Model Building
model = _________
model.fit(x_train, y_train)

# Predict class and converting to original labels
predicted= model.predict(____)
predicted = number.inverse_transform(predicted)

# Storing prediction to test data set and sumit solution to datahack
test_modified['Loan_Status']=predicted
test_modified.to_csv("Submission3.csv", ____________)

```

*** =solution

```{python}
# Import module for Random Forest classifier
from sklearn.ensemble import RandomForestClassifier

# Select three predictors Credit_History, LoanAmount and Log_TotalIncome 
predictors =['Credit_History','LoanAmount','Log_TotalIncome']

# Converting predictors and outcome to numpy array
x_train = train_modified[predictors].values
y_train = train_modified['Loan_Status'].values
x_test = test_modified[predictors].values

# Model Building
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict class and converting to original labels
predicted= model.predict(x_test)
predicted = number.inverse_transform(predicted)

# Storing prediction to test data set and sumit solution to datahack
test_modified['Loan_Status']=predicted
test_modified.to_csv("Submission3.csv", columns=['Loan_ID','Loan_Status'])

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

# Test for prediction
#test_object("predicted")

success_msg("Great work!")
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:4621632d2a
## Selecting important variables for model building

One of benefits of Random forest which excites me most is, the power of handle large data set with higher dimensionality. It can handle thousands of input variables and identify most significant variables so it is considered as one of the dimensionality reduction methods. Further, the model outputs Importance of variable, which can be a very handy feature. 

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
