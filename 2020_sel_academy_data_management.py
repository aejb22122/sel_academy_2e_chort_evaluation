#!/usr/bin/env python
# coding: utf-8

# # SEL Academy survey data analysis

# First thing set the working directory - it is done by setting it in the folder
# icon to the right;

# Next step is to import all the library we will need

# Libraries

import pandas as pd
import numpy as np
import seaborn as sns  # for plots
import matplotlib.pyplot as plt  # for plots
import statsmodels.formula.api as smf  # statsmodels
import statsmodels.stats.multicomp as multi  # statsmodels and posthoc test
import statsmodels.api as sm  # Statsmodel for the qqplots
import scipy.stats  # For the Chi-Square test of independance

# Machine learning libraries
# Libraries for decision trees

from pandas import Series, DataFrame
import os


# In[]:
# Importing the data set 
# to prevent uft-8 encoding errors open it in exell and save it in ms DOS csv
df = pd.read_csv("2020_04_17_sel_academy_series_feedback_survey_2020.csv", low_memory=False)

pd.set_option('display.max_columns', None) # Display all the columns

df.head(3)

# The variable names
for col in df:
    print(col)

# First set of data cleaning :
# Removing the first row of the dataframe
df = df.drop([0])

df.head(3)
print(len(df)) # Number of participants
df.dtypes

len(df)

# In[Q19]:
# Site/program



# =============================================================================
# Data management and frequency tables
# =============================================================================
# Q9 Which OST SEL Academy trainings have you attended? (Please check all that apply.)

# ------  Q9:1	Which OST SEL Academy trainings have you attended? 

print("Which OST SEL Academy have you attended? (Check all that apply)")
df.dtypes[['Q9:1']]
df['Q9:1'].describe()

# Check the nature of the vartiables
print(df['Q9:1'].value_counts(sort=False, dropna = False)) # This show the NaN so we can recode them

# Recoding by creating a new variable
def Q9_1(row):
    if row['Q9:1'] == 'SEL l':
        return 1
    else:
        return 0

# This variable is then added to the dataframe
df["Q9_1"] = df.apply(lambda row: Q9_1(row), axis = 1)
df['Q9_1'].describe()

# Verify

print(df['Q9_1'].value_counts(sort=False, dropna = False)) # We can recode the NaNs
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_1")
print(df['Q9:1'].value_counts(sort=False, dropna = False))

# ------ Q9:2 	Which OST SEL Academy trainings have you attended? 

df.dtypes[['Q9:2']]
df['Q9:2'].describe()

# Verify the variable distribution
print(df['Q9:2'].value_counts(sort = False, dropna = False))

# Recoding by creating a new variable
def Q9_2(row):
    if row['Q9:2'] == 'SEL ll':
        return 1
    else:
        return 0

# The new created variable is then added to the dataset
df["Q9_2"] = df.apply(lambda row: Q9_2(row), axis = 1)

