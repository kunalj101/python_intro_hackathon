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
    * from sklearn.linear_model import LogisticRegression #Logistic Rgression 
    * from sklearn.tree import DecisionTreeClassifier #Decision Tree
    * from sklearn.ensemble import RandomForestClassifier #Random Forest
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

```

*** =sample_code

```{python}

# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Import module for Decision Tree
from sklearn.tree import _________

# Import module for Random Forest
from _________ import RandomForestClassifier

# Number of observations in train_modiefied and test_modiefied
train_modified_count = 
train_modified_count = 

```

*** =solution

```{python}
# Import module for Logistic regression
from sklearn.linear_model import LogisticRegression

# Import module for Decision Tree
from sklearn.tree import DecisionTreeClassifier

# Import module for Random Forest
from sklearn.ensemble import RandomForestClassifier

# Number of observations in train_modiefied and test_modiefied
train_modified_count = len(train_modified)
train_modified_count = len(test_modified)

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
