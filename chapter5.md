---
title       : Building a Predictive model in Python
description : We build our predictive models and make submissions to the AV DataHack platform in this section.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

--- type:NormalExercise lang:python xp:100 skills:1 key:af2f6f90f3
## First Step of Model Building

Till now, we have looked at the data exploartion, cleaning, feature engineering and pre processing steps of model building. Now, we will look at the methods of building a model. 

In this challengs "Loan Prediction", we need to classify customer in Loan status "Y" or "N" category based on available information about customer. Before jumping into model building steps, we need to follow below steps:

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
- Import sklearn library and required model for model building
- Dataframes train_modified and test_modified are available in the enviorment


*** =hint
- Write statement from sklearn.tree import DecisionTreeClassifier to import Decision tree
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

# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Import module for Decision Tree
from sklearn.tree import _________

# Import module for Random Forest
from _________ import RandomForestClassifier

# Number of observations in the dataframes train_modiefied and test_modiefied
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

* Predicting class and converting to original labels

```{python}      
  predicted= model.predict(x_test)
  
  #Remember number = LabelEncoder()
  predicted = number.inverse_transform(predicted)
```    

* Storing prediction to test data set and sumit solution to datahack

  ```{python}      
  test_modified['Loan_Status']=predicted
  
  test_modified.to_csv("Submission1.csv", columns=['Loan_ID','Loan_Status'])

```


*** =instructions
- Import sklearn library and required model for model building
- Dataframes train_modified and test_modified are available in the enviorment


*** =hint
- Write statement from sklearn.tree import DecisionTreeClassifier to import Decision tree
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
model.fit(x_train, y_test)

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
test_object("features")

# Test for model
test_object("model")

# Test for prediction
test_object("predicted")

success_msg("Great work!")
```

