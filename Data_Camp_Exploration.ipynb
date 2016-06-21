{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Who is eligible for loan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Import library pandas\n",
    "import pandas as pd\n",
    "\n",
    "# Import training data as train\n",
    "train = pd.read_csv(\"https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/train.csv\")\n",
    "\n",
    "# Import testing data as test\n",
    "test = pd.read_csv(\"https://s3-ap-southeast-1.amazonaws.com/av-datahack-datacamp/test.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Loan_ID Gender Married Dependents     Education Self_Employed  \\\n",
      "0  LP001002   Male      No          0      Graduate            No   \n",
      "1  LP001003   Male     Yes          1      Graduate            No   \n",
      "2  LP001005   Male     Yes          0      Graduate           Yes   \n",
      "3  LP001006   Male     Yes          0  Not Graduate            No   \n",
      "4  LP001008   Male      No          0      Graduate            No   \n",
      "\n",
      "   ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
      "0             5849                0.0         NaN             360.0   \n",
      "1             4583             1508.0       128.0             360.0   \n",
      "2             3000                0.0        66.0             360.0   \n",
      "3             2583             2358.0       120.0             360.0   \n",
      "4             6000                0.0       141.0             360.0   \n",
      "\n",
      "   Credit_History Property_Area Loan_Status  \n",
      "0             1.0         Urban           Y  \n",
      "1             1.0         Rural           N  \n",
      "2             1.0         Urban           Y  \n",
      "3             1.0         Urban           Y  \n",
      "4             1.0         Urban           Y  \n"
     ]
    }
   ],
   "source": [
    "# Print top 5 observation of training dataset\n",
    "print (train.head(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Store total number of observation in training dataset\n",
    "train_length =len(train)\n",
    "\n",
    "# Store total number of columns in testing data set\n",
    "test_col = len(test.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Understanding Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
      "count       614.000000         614.000000  592.000000         600.00000   \n",
      "mean       5403.459283        1621.245798  146.412162         342.00000   \n",
      "std        6109.041673        2926.248369   85.587325          65.12041   \n",
      "min         150.000000           0.000000    9.000000          12.00000   \n",
      "25%        2877.500000           0.000000  100.000000         360.00000   \n",
      "50%        3812.500000        1188.500000  128.000000         360.00000   \n",
      "75%        5795.000000        2297.250000  168.000000         360.00000   \n",
      "max       81000.000000       41667.000000  700.000000         480.00000   \n",
      "\n",
      "       Credit_History  \n",
      "count      564.000000  \n",
      "mean         0.842199  \n",
      "std          0.364878  \n",
      "min          0.000000  \n",
      "25%          1.000000  \n",
      "50%          1.000000  \n",
      "75%          1.000000  \n",
      "max          1.000000  \n"
     ]
    }
   ],
   "source": [
    "# Look at the summary of numerical variables for train data set\n",
    "df= train.describe()\n",
    "print (df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Semiurban    233\n",
      "Urban        202\n",
      "Rural        179\n",
      "Name: Property_Area, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Print the unique values and their frequency of variable Property_Area\n",
    "df1=train['Property_Area'].value_counts()\n",
    "print (df1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Understanding distribution of numerical variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x88843c8>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nSUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7c61ef0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%matplotlib inline\n",
    "# Plot histogram for variable LoanAmount\n",
    "train['LoanAmount'].hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x8a67eb8>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nX9JJkn4i6aeSLmjWdWxby/we2tqQn1O1l6Ykf0k7AZ8G/gJ4GfB2SS9txrVsW+vXry86BLNtTPac\n6pJLLvFzqhbbpUnnPQpYGxEPA0i6EjgV+EmTrld61Wp1pNyzYsUKFi1aBEClUqFSqRQWl1k9Nm7c\nWHQIpdOs5L8v8Ehu/ZdkfxCsSfJJvlqtjiR/M7Px+IFvF3IryjrN0NBQ0SGUTrNa/uuAA3Lr+6Vt\no/hhTvP4Z2udZmBgoOgQSqUp/fwl7Qw8ALwe+BVwJ/D2iLh/2i9mZmYNa0rLPyL+KOk8YCVZaeky\nJ34zs/ZR2AhfMzMrjh/4thFJf5R0j6QfpP8fMPVR232tMyV9qlnnN5O0VdLlufWdJf1a0vVTHHec\npK81P8Jya9YDX9s+T0bEES28nt/2WTM9CfyppF0j4mngDYzuAj4Z35tN5pZ/e9mmi46knSRdLOkO\nSYOS3pO2HyepKuk6SQ9KulDSO9J+90o6KO33Zkm3S7pb0kpJLxrnGi+UdHU69g5Jr2n+t2olcSPw\nprT8duDLtRckHSnpu+nevE3S3LEHS9pD0mW5e/jkFsXd9Zz828vuubLPNWnbOcDGiDiabKDceyUd\nmF57BfBe4FDgXcDctN9lwPvSPt+OiGMi4pXAVcB48yx9EvindOxbgM8245uz0gngSrLpXXYlu1/v\nyL1+P3BsujcXAheOc45/AL4ZEccArwM+IWn35oZdDi77tJenxin7nAi8XNJb0/rzgbnAZuCuiHgU\nQNLPyHpXAdwHVNLy/pKWA/sAzwF+Ps51TwAO0bODA/aUtEdEPDUN35OVWET8SFIvWav/Bka/u+0B\nLk8t/mD8fHQicLKkD6b1GWRjiB5oVsxl4eTf/gS8LyJuHrVROg54Ordpa259K8/+234K+ERE3JCO\nWTjBNY6OiM3TGrlZ5nrg42QNkhfmtn8UuDUiTk/vZleNc6yAMyJibdOjLBmXfdrLeMNyVwDnStoF\nQNJcSXs0cM7nA/+Zls+cYJ+VwPkjQUiHNXB+s4nU7ufPAYsj4sdjXp/JsyP/z5rgHCuA94+cUOqb\n1ghLzMm/vYzXw+GzwBrgHkn3Af8K7FznsQCLgasl3QX8eoJ9zgdelR4U/wj428bCNhtXAETEuoj4\n9DivXwxcJOluJs5FHwWeI+mH6f7/x+aEWj4e5GVmVkJu+ZuZlZCTv5lZCTn5m5mVkJO/mVkJOfmb\nmZWQk7+ZWQk5+VspSNpb0hVpEry7JH1H0qnTcF5PP2wdycnfyuI6oBoRB0fEkcDbyD5bejrUPVgm\nfcSpWeEnSNnBAAABfUlEQVSc/K3rSXod8HRE/HttW0Q8EhGXTjFl9ipJX5F0v6Qv5M53Utr2feD0\n3PZxpx9OH5zzVUnfBG5p2TduNglP7GZl8DLgngleG5kyW9IM4DuSarOj9pFNl70+bX8NcDfwb0Al\nIh6SdFXuXLXph8+RNBO4U1It2R8OvDwinpjeb81s+zj5W+lI+jRwLPAM8DATT5l9Z0T8Kh0zCPSS\nfTrVQxHxUNr/i8B70vJE0w8D3OzEb+3Eyd/K4MfAGbWViDhP0l5krfiHqW/K7D/y7O/LeLOv1rZv\nM/2wpGPI/miYtQ3X/K3rRcStwK6S8rOV7kn2oLbRKbN/AhxY+5hMsg8pqfH0w9Yx3PK3sjgNWCrp\nQ2RTWz8JfCgirk6J/J70SWaPpn3Hqk1P/HT6I3KjpCeBb5P9IYFs+uGlkn5I1rB6CDilmd+U2fby\nlM5mZiXkso+ZWQk5+ZuZlZCTv5lZCTn5m5mVkJO/mVkJOfmbmZWQk7+ZWQk5+ZuZldD/B5YBYFEV\nIZAuAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x894c198>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plot a box plot for variable LoanAmount by variable Gender of training data set\n",
    "train.boxplot(column='LoanAmount', by = 'Gender')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Understanding distribution of categorical variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "422 number of loans were approved.\n"
     ]
    }
   ],
   "source": [
    "# Loan approval rates in absolute numbers\n",
    "loan_approval = train['Loan_Status'].value_counts()['Y']\n",
    "print \"%d number of loans were approved.\" %loan_approval"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Loan_Status</th>\n",
       "      <th>N</th>\n",
       "      <th>Y</th>\n",
       "      <th>All</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Credit_History</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0.0</th>\n",
       "      <td>82</td>\n",
       "      <td>7</td>\n",
       "      <td>89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1.0</th>\n",
       "      <td>97</td>\n",
       "      <td>378</td>\n",
       "      <td>475</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>All</th>\n",
       "      <td>192</td>\n",
       "      <td>422</td>\n",
       "      <td>614</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Loan_Status       N    Y  All\n",
       "Credit_History               \n",
       "0.0              82    7   89\n",
       "1.0              97  378  475\n",
       "All             192  422  614"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Two-way comparison: Credit History and Loan Status\n",
    "pd.crosstab(train [\"Credit_History\"], train [\"Loan_Status\"], margins=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "79.578947 percent of the applicants whose loans were approved have Credit_History equals to 1.\n"
     ]
    }
   ],
   "source": [
    "#Function to output percentage row wise in a cross table\n",
    "def percentageConvert(ser):\n",
    " return ser/float(ser[-1])\n",
    "\n",
    "# Two-way comparison: Loan approval rate for customers having Credit_History (1)\n",
    "df=pd.crosstab(train [\"Credit_History\"], train [\"Loan_Status\"], margins=True).apply(percentageConvert, axis=1)\n",
    "loan_approval_with_Credit_1 = df['Y'][1]\n",
    "print \"%f percent of the applicants whose loans were approved have Credit_History equals to 1.\" %(loan_approval_with_Credit_1*100) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Credit_History\n",
       "0.0    0.078652\n",
       "1.0    0.795789\n",
       "All    0.687296\n",
       "Name: Y, dtype: float64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Y']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Dealing with missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender               13\n",
       "Married               3\n",
       "Dependents           15\n",
       "Education             0\n",
       "Self_Employed        32\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount           22\n",
       "Loan_Amount_Term     14\n",
       "Credit_History       50\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Number of variables with missing values\n",
    "variables_missing_value = train.isnull().sum()\n",
    "variables_missing_value "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Impute missing value of Loan_Amount_Term with median\n",
    "train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].median(), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Impute missing value of Self_Employed with more frequent category\n",
    "train['Self_Employed'].fillna('No',inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Treat Outliers of LoanAmount and Applicant Income"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x8ba7ac8>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nMbMmc71jZmZ986I/sCp3gCSl95rOn0/J2aH8/Km86JuZTRB3+j3c6ZtZk7nTNzOzvnnRH1iVO0CS\n0ntN58+n5OxQfv5UXvTNzCaIO/0e7vTNrMnc6ZuZWd+86A+syh0gSem9pvPnU3J2KD9/Ki/6ZmYT\nxJ1+D3f6ZtZk7vTNzKxvqy76km6WNC/p0a65z0p6QtIeSX8o6Q1d122TtK++/sJRBc+vyh0gSem9\npvPnU3J2KD9/qn6O9HcCF/XM7QLeGhEzwD5gG4Ckc4DLgS3AJcAX1elLzMysAfrq9CVtBu6MiLcv\nc92HgH8aER+TtBWIiNhRX3c38OmIeHCZ7dzpH2EfTXxszCy/JnT6VwF31T+fBDzbdd3Bes7MzBpg\nXcrGkn4TeCkifn+Q7WdnZ2m1WgBMTU0xMzNDu90GFnu3tR4vWhi3VxjfCMwsc32/2x95POrf98Yb\nb2zE4+38zchzNOPu/1eakGfc81dVxdzcHMDh9TJJRKx6ATYDj/bMzQJ/AhzXNbcVuK5r/E3g/BX2\nGU0EBEQfl90rzPe7/ZEuo39sdu/ePfL7GCXnz6fk7BHl56/Xh77W7uUu/Xb6LTqd/tvq8cXA54Cf\nj4gfdt3uHOArwPl0ap17gbfEMnfiTv/I+2jiY2Nm+aV2+qvWO5JupdM5nCDpGWA7cD2wHri3fnHO\nAxFxdUTslXQbsBd4Cbi6kSu7mdmEWvVEbkR8NCLeHBHHRcSpEbEzIt4SEZsj4tz6cnXX7T8TEWdE\nxJaI2DXa+DlVuQMkWXoOoyzOn0/J2aH8/Kn8jlwzswniz97p4U7fzJqsCa/TNzOzQnjRH1iVO0CS\n0ntN58+n5OxQfv5UXvTNzCaIO/0e7vTNrMnc6ZuZWd+86A+syh0gSem9pvPnU3J2KD9/Ki/6ZmYT\nxJ1+D3f6ZtZk7vTNzKxvXvQHVuUOkKT0XtP58yk5O5SfP5UXfTOzCeJOv4c7fTNrMnf6ZmbWt1UX\nfUk3S5qX9GjX3EZJuyQ9JekeSRu6rtsmaZ+kJyRdOKrg+VW5AyQpvdd0/nxKzg7l50/Vz5H+TuCi\nnrmtwH0RcRZwP7ANDn9d4uXAFuAS4Iuqv1rLzMzy6/c7cjfT+Y7ct9fjJ4H3RcS8pGmgioizJW2l\n86W9O+rb3Q18OiIeXGaf7vSPsI8mPjZmll+uTv/EiJgHiIhDwIn1/EnAs123O1jPmZlZAwzrRO4E\n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\n+u36eC0AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x8ac69b0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Add both ApplicantIncome and CoapplicantIncome to TotalIncome\n",
    "train['TotalIncome'] = train['ApplicantIncome'] + train['CoapplicantIncome']\n",
    "\n",
    "# Looking at the distribtion of TotalIncome\n",
    "train['LoanAmount'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x9874da0>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x8bf5358>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "# Perform log transformation of TotalIncome to make it closer to normal\n",
    "train['LoanAmount_log'] = np.log(train['LoanAmount'])\n",
    "\n",
    "# Looking at the distribtion of TotalIncome_log\n",
    "train['LoanAmount_log'].hist(bins=20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Preparation for Model Building"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from sklearn import preprocessing\n",
    "\n",
    "# Impute missing values for Gender\n",
    "train['Gender'].fillna(train['Gender'].mode()[0],inplace=True)\n",
    "\n",
    "# Impute missing values for Married\n",
    "train['Married'].fillna(train['Married'].mode()[0],inplace=True)\n",
    "\n",
    "# Impute missing values for Dependents\n",
    "train['Dependents'].fillna(train['Dependents'].mode()[0],inplace=True)\n",
    "\n",
    "# Impute missing values for Credit_History\n",
    "train['Credit_History'].fillna(train['Credit_History'].mode()[0],inplace=True)\n",
    "\n",
    "# Convert all non-numeric values to number\n",
    "cat_col=['Gender','Married','Dependents','Education','Self_Employed','Credit_History','Property_Area']\n",
    "for var in cat_col:\n",
    "    le = preprocessing.LabelEncoder()\n",
    "    train[var]=le.fit_transform(train[var].astype('str'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['Credit_History'].isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "LoanAmount_have_missing_value = train['LoanAmount'].isnull().sum() > 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "LoanAmount_have_missing_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Loan_ID               0\n",
       "Gender                0\n",
       "Married               3\n",
       "Dependents           15\n",
       "Education             0\n",
       "Self_Employed        32\n",
       "ApplicantIncome       0\n",
       "CoapplicantIncome     0\n",
       "LoanAmount            0\n",
       "Loan_Amount_Term     14\n",
       "Credit_History        0\n",
       "Property_Area         0\n",
       "Loan_Status           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ApplicantIncome</th>\n",
       "      <th>CoapplicantIncome</th>\n",
       "      <th>LoanAmount</th>\n",
       "      <th>Loan_Amount_Term</th>\n",
       "      <th>Credit_History</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>614.000000</td>\n",
       "      <td>614.000000</td>\n",
       "      <td>592.000000</td>\n",
       "      <td>600.00000</td>\n",
       "      <td>564.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5403.459283</td>\n",
       "      <td>1621.245798</td>\n",
       "      <td>146.412162</td>\n",
       "      <td>342.00000</td>\n",
       "      <td>0.842199</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>6109.041673</td>\n",
       "      <td>2926.248369</td>\n",
       "      <td>85.587325</td>\n",
       "      <td>65.12041</td>\n",
       "      <td>0.364878</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>150.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>12.00000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2877.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>3812.500000</td>\n",
       "      <td>1188.500000</td>\n",
       "      <td>128.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>5795.000000</td>\n",
       "      <td>2297.250000</td>\n",
       "      <td>168.000000</td>\n",
       "      <td>360.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>81000.000000</td>\n",
       "      <td>41667.000000</td>\n",
       "      <td>700.000000</td>\n",
       "      <td>480.00000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       ApplicantIncome  CoapplicantIncome  LoanAmount  Loan_Amount_Term  \\\n",
       "count       614.000000         614.000000  592.000000         600.00000   \n",
       "mean       5403.459283        1621.245798  146.412162         342.00000   \n",
       "std        6109.041673        2926.248369   85.587325          65.12041   \n",
       "min         150.000000           0.000000    9.000000          12.00000   \n",
       "25%        2877.500000           0.000000  100.000000         360.00000   \n",
       "50%        3812.500000        1188.500000  128.000000         360.00000   \n",
       "75%        5795.000000        2297.250000  168.000000         360.00000   \n",
       "max       81000.000000       41667.000000  700.000000         480.00000   \n",
       "\n",
       "       Credit_History  \n",
       "count      564.000000  \n",
       "mean         0.842199  \n",
       "std          0.364878  \n",
       "min          0.000000  \n",
       "25%          1.000000  \n",
       "50%          1.000000  \n",
       "75%          1.000000  \n",
       "max          1.000000  "
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Impute missing value of LoanAmount with 168\n",
    "train['LoanAmount'].fillna(168, inplace=True)\n",
    "\n",
    "# Impute missing value of LoanAmount with median\n",
    "#train['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "129.0"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['LoanAmount'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "train['Gender'].fillna('Male',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0    475\n",
       "0.0     89\n",
       "Name: Credit_History, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train['Credit_History'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "train['Credit_History'].fillna(1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