# Let's verify that all is correct
print(df['Q9_2'].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_2")
print(df["Q9:2"].value_counts(sort = False, dropna = False))


# ------ Q9:3 	Which OST SEL Academy trainings have you attended? 

df.dtypes[["Q9:3"]]
df['Q9:3'].describe()

# The variable's distribution
print(df["Q9:3"].value_counts(sort = False, dropna = False))

# Recording and creating a new variable
def Q9_3(row):
    if row["Q9:3"] == "SEL lll":
        return 1
    else:
        return 0

# This variable is then added to the dataframe
df['Q9_3'] = df.apply(lambda row: Q9_3(row), axis = 1)

# Let's verify that all is correct
print(df["Q9:3"].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_3")
print(df['Q9_3'].value_counts(sort = False, dropna = False))

# ------ Q9:4 	Which OST SEL Academy trainings have you attended? 

df.dtypes[["Q9:4"]]
df['Q9:4'].describe()

# How does the variable distribution look like?
print(df["Q9:4"].value_counts(sort = False, dropna = False))

# Recoding the variables
def Q9_4(row):
    if row['Q9:4'] == 'SEL lV':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q9_4'] = df.apply(lambda row: Q9_4(row), axis = 1)

# check if all is right
print(df['Q9:4'].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_4")
print(df['Q9_4'].value_counts(sort = False, dropna = False))

# ---- Q9:5	Which OST SEL Academy trainings have you attended? 

df.dtypes[["Q9:5"]]
df['Q9:5'].describe()

# How does the variable distribution look like?
print(df["Q9:5"].value_counts(sort = False, dropna = False))

# Recoding the variables
def Q9_5(row):
    if row['Q9:5'] == 'SEL V':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q9_5'] = df.apply(lambda row: Q9_5(row), axis = 1)

# check if all is right
print(df['Q9:5'].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_5")
print(df['Q9_5'].value_counts(sort = False, dropna = False))


# ---- Q9:6	Which OST SEL Academy trainings have you attended? 

df.dtypes[["Q9:6"]]
df['Q9:6'].describe()

# How does the variable distribution look like?
print(df["Q9:6"].value_counts(sort = False, dropna = False))

# Recoding the variables
def Q9_6(row):
    if row['Q9:6'] == 'SEL Vl':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q9_6'] = df.apply(lambda row: Q9_6(row), axis = 1)

# check if all is right
print(df['Q9:6'].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_6")
print(df['Q9_6'].value_counts(sort = False, dropna = False))

# ---- Q9:7	Which OST SEL Academy trainings have you attended? 

df.dtypes[["Q9:7"]]
df['Q9:7'].describe()

# How does the variable distribution look like?
print(df["Q9:7"].value_counts(sort = False, dropna = False))

# Recoding the variable
def Q9_7(row):
    if row['Q9:7'] == 'SEL Vll':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q9_7'] = df.apply(lambda row: Q9_7(row), axis = 1)

# check if all is right
print(df['Q9:7'].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_7")
print(df['Q9_7'].value_counts(sort = False, dropna = False))

# ---- Q9:8	Which OST SEL Academy trainings have you attended? 

df.dtypes[['Q9:8']]
df['Q9:8'].describe()

print(df['Q9:8'].value_counts(sort = False, dropna = False))

# Recoding and creating a new variable
def Q9_8(row):
    if row['Q9:8'] == 'SEL Vlll':
        return 1
    else:
        return 0
    
df['Q9_8'] = df.apply(lambda row: Q9_8(row), axis = 1)

# Verifications
print(df['Q9:8'].value_counts(sort = False, dropna = False))
print("Which OST SEL Academy have you attended? (Check all that apply) Q9_8")
print(df['Q9_8'].value_counts(sort = False, dropna = False))


# ### Participation in SEL academy trainings

df['training_participation'] = df['Q9_1'] + df['Q9_2'] + df['Q9_3'] + df['Q9_4'] + df['Q9_5'] + df['Q9_6'] + df['Q9_7'] + df['Q9_8']

print('Number of training sessions attented?')
print(df['training_participation'].value_counts(sort = False, dropna = False))


# Counts of trainings attendance and frequency
df_sub1 = df[['Q9_1', 'Q9_2', 'Q9_3', 'Q9_4', 'Q9_5', 'Q9_6', 'Q9_7', 'Q9_8']]

print('Which OST SEL Academy trainings have you attended? (Sum) :')
df_sub1.sum()

print('Which OST SEL Academy trainings have you attended? (Frequency) :')
df_sub1.sum()/len(df_sub1)*100


# In[25]:
# ### Question : How often do you identify the name the SEL competencies or skills in your interaction with adults and youth?
# Q10	How often do you identify the name the SEL competencies  ...

df.dtypes[['Q10']]
# Let's transform this variable

print(df['Q10'].value_counts(sort = False, dropna = False))


# Let' create a new variable ... 
def question10(row):
    if row['Q10'] == "Very rarely":
        return 0
    if row['Q10'] == "Rarely":
        return 1
    if row['Q10'] == "Sometimes":
        return 2
    if row['Q10'] == "Often":
        return 3
    if row['Q10'] == "Very often":
        return 4
    else:
        return 0


# ... and add it to the dataset

df['question10'] = df.apply(lambda row: question10 (row), axis = 1)


print(df['Q10'].value_counts(sort = False, dropna = False)/len(df))
print(df['question10'].value_counts(sort = False, dropna = False))

# In[]:

## How often do you use common SEL terminology and language in communication and interactions with adults and youth?

print(df['Q11'].value_counts(sort = False, dropna = False)/len(df)*100)


# Let' create a new variable ... 
def question11(row):
    if row['Q11'] == "Very rarely":
        return 0
    if row['Q11'] == "Rarely":
        return 1
    if row['Q11'] == "Sometimes":
        return 2
    if row['Q11'] == "Often":
        return 3
    if row['Q11'] == "Very often":
        return 4
    else:
        return 0

# ... and add it to the dataset

df['question11'] = df.apply(lambda row: question11 (row), axis = 1)


print(df['question11'].value_counts(sort = False, dropna = False))

# In[]

# =============================================================================
# # ## Foundations in SEL 1
# =============================================================================

# ### Question 12 How often have you been able to use any self-awareness practices and tools? (mindful breathing, power pause, body scan, reflection etc.)
# Q12	How often have you been able to use any self-awareness practices and tools?

print(df['Q12'].value_counts(sort = False, dropna = False))

# Let' create a new variable ... 
def question12(row):
    if row['Q12'] == "Very rarely":
        return 0
    if row['Q12'] == "Rarely":
        return 1
    if row['Q12'] == "Sometimes":
        return 2
    if row['Q12'] == "Often":
        return 3
    if row['Q12'] == "Very often":
        return 4
    else:
        return 0


# ... and add it to the dataset
df['question12'] = df.apply(lambda row: question12 (row), axis = 1)

# verifications
print(df['Q12'].value_counts(sort = False, dropna = False)/len(df)*100)
print(df['question12'].value_counts(sort = False, dropna = False))


# Question 13 is an open-ended free form question.
# Question 14 (How often have you been able to use any Responsive Classroom practices and tools in your program?) is missing and the subsequent open-ended question also.

# In[]

# Q14 How confident are you in your ability to use self-regulation practices and tools in your work or personal life?
print(df['Q14'].value_counts(sort = False, dropna = False))


def question14 (row):
    if row['Q14'] == 'Very rarely':
        return 0
    if row['Q14'] == 'Rarely':
        return 1
    if row['Q14'] == 'Sometimes':
        return 2
    if row['Q14'] == 'Very often':
        return 3
    if row['Q14'] == 'Often':
        return 4
    else:
        return 0

df['question14'] = df.apply(lambda row: question14(row), axis = 1)

print(df['Q14'].value_counts(sort = False, dropna = False))
print(df['question14'].value_counts(sort = False, dropna = False))
    
print(df['question14'].value_counts(sort = False, dropna = False)/len(df)*100)

# In[]
# =============================================================================
# ### Foundations in SEL II
# =============================================================================

# Question 16 How much has your awareness of your multiple identities increased 
# since you attended the training (race, culture, spoken language, gender, profession, age, etc)?

# Q16	How much has your awareness of your multiple identities increased ...

print(df['Q16'].value_counts(sort = False, dropna = False)/len(df))

# Let' create a new variable ... 
def question16 (row):
    if row['Q16'] == "Not at all":
        return 0
    if row['Q16'] == "Very little":
        return 1
    if row['Q16'] == "Somewhat":
        return 2
    if row['Q16'] == "A lot":
        return 3
    if row['Q16'] == "Very much":
        return 4
    else:
        return 0


# adding this to the dataset
# ... and add it to the dataset
df['question16'] = df.apply(lambda row: question16 (row), axis = 1)

# Verifications
print(df['Q16'].value_counts(sort = False, dropna = False))

print(df['question16'].value_counts(sort = False, dropna = False))

# In[ ]:
# How much has your ability to be empathetic in your personal life and at work increased since
# attending the trainings?

print('Q19	Have you noticed an increase in your ability to be empathetic in your personal life and at work since attending the trainings?')
print(df['Q19'].value_counts(sort = False, dropna = False)/len(df)*100)

# Let's create a new variable 
def question19 (row):
    if row['Q19'] == 'Not at all':
        return 0
    if row['Q19'] == 'Very little':
        return 1
    if row['Q19'] == 'Somewhat':
        return 2
    if row['Q19'] == 'A lot':
        return 3
    if row['Q19'] == 'Very much':
        return 4
    else:
        return 0

# This variable is then added to the dataset as so ...
df['question19'] = df.apply(lambda row: question19(row), axis = 1)

# Verifications ...
print(df['Q19'].value_counts(sort = False, dropna = False))
print(df['question19'].value_counts(sort = False, dropna = False))

# In[ ]:
# Which component(s) of Afternoon Meeting do you typically practice with youth (select all relevant
# responses):
# Questions 20:1 to 20:6

# ------ Afternnon meeting --- 'Greeting' question response

print("Which component(s) of Afternoon Meeting do you typically practice with youth (select all relevant responses):")
df.dtypes[['Q20:1']]
df['Q20:1'].describe()

# Check the nature of the vartiables
print(df['Q20:1'].value_counts(sort=False, dropna = False)) # This show the NaN so we can recode them

# Recoding by creating a new variable
def Q20_1(row):
    if row['Q20:1'] == 'Greeting':
        return 1
    else:
        return 0

# This variable is then added to the dataframe
df["Q20_1"] = df.apply(lambda row: Q20_1(row), axis = 1)


# Verify

print(df['Q20_1'].value_counts(sort=False, dropna = False)) # We can recode the NaNs
print(df['Q20:1'].value_counts(sort=False, dropna = False))

# ------ Afternnon meeting --- 'Sharing' question response 

# Verify the variable distribution
print(df['Q20:2'].value_counts(sort = False, dropna = False))

# Recoding by creating a new variable
def Q20_2(row):
    if row['Q20:2'] == 'Sharing':
        return 1
    else:
        return 0

# The new created variable is then added to the dataset
df["Q20_2"] = df.apply(lambda row: Q20_2(row), axis = 1)

# Let's verify that all is correct
print(df['Q20_2'].value_counts(sort = False, dropna = False))
print(df["Q20:2"].value_counts(sort = False, dropna = False))


# ------ Afternnon meeting --- 'Activity' question response 
# The variable's distribution
print(df["Q20:3"].value_counts(sort = False, dropna = False))

# Recording and creating a new variable
def Q20_3(row):
    if row["Q20:3"] == "Activity":
        return 1
    else:
        return 0

# This variable is then added to the dataframe
df['Q20_3'] = df.apply(lambda row: Q20_3(row), axis = 1)

# Let's verify that all is correct
print(df["Q20:3"].value_counts(sort = False, dropna = False))
print(df['Q20_3'].value_counts(sort = False, dropna = False))

# ------ Afternnon meeting --- 'Message' question response 

# How does the variable distribution look like?
print(df["Q20:4"].value_counts(sort = False, dropna = False))

# Recoding the variables
def Q20_4(row):
    if row['Q20:4'] == 'Message':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q20_4'] = df.apply(lambda row: Q20_4(row), axis = 1)

# checking if all is right
print(df['Q20:4'].value_counts(sort = False, dropna = False))
print(df['Q20_4'].value_counts(sort = False, dropna = False))

# ------ Afternnon meeting --- 'Message' question response 
# How does the variable distribution look like?
print(df["Q20:5"].value_counts(sort = False, dropna = False))

# Recoding the variables
def Q20_5(row):
    if row['Q20:5'] == 'None of the above':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q20_5'] = df.apply(lambda row: Q20_5(row), axis = 1)

# check if all is right
print(df['Q20:5'].value_counts(sort = False, dropna = False))
print(df['Q20_5'].value_counts(sort = False, dropna = False))


# ------ Afternnon meeting --- 'Message' question response 

# How does the variable distribution look like?
print(df["Q20:6"].value_counts(sort = False, dropna = False))

# Recoding the variables
def Q20_6(row):
    if row['Q20:6'] == 'Not applicable':
        return 1
    else:
        return 0

# This variable is now added to the dataset
df['Q20_6'] = df.apply(lambda row: Q20_6(row), axis = 1)

# check if all is right
print(df['Q20:6'].value_counts(sort = False, dropna = False))
print(df['Q20_6'].value_counts(sort = False, dropna = False))

# We can then create a variable representing the components of Afternoon Mettings
# df['components'] = df['Q20_1'] + df['Q20_2'] + df['Q20_3'] + df['Q20_4'] + df['Q20_5'] + df['Q20_6']
# df['components'] 

# # creating a subset of the data with these variables 
df_sub0 = df[['Q20_1', 'Q20_2', 'Q20_3', 'Q20_4', 'Q20_5', 'Q20_6']]
df_sub0.head()
df_sub0.mean()

print("Respondent's implementation of 'Afternoon Meeting':")
df_sub0.sum()

print("Respondent's frequency of 'Afternoon Meeting' parctices:")
df_sub0.sum()/len(df_sub0)*100




# In[]
# Q21 How often are Afternoon Meetings conducted in your program?

# ---- Every day of the week selected

print(df['Q21:1'].value_counts(sort = False, dropna = False))

def Q21_1(row):
    if row['Q21:1'] == 'Every day of the week':
        return 1
    else:
        return 0

# We can now add it to the dataset
df['Q21_1'] = df.apply(lambda row: Q21_1(row), axis = 1)

# Verification
print(df['Q21:1'].value_counts(sort = False, dropna = False))
print(df['Q21_1'].value_counts(sort = False, dropna = False))

# ---- Several days a week selected
print(df['Q21:2'].value_counts(sort = False, dropna = False))

def Q21_2(row):
    if row['Q21:2'] == 'Several days a week':
        return 1
    else:
        return 0

# Adding this variable to the dataset
df['Q21_2'] = df.apply(lambda row: Q21_2(row), axis = 1)

# Verifications
print(df['Q21_2'].value_counts(sort = False, dropna = False))
print(df['Q21:2'].value_counts(sort = False, dropna = False))

# ---- Once a week is selected 
print(df['Q21:3'].value_counts(sort = False, dropna = False))

def Q21_3(row):
    if row['Q21:3'] == 'Once a week':
        return 1
    else:
        return 0
    
# Adding this variable's function to the dataset to create a new variable
df['Q21_3'] = df.apply(lambda row: Q21_3(row), axis = 1)

# Let's verify that all is well
print(df['Q21:3'].value_counts(sort = False, dropna = False))
print(df['Q21_3'].value_counts(sort = False, dropna = False))

# ----- Once every 2 to 3 weeks
print(df['Q21:4'].value_counts(sort = False, dropna = False))

def Q21_4(row):
    if row['Q21:4'] == 'Once every 2 to 3 weeks':
        return 1
    else:
        return 0

# Adding to the dataset
df['Q21_4'] = df.apply(lambda row: Q21_4(row), axis = 1)

# Verifications
print(df['Q21:4'].value_counts(sort = False, dropna = False))
print(df['Q21_4'].value_counts(sort = False, dropna = False))

# ----- Never
print(df['Q21:5'].value_counts(sort = False, dropna = False))

def Q21_5(row):
    if row['Q21:5'] == 'Never':
        return 1
    else:
        return 0

# Adding the variable to the dataset
df['Q21_5'] = df.apply(lambda row: Q21_5(row), axis = 1)

# Verifications
print(df['Q21:5'].value_counts(sort = False, dropna = False))
print(df['Q21_5'].value_counts(sort = False, dropna = False))

# Create a sub dataset from the main data
df_sub2 = df[['Q21_1', 'Q21_2', 'Q21_3', 'Q21_4', 'Q21_5']]

# Getting the sums and the frequencies
print("How often are Afternoon Meetings conducted in your program? (sum)")
df_sub2.sum()

print('How often are Afternoon Meetings conducted in your program? (frequencies')
df_sub2.sum()/len(df_sub2)*100

# df_sub2.plot.box()

# In[]
#  Question 23 (Q23a : Q23g) How often do you implement these SEL tools and practices throughout 
# your program with coworkers and/or youth?

print('How often do you implement these SEL tools and practices throughout your', end ='')
print(' program with co-workers and/or youth?')

# ---- Circle seating structure

print(df['Q23a'].value_counts(sort = False, dropna = False))

def Q23_1(row):
    if row['Q23a'] == 'Never':
        return 0
    if row['Q23a'] == 'Once a week':
        return 1
    if row['Q23a'] == 'Twice a Week':
        return 2
    if row['Q23a'] == 'Three times a week':
        return 3
    if row['Q23a'] == 'Four or more times a week':
        return 4
    else:
        return 0

df['Q23_1'] = df.apply(lambda row: Q23_1(row), axis = 1)

print(df['Q23_1'].value_counts(sort = False, dropna = False)/len(df)*100)
print(df['Q23a'].value_counts(sort = False, dropna = False)/len(df)*100)

# ---- Group agreements
print(df['Q23b'].value_counts(sort = False, dropna = False))

def Q23_2(row):
    if row['Q23b'] == 'Never':
        return 0
    if row['Q23b'] == 'Once a week':
        return 1
    if row['Q23b'] == 'Twice a Week':
        return 2
    if row['Q23b'] == 'Three times a week':
        return 3
    if row['Q23b'] == 'Four or more times a week':
        return 4
    else:
        return 0

df['Q23_2'] = df.apply(lambda row: Q23_2(row), axis = 1)

print(df['Q23b'].value_counts(sort = False, dropna = False)/len(df))
print(df['Q23_2'].value_counts(sort = False, dropna = False))

# ---- Welcoming rituals

print(df['Q23c'].value_counts(sort = False, dropna = False))

def Q23_3(row):
    if row['Q23c'] == 'Never':
        return 0
    if row['Q23c'] == 'Once a week':
        return 1
    if row['Q23c'] == 'Twice a Week':
        return 2
    if row['Q23c'] == 'Three times a week':
        return 3
    if row['Q23c'] == 'Four or more times a week':
        return 4
    else:
        return 0
    
df['Q23_3'] = df.apply(lambda row: Q23_3(row), axis = 1)

print(df['Q23_3'].value_counts(sort = False, dropna = False))
print(df['Q23c'].value_counts(sort = False, dropna = False)/len(df))

# ---- Transition pauses/activities

print(df['Q23d'].value_counts(sort = False, dropna = False))

def Q23_4(row):
    if row['Q23d'] == 'Never':
        return 0
    if row['Q23d'] == 'Once a week':
        return 1
    if row['Q23d'] == 'Twice a Week':
        return 2
    if row['Q23d'] == 'Three times a week':
        return 3
    if row['Q23d'] == 'Four or more times a week':
        return 4
    else:
        return 0


df['Q23_4'] = df.apply(lambda row: Q23_4(row), axis = 1)

print(df['Q23d'].value_counts(sort = False, dropna = False)/len(df))
print(df['Q23_4'].value_counts(sort = False, dropna = False))


# ---- Attention cues

print(df['Q23e'].value_counts(sort = False, dropna = False))

def Q23_5(row):
    if row['Q23e'] == 'Never':
        return 0
    if row['Q23e'] == 'Once a week':
        return 1
    if row['Q23e'] == 'Twice a Week':
        return 2
    if row['Q23e'] == 'Three times a week':
        return 3
    if row['Q23e'] == 'Four or more times a week':
        return 4
    else:
        return 0
    
df['Q23_5'] = df.apply(lambda row : Q23_5(row), axis = 1)

print(df['Q23e'].value_counts(sort = False, dropna = False)/len(df)*100)
print(df['Q23_5'].value_counts(sort = False, dropna = False))

# ---- Brain breaks

print(df['Q23f'].value_counts(sort = False, dropna = False))

def Q23_6(row):
    if row['Q23f'] == 'Never':
        return 0
    if row['Q23f'] == 'Once a week':
        return 1
    if row['Q23f'] == 'Twice a Week':
        return 2
    if row['Q23f'] == 'Three times a week':
        return 3
    if row['Q23f'] == 'Four or more times a week':
        return 4
    else:
        return 0

 
df['Q23_6'] = df.apply(lambda row : Q23_6(row), axis = 1)

print(df['Q23f'].value_counts(sort = False, dropna = False)/len(df)*100)
print(df['Q23_6'].value_counts(sort = False, dropna = False))

# ---- Optimistic closure

print(df['Q23g'].value_counts(sort = False, dropna = False))

def Q23_7(row):
    if row['Q23g'] == 'Never':
        return 0
    if row['Q23g'] == 'Once a week':
        return 1
    if row['Q23g'] == 'Twice a Week':
        return 2
    if row['Q23g'] == 'Three times a week':
        return 3
    if row['Q23g'] == 'Four or more times a week':
        return 4
    else:
        return 0

df['Q23_7'] = df.apply(lambda row : Q23_7(row), axis = 1)

print(df['Q23g'].value_counts(sort = False, dropna = False)/len(df)*100)
print(df['Q23_7'].value_counts(sort = False, dropna = False))

# In[]


# =============================================================================
# SEL IV
# =============================================================================

# How often do you use strategies to take multiple perspectives and diverse needs of those around you
# into account (checking assumptions and misperceptions, open-ended questions and choices, looking
# from a different perspective, reflection, etc.)?

# Q25 How often do you use strategies to take multiple perspect...
print(df['Q25'].value_counts(sort = False, dropna = False)/len(df))

# Let's create a new variable 
def question25 (row):
    if row['Q25'] == 'Very rarely':
        return 0
    if row['Q25'] == 'Rarely':
        return 1
    if row['Q25'] == 'Sometimes':
        return 2
    if row['Q25'] == 'Often':
        return 3
    if row['Q25'] == 'Very often':
        return 4
    else:
        return 0

# This variable is then added to the dataset as so ...
df['question25'] = df.apply(lambda row: question25(row), axis = 1)

# Verifications ...
print(df['Q25'].value_counts(sort = False, dropna = False))
print(df['question25'].value_counts(sort = False, dropna = False))

# In[]

# Q27 How often are you aware of and able to notice and name stressors and your reactions (sensations,
# thoughts, emotions, behavior)?
print(df['Q27'].value_counts(sort = False, dropna = False)/len(df)*100)

def question27 (row):
    if row['Q27'] == 'Very rarely':
        return 0
    if row['Q27'] == 'Rarely':
        return 1
    if row['Q27'] == 'Sometimes':
        return 2
    if row['Q27'] == 'Often':
        return 3
    if row['Q27'] == 'Very often':
        return 4
    else:
        return 0
    
df['question27'] = df.apply(lambda row: question27(row), axis = 1)

# Verifications... 
print(df['Q27'].value_counts(sort = False, dropna = False))
print(df['question27'].value_counts(sort = False, dropna = False))

# In[]
# How often do you guide youth to reflect on and regulate their emotions using positive and proactive
# approach to discipline (proximity, logical consequence, self-regulation space, restorative actions, etc.)?
# Q29 How often do you guide youth to reflect on and regulate t...

print(df['Q29'].value_counts(sort = False, dropna = False))

def question29 (row):
    if row['Q29'] == 'Very rarely':
        return 0
    if row['Q29'] == 'Rarely':
        return 1
    if row['Q29'] == 'Sometimes':
        return 2
    if row['Q29'] == 'Often':
        return 3
    if row['Q29'] == 'Very often':
        return 4
    else:
        return 0

df['question29'] = df.apply(lambda row : question29(row), axis = 1)

print(df['Q29'].value_counts(sort = False, dropna = False)/len(df)*100)
print(df['question29'].value_counts(sort = False, dropna = False))

# In[]
# =============================================================================
# SEL V
# =============================================================================

# How often do you use practices to build self-care and resilience (journaling, mindfulness, exercise,
# mindful walking, healthy eating and nutrition, self-compassion exercises, spend time outdoors/nature,
# etc)

# Q30 	How often do you use practices to build self-care and res...
print(df['Q30'].value_counts(sort = False, dropna = False)/len(df)*100)

def question30(row):
    if row['Q30'] == 'Very rarely':
        return 0
    if row['Q30'] == 'Rarely':
        return 1
    if row['Q30'] == 'Sometimes':
        return 2
    if row['Q30'] == 'Often':
        return 3
    if row['Q30'] == 'Very often':
        return 4
    else:
        return 0

df['question30'] = df.apply(lambda row: question30(row), axis = 1)

print(df['Q30'].value_counts(sort = False, dropna = False))
print(df['question30'].value_counts(sort = False, dropna = False))


# In[]

# Q32 	How much has your ability to be empathetic in your person...
# How much has your ability to be empathetic in your personal life and at work increased since
# attending the trainings?

print(df['Q32'].value_counts(sort = False, dropna = False))

def question32 (row):
    if row['Q32'] == 'Not at all':
        return 0
    if row['Q32'] == 'Very little':
        return 1
    if row['Q32'] == 'Somewhat':
        return 2
    if row['Q32'] == 'A lot':
        return 3
    if row['Q32'] == 'Very much':
        return 4
    else:
        return 0

df['question32'] = df.apply(lambda row : question32(row), axis = 1)


print(df['Q32'].value_counts(sort = False, dropna = False))

# We can also get the percentages
print(df['question32'].value_counts(sort = False, dropna = False)/len(df)*100)

# In[]

# How frequently do you use Positive Language (reminding, reinforcing and redirecting language, openended
# questions, nonviolent communication, solutions and growth mindset focus, etc.) in interactions
# with youth?

# Q33 How frequently do you use Positive Language (reminding, r...
print(df['Q33'].value_counts(sort = False, dropna = False))

def question33 (row):
    if row['Q33'] == 'Very rarely':
        return 0
    if row['Q33'] == 'Rarely':
        return 1
    if row['Q33'] == 'Sometimes':
        return 2
    if row['Q33'] == 'Often':
        return 3
    if row['Q33'] == 'Very often':
        return 4
    else:
        return 0
    
df['question33'] = df.apply(lambda row : question33(row), axis = 1)

print(df['Q33'].value_counts(sort = False, dropna = False))
print(df['question33'].value_counts(sort = False, dropna = False))


# In[]

# How much has your ability to effectively build healthy and rewarding relationships in your personal life
# and at work increased since attending the trainings?

# Q34 How much has your ability to effectively build healthy an...

print(df['Q34'].value_counts(sort = False, dropna = False))

def question34 (row):
    if row['Q34'] == 'Not at all':
        return 0
    if row['Q34'] == 'Very little':
        return 1
    if row['Q34'] == 'Somewhat':
        return 2
    if row['Q34'] == 'A lot':
        return 3
    if row['Q34'] == 'Very much':
        return 4
    else:
        return 0

df['question34'] = df.apply(lambda row: question34(row), axis = 1)

print(df['Q34'].value_counts(sort = False, dropna = False))
print(df['question34'].value_counts(sort = False, dropna = False))

# In[]

# How often have you been able to use any implicit bias awareness and de-biasing practices and tools
# (mindful inquiry, self-awareness exercises, multiple identities reflection, perspective checking,
# compassion practices, cultural exposure, etc.)?

# Q36 	How often have you been able to use any implicit bias awa...

print(df['Q36'].value_counts(sort = False, dropna = False))

def question36(row):
    if row['Q36'] == 'Very rarely':
        return 0
    if row['Q36'] == 'Rarely':
        return 1
    if row['Q36'] == 'Sometimes':
        return 2
    if row['Q36'] == 'Often':
        return 3
    if row['Q36'] == 'Very often':
        return 4
    else:
        return 0


df['question36'] = df.apply(lambda row: question36(row), axis = 1)

print(df['Q36'].value_counts(sort = False, dropna = False))
print(df['question36'].value_counts(sort = False, dropna = False))


# In[]

# How often are you using SIT (signature practices, inquiry, thematic connection) to integrate SEL in
# regular program activities/cafeteria/playground, outside of Afternoon Meeting time?

# Q38 	How often are you using SIT (signature practices, inquiry...

print(df['Q38'].value_counts(sort = False, dropna = False))

def question38 (row):
    if row['Q38'] == 'Never':
        return 0
    if row['Q38'] == 'Once a week':
        return 1
    if row['Q38'] == 'Twice a week':
        return 2
    if row['Q38'] == 'Three times a week':
        return 3
    if row['Q38'] == 'Four or more times a week':
        return 4
    else:
        return 0
    
df['question38'] = df.apply(lambda row: question38(row), axis = 1)

print(df['Q38'].value_counts(sort = False, dropna = False))
print(df['question38'].value_counts(sort = False, dropna = False))

# In[]

# How often are you implementing Second Step activities?
# Q40 How often are you implementing Second Step activities? 

print(df['Q40'].value_counts(sort = False, dropna = False))

def question40 (row):
    if row['Q40'] == 'Never':
        return 0
    if row['Q40'] == 'Once a week':
        return 1
    if row['Q40'] == 'Twice a week':
        return 2
    if row['Q40'] == 'Three times a week':
        return 3
    if row['Q40'] == 'Four or more times a week':
        return 4
    else:
        return 0
    
df['question40'] = df.apply(lambda row: question40(row), axis = 1)

print(df['Q40'].value_counts(sort = False, dropna = False))
print(df['question40'].value_counts(sort = False, dropna = False))


# In[]

# Frequency tables with frequencies :

pd.crosstab(df['training_participation'],df['Q36'], normalize = 'index')

pd.crosstab(df['training_participation'], df['Q38'], normalize = 'index')

pd.crosstab(df['training_participation'], df['Q40'], normalize = 'index')
