---
title       : Building a Predictive model in Python
description : We build our predictive models and make submissions to the AV DataHack platform in this section.
attachments :
  slides_link : https://s3.amazonaws.com/assets.datacamp.com/course/teach/slides_example.pdf

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

* Storing prediction to test data set and sumit solution to <a href="datahack.analyticsvidhya.com">datahack</a>

  ```{python}      
  test_modified['Loan_Status']=predicted
  
  test_modified.to_csv("Submission1.csv", columns=['Loan_ID','Loan_Status'])

```


*** =instructions
- Store input variable in list "predictors"
- Create a object of logistic regression
- Train model on training data set and perform predition on test data


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

* Predicting class and converting to original labels

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
- Create a object of Decision Tree Classifier
- Train model on training data set and perform predition on test data


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
model.fit(x_train, y_train)

# Predict class and converting to original labels
predicted= model.predict(____)
predicted = number.inverse_transform(predicted)

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

* Predicting class and converting to original labels

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
- Create a object of Random Forest Classifier
- Train model on training data set and perform prediction on test data


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

# Import module for Random Forest Classifiers
from sklearn.ensemble import RandomForestClassifier

# Select three predictors Credit_History, LoanAmount and Log_TotalIncome 
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
test_modified.to_csv("Submission3.csv", columns=['Loan_ID','Loan_Status'])

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
test_object("predicted")

success_msg("Great work!")
```


--- type:MultipleChoiceExercise lang:python xp:50 skills:1 key:9a8fd577a9
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

model = RandomForestClassifier()

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
