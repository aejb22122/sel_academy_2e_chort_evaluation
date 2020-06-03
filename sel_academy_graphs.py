# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:39:23 2020

@author: annick-eudes
"""
import pandas as pd
import numpy as np
import seaborn as sns  # for plots
import matplotlib.pyplot as plt  # for plots
sns.palplot(sns.color_palette("Blues"))
sns.set(style="darkgrid")

# In[]
# Participation in SEL academy trainings
# Refer to the previsous scrip for this 

# -------------- NO NOT RUN THESES 2 LINES OF CODES! -----------------

df = pd.read_csv("sel_academy_series_feedback_survey_04_10_2020.csv", low_memory=False)
df_sub1 = df[['Q9_1', 'Q9_2', 'Q9_3', 'Q9_4', 'Q9_5', 'Q9_6', 'Q9_7', 'Q9_8']]

# In[]


print('Which OST SEL Academy trainings have you attended? (Sum) :')
df_sub1.sum()

print('Which OST SEL Academy trainings have you attended? (Frequency) :')
df_sub1.sum()/len(df_sub1)*100

# Let's rename the columns to make the plot cleaner 
df_sub1 = df_sub1.rename(columns={"Q9_1": "SEL I", "Q9_2": "SEL II", 'Q9_3' : 'SEL III', 'Q9_4' : 'SEL IV', 'Q9_5': 'SEL V', 'Q9_6': 'SEL VI', 'Q9_7': 'SEL VII', 'Q9_8':'SEL VIII'})

print('Which OST SEL Academy trainings have you attended? (Sum) :')
df_sub1.sum().plot.bar()
#df_sub1.sum().plot.barh()
#plt.title("Simple Horizontal Bar graph")
plt.xlabel("OST SEL Academy training attended")
#plt.ylabel('')


print('Which OST SEL Academy trainings have you attended? (Frequency) :')
x = df_sub1.sum()/len(df_sub1)
x.plot.bar()


# In[]

sns.set_style("darkgrid", {"axes.facecolor": ".9"})
# Univariate graphs
sns.countplot(x="question10", data = df) # , palette = 'Blues'
plt.xlabel('Identify SEL competencies')

#plt.title(' ')

# bivariate bar graph C -> Q
# How oftern do you identify SEL competencies or skills in your interaction with adults and Youths ?  
# Vs number of training sessions

sns.catplot(x = 'training_participation', y = 'question10', palette= 'Blues', data = df, kind = 'bar', ci =None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Identify SEL competencies')

sns.catplot(x = 'training_participation', y = 'Q10', palette= 'Blues', data = df, kind = 'bar', ci =None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Identify SEL competencies')

# In[]

# Univariate graphs
sns.countplot(x="question11", data = df)
plt.xlabel('Use of common SEL terminology and language')

# bivariate bar graph C -> Q
## How often do you use common SEL terminology and language in communication and interactions with adults and youth?
# Vs Number of training sessions attended

sns.catplot(x = 'training_participation', y = 'question11', palette = 'Blues', data = df, kind = 'bar', ci = None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of common SEL terminology and language')

# In[]
# Univariate graphs
# ### Question 12 How often have you been able to use any self-awareness practices and tools? (mindful breathing, power pause, body scan, reflection etc.)
# Q12	How often have you been able to use any self-awareness practices and tools?

sns.countplot( x= 'question12', data = df)
plt.xlabel('use any self-awareness practices and tools')

sns.countplot( x= 'Q12', data = df)
plt.xlabel('use any self-awareness practices and tools')

sns.catplot(x = 'training_participation', y = 'question12', palette = 'Blues', data = df, kind = 'bar', ci = None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of self-awareness practices and tools')




# In[]
# Univariate graphs
# Q14 How confident are you in your ability to use self-regulation practices and tools in your work or personal life?

sns.countplot(x = 'question14', data = df)
plt.xlabel('Use of Responsive Classroom')
#plt.xlabel('Use self-regulation practices and tools')

sns.catplot(x = 'training_participation', y = 'question14', palette = 'Blues', data = df, kind = 'bar', ci = None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of Responsive Classroom')
#plt.ylabel('Use self-regulation practices and tools')

# In[]
# Question 16 How much has your awareness of your multiple identities increased 
# since you attended the training (race, culture, spoken language, gender, profession, age, etc)?

# Univariate graphs
sns.countplot(x = 'question16', data = df)
plt.xlabel('Increased awareness of your multiple identities (race, culture, etc.)')

sns.catplot(x = 'training_participation', y = 'question16', palette = 'Blues', data = df, kind = 'bar', ci = None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Increased awareness of multiple identities (race, culture, etc.)')

# In[]
# Q19 Have you noticed an increase in your ability to be empathetic in your personal life 
# and at work since attending the trainings?

# Univariate graphs
sns.countplot(x = 'question19', data = df)
plt.xlabel('Increase in your ability to be empathetic')

sns.catplot(x = 'training_participation', y = 'question19', palette = 'Blues', data = df, kind = 'bar', ci = None)
plt.xlabel('Number of training sessions attended')
plt.ylabel('Increase in your ability to be empathetic')

# In[]
print("Which component(s) of Afternoon Meeting do you typically practice with youth (select all relevant responses):")

print("Respondent's implementation of 'Afternoon Meeting':")
df_sub0.sum()

print("Respondent's frequency of 'Afternoon Meeting' parctices:")
df_sub0.sum()/len(df_sub0)*100

# Let's rename the columns to make the plot cleaner 
df_sub0 = df_sub0.rename(columns={"Q20_1": "Greeting", "Q20_2": "Sharing", 'Q20_3' : 'Activity', 'Q20_4' : 'Message', 'Q20_5': 'None', 'Q20_6': 'NA'})



print('Which component(s) of Afternoon Meeting do you typically practice with youth (select all relevant responses)?')
#for_graph11.plot.bar()
df_sub0.sum().plot.bar()
plt.xlabel("Implementation of 'Afternoon Meeting'")
plt.ylim(0, 100) # control x and y limits
#sns.plt.xlim(0, None)

plot_data = df_sub0.sum()/len(df_sub0)*100
# Other graph
df_sub0perc = pd.DataFrame(data = plot_data)
# Let's rename the columns to make the plot cleaner 
df_sub0perc = df_sub0perc.rename(columns={"Q20_1": "Greeting", "Q20_2": "Sharing", 'Q20_3' : 'Activity', 'Q20_4' : 'Message', 'Q20_5': 'None', 'Q20_6': 'NA'})

df_sub0perc.plot.bar()
plt.xlabel("Implementation of 'Afternoon Meeting'")
plt.ylim(0, 100) # control x and y limits


# In[]
# Q21 How often are Afternoon Meetings conducted in your program?
# Create a sub dataset from the main data
df_sub2 = df[['Q21_1', 'Q21_2', 'Q21_3', 'Q21_4', 'Q21_5']]

df_sub2 = df_sub2.rename(columns = {'Q21_1' : 'Every day', 'Q21_2':'Several days', 'Q21_3': 'Once a week', 'Q21_4' : 'Every 2 to 3 weeks', 'Q21_5': 'Never'})

plot_data2 = df_sub2.sum()/len(df_sub2)*100
# Getting the sums and the frequencies
print("How often are Afternoon Meetings conducted in your program? (in a given week)")
df_sub2.sum().plot.bar()
plt.xlabel("Recurrence of 'Afternoon Meeting'")
# control x and y limits
plt.ylim(0, 100)

df_sub2perc = pd.DataFrame(data = plot_data2)

df_sub2perc.plot.bar()
plt.xlabel("Recurrence of 'Afternoon Meeting'")
plt.ylim(0, 100) # control x and y limits



# In[]
#  Question 23 (Q23a : Q23g) How often do you implement these SEL tools and practices throughout 
# your program with coworkers and/or youth?

print('How often do you implement these SEL tools and practices throughout your', end ='')
print(' program with co-workers and/or youth?')

# ---- Circle seating structure
# Univariate graph

sns.countplot(x = 'Q23_1', data = df, palette = 'Blues')
plt.xlabel("How often do you implement the 'Circle seating structure'")

# Bivariate graph
sns.catplot(x = 'training_participation',  y = 'Q23_1', data=df, kind="bar", ci=None, palette="Blues_d")
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implement 'Circle seating structure")

# ---- Group agreements
print(df['Q23_2'].value_counts(sort = False, dropna = False))

# Univariate graph
sns.countplot(x = 'Q23_2', data = df, palette = 'Blues')
plt.xlabel("How often do you implement the 'Group agreements'")

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'Q23_2', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implement 'Group agreements'")

# ---- Welcoming rituals
# Univariate graph
sns.countplot(x = 'Q23_3', data = df, palette = 'Blues')
plt.xlabel("How often do you implement 'Welcoming rituals'")

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'Q23_3', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implement 'Welcoming rituals'")

# ---- Transition pauses/activities
# Univariate graph
sns.countplot(x = 'Q23_4', data = df, palette = 'Blues')
plt.xlabel("How often do you implement 'Transition pauses/activities'")

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'Q23_4', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implement 'Transition pauses/activities'")



# ---- Attention cues
# Q23_5

# Univariate graph
sns.countplot(x = 'Q23_5', data = df, palette = 'Blues')
plt.xlabel("How often do you implement 'Attention cues'")

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'Q23_5', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implement 'Attention cues'")

pd.crosstab(df['training_participation'], df['Q23_5'])

# ---- Brain breaks
# Q23f

# Univariate graph
sns.countplot(x = 'Q23_6', data = df, palette = 'Blues')
plt.xlabel("How often do you implement 'Brain breaks'")

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'Q23_6', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implentation 'Brain breaks'")

# ---- Optimistic closure
# Q23_7

# Univariate graph
sns.countplot(x = 'Q23_7', data = df, palette = 'Blues')
plt.xlabel("How often do you implement 'Optimistic closure'")

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'Q23_7', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel("Implementation of 'Optimistic closure'")


#ax = sns.barplot(x = 'training_participation', y = 'Q23_7', data=df, estimator = lambda x: len(x) / len(df) * 100)
#ax.set(ylabel="Percent")

# In[]
# How often do you use strategies to take multiple perspectives and diverse needs of those around you
# into account (checking assumptions and misperceptions, open-ended questions and choices, looking
# from a different perspective, reflection, etc.)?

# Q25 	How often do you use strategies to take multiple perspect...
# 'question25'

# Univariate graph
sns.countplot(x = 'question25', data = df)
plt.xlabel('Use of strategies to take multiple perspectives')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question25', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of strategies to take multiple perspectives')


# In[]

# Q27 How often are you aware of and able to notice and name stressors and your reactions (sensations,
# thoughts, emotions, behavior)?

# Univariate graph
sns.countplot(x = 'question27', data = df)
plt.xlabel('Notice and name stressors')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question27', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Notice and name stressors')

# In[]
# How often do you guide youth to reflect on and regulate their emotions using positive and proactive
# approach to discipline (proximity, logical consequence, self-regulation space, restorative actions, etc.)?
# Q29 How often do you guide youth to reflect on and regulate t...

# Univariate graph
sns.countplot(x = 'question29', data = df)
plt.xlabel('guide youth to reflect/regulate emotions')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question29', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('guide youth to reflect/regulate emotions')

# In[]

# How often do you use practices to build self-care and resilience (journaling, mindfulness, exercise,
# mindful walking, healthy eating and nutrition, self-compassion exercises, spend time outdoors/nature,
# etc)

# Q30 	How often do you use practices to build self-care and res...

# Univariate graph
sns.countplot(x = 'question30', data = df)
plt.xlabel('Practices to build self-care and resilience')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question30', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Practices to build self-care and resilience')


# Frequency tables with frequencies :

pd.crosstab(df['training_participation'],df['Q30'])#, normalize = 'index')

# In[]

# Q32 	How much has your ability to be empathetic in your person...
# How much has your ability to be empathetic in your personal life and at work increased since
# attending the trainings?

# Univariate graph
sns.countplot(x = 'question32', data = df)
plt.xlabel('Ability to be empathetic')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question32', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Increased ability to be empathetic')


# In[]

# How much has your ability to be empathetic in your personal life and at work increased since
# attending the trainings?
# Q33 How frequently do you use Positive Language (reminding, r...

# Univariate graph
sns.countplot(x = 'question33', data = df)
plt.xlabel('Use of Positive Language')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question33', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of Positive Language')


# In[]

# How much has your ability to effectively build healthy and rewarding relationships in your personal life
# and at work increased since attending the trainings?

# Q34 How much has your ability to effectively build healthy an...

# Univariate graph
sns.countplot(x = 'question34', data = df)
plt.xlabel('Ability to build relationships')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question34', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Ability to build relationships')


# In[]
# How often have you been able to use any implicit bias awareness and de-biasing practices and tools
# (mindful inquiry, self-awareness exercises, multiple identities reflection, perspective checking,
# compassion practices, cultural exposure, etc.)?

# Q36 	How often have you been able to use any implicit bias awa...

# Univariate graph
sns.countplot(x = 'question36', data = df, palette = 'Blues_d')
plt.xlabel('Use of any implicit bias awareness and de-biasing practices')

# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question36', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of any implicit biais awareness practicies')



print(df['Q36'].value_counts(sort = False, dropna = False))
print(df['question36'].value_counts(sort = False, dropna = False))

pd.crosstab(df['training_participation'], df['question36'])
pd.crosstab(df['training_participation'], df['Q36'])

# In[]

# How often are you using SIT (signature practices, inquiry, thematic connection) to integrate SEL in
# regular program activities/cafeteria/playground, outside of Afternoon Meeting time?

# Q38 	How often are you using SIT (signature practices, inquiry...

print(df['question38'].value_counts(sort = False, dropna = False))

# Univariate graph
sns.countplot(x = 'question38', data = df)
plt.xlabel('Use of SIT (signature practices, inquiry, thematic connection)')


# Bivariate graph
sns.catplot(x = 'training_participation', y = 'question38', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Use of SIT (signature practices, inquiry, thematic connection)')

pd.crosstab(df['training_participation'], df['question38'])


# In[]

# How often are you implementing Second Step activities?
# Q40 How often are you implementing Second Step activities? 

# Univariate graph
sns.countplot(x = 'question40', data = df)
plt.xlabel('Implementing Second Step activities')

# Bivariate graphs
sns.catplot(x = 'training_participation', y = 'question40', data = df, kind = 'bar', ci = None, palette = 'Blues_d')
plt.xlabel('Number of training sessions attended')
plt.ylabel('Implementing Second Step activities')

pd.crosstab(df['training_participation'], df['question40'])











