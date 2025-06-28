#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Loading the Student Performance Dataset 

# In[3]:



# Load Data
df = pd.read_csv('StudentsPerformance.csv')

# View first few rows

df.head()


# 1. Data Cleaning

# In[4]:


# Check for nulls
print(df.isnull().sum())

# Rename columns (optional)
df.columns = df.columns.str.replace(" ", "_").str.lower()


# 2. Basic Descriptive Stats

# In[5]:



df.describe() 


# In[6]:


df['gender'].value_counts()


# In[7]:


df['parental_level_of_education'].value_counts()


#  3. Visualizations

# In[8]:


# a. Distribution of Scores
plt.figure(figsize=(10,6))
sns.histplot(df['math_score'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Math Scores')
plt.show()


# In[9]:


# b. Average Scores by Gender
df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean().plot(kind='bar')
plt.title('Average Scores by Gender')
plt.ylabel('Score')
plt.xticks(rotation=0)
plt.show()


# In[10]:


# Boxplot: Test Preparation vs Scores 
plt.figure(figsize=(10,6))
sns.boxplot(x='test_preparation_course', y='math_score', data=df)
plt.title('Math Score vs Test Prep')
plt.show()


# 4. Correlation Heatmap

# In[11]:



plt.figure(figsize=(8,6))
sns.heatmap(df[['math_score','reading_score','writing_score']].corr(), annot=True, cmap='coolwarm')
plt.title('Score Correlation Heatmap')
plt.show()


# In[ ]:




