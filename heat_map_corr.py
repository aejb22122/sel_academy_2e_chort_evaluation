# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:52:51 2020

@author: ajeanbaptiste
"""

import pandas as pd
import numpy as np
import seaborn as sns  # for plots
import matplotlib.pyplot as plt  # for plots
sns.palplot(sns.color_palette("Blues"))
sns.set(style="darkgrid")


# Participation in SEL academy trainings
# Refer to the previsous scrip for this 

# ------------------ NO NOT RUN THIS LINE OF CODES! ---------------------------

df = pd.read_csv("sel_academy_series_feedback_survey_04_10_2020.csv", low_memory=False)

# -----------------------------------------------------------------------------


# df_corr = df[['training_participation', 'question10', 'question11', 'question12', 'question14', 'question16', 'question19', 'question30', 'question32', 'question34', 'question36']]

df_sub3 = df[['training_participation', 'question10', 'question11', 
              'question12', 'question14', 'question16', 'question19', 
              'question25', 'question27', 'question29','question30','question33', 'question34', 'question36', 
              'question38', 'question40']]


# Let's rename the columns to make the plot cleaner 
df_sub3 = df_sub3.rename(columns={"training_participation": "# sessions ",
                                  'question10':'Name SEL skills',
                                  'question11': 'Use SEL terms',
                                  'question12': 'Use self-awareness',
                                  'question14': 'Responsive Classroom',
                                  'question16': 'Awareness of mult-identities',
                                  'question19': 'Ability to be empathetic',
                                  'question25': 'Take mult. perspectives',
                                  'question27': 'Name stressors',
                                  'question29': 'Help youth regulate',
                                  'question30': 'Practice self-care',
                                  'question33': 'Use positive language',
                                  'question34': 'Build relationships',
                                  'question36': 'Implicit bias awareness',
                                  'question38': 'Use SIT',
                                  'question40': 'Second Step'})


df_sub3.head()
#sns.pairplot(df_sub3, hue = 'training_participation', height = 2.5)

# Compute correlations
corr = df_sub3.corr()

sns.set_style("white")
# Exclude duplicate correlations by masking uper right values
# print the mask and you will see a diagonal of 1s and 0s

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True


# Set up  matplotlib figure
#f, ax = plt.figure(figsize = (13,9))
f, ax = plt.subplots(figsize=(11, 9))

# Draw correlation plot
sns.heatmap(corr, annot = True, annot_kws={"size": 9},
            mask=mask, cmap = 'Blues',  #cmap=  , "YlGnBu", "coolwarm", "RdBu_r", "coolwarm"
        square=True,
        linewidths=.5, cbar_kws={"shrink": .5, 'label': 'Correlation'}, ax=ax) # 

# cbar_kws = {"shrink":.8,
#            'extend':'max',
#            'extendfrac':.2, 
#            "drawedges":True} 
# 
#heat_map = sb.heatmap(data, annot=True, cbar_kws={'label': 'My Colorbar'})

# -----------------------------------------------------------------------------
# Heat map simple straighfoward
sns.heatmap(df_sub3.corr(), annot = True, annot_kws={"size": 8}, 
            linewidth = 0.5, 
        square=True, cbar_kws={"shrink": .5},
        cmap = 'Blues') #  cmap = 'Blues' 

# Set background color / chart style
#sns.set_style(style = 'white')

# Set up  matplotlib figure
#f, ax = plt.subplots(figsize=(11, 9))

# Add diverging colormap
cmap = sns.diverging_palette(10, 250, as_cmap=True)

# Draw correlation plot
sns.heatmap(corr, mask=mask, cmap=cmap, 
        square=True,
        linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

