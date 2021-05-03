#!/usr/bin/env python
# coding: utf-8

# # Project Milestone Template

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# The file contains information about California crime by campus. It shows the 
# university/college name, campus, student enrollment, violent crime, murder and nonnegligent manslaughter, rape (revised definition), robbery, aggravated assault, property crime, burglary, larceny-theft, motor vehicle theft, and arson.

# ### Step 1b: Planning 
# #### Write a description of what your program will produce
# 
# 1. Which school has the most crimes, and what is the number of cases in each crime. Show with a pie chart.
# 
# 2. Calculate the ratio of 5 different  kinds of crimes(Robbery,Property crime,Burglary,Larceny-theft,Motor vehicle theft) that may happen to per student in each school(The sum of  different crimes/ student enrollments). Pick the top five school and campus(if there is one), then turn it into a bar chart
# 
# 3. Show whether crime cases are related to the number of student enrollment. Show by using a line chart, x-axis: number of student enrollment, y-axis: crime commited (Choose the top 5 crime cases commited and the least 5 commited (in total of 10 cases))
# 
# I chose to do number 2.
# 
# You must brainstorm at least three ideas for graphs or charts that your program could produce and choose the one that you'd like to work on. You can choose between a line chart, histogram, bar chart, scatterplot, or pie chart.

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# Double click this cell to edit. ![75603840_2755552404506724_1652107819500961792_n.jpg](attachment:75603840_2755552404506724_1652107819500961792_n.jpg)
# 
# You must include an image that shows what your chart or plot will look like. You can insert an image using the Insert Image command near the end of the Edit menu.

# ### Step 2a: Building
# #### Design data definitions
# 
# First, I need to design the compound data definition. Then, I can use it to design the list data definition. I would need every data in the csv file.
# 
# Before you design data definitions in the code cell below, you must explicitly document here which information in the file you chose to represent and why that information is crucial to the chart or graph that you'll produce when you complete step 2c.

# In[13]:


from cs103 import *
from typing import NamedTuple, List
import csv

##################
# Data Definitions

CaliCrime = NamedTuple('CaliCrime',[('university_college',str), 
                                    ('campus', str),
                                    ('student_enrollment', int), 
                                    ('robbery', int), 
                                    ('property_crime', int),
                                    ('burglary', int), 
                                    ('larceny_theft',int), 
                                    ('motor_vehicle_theft',int)])

# interp. the California crime containing information of 
#university/college name, campus(might not have one, return an empty str), student enrollment, 
#robbery, property crime, burglary, larceny-theft,and motor vehicle theft.

CC1 = CaliCrime('Allan Hancock College','', 11047, 0, 21, 2, 18, 1)
CC2 = CaliCrime('California State Polytechnic University', 'Pomona', 23966, 1, 173, 5, 150, 18)

#template based on compound and reference rule
@typecheck
def fn_for_cali_crime(cc:CaliCrime) -> ...:
    return ...(cc.university_college, cc.campus, cc.student_enrollment,cc.robbery,
               cc.property_crime, cc.burglary, cc.larceny_theft, cc.motor_vehicle_theft)

# List[CaliCrime]
# interp. a list of California crime

LOCC0 = []
LOCC1 = [CC1, CC2]

@typecheck
def fn_for_locc(locc: List[CaliCrime]) -> ...: # template based on arbitrary-sized data and reference rule
    #description of accumulator
    acc = ... #type: ...
    
    for cc in locc:
        acc = ...(acc, fn_for_cali_crime(cc))
    return ... (acc)


# ### Step 2b: Building
# #### Design a function to read the information and store it as data in your program
# 
# Complete this step in the code cell below. 

# In[11]:



###########
# Functions

@typecheck
def read(filename: str) -> List[CaliCrime]:
    """    
    reads information from the specified file and returns a list of california crime data
    """
    #return []  #stub
    # Template from HtDAP
    # locc contains the result so far
    locc = [] # type: List[CaliCrime]

    with open(filename) as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader) # skip header line

        for row in reader:
            
            # you may not need to store all the rows, and you may need
            # to convert some of the strings to other types
            
            cc = CaliCrime(row[0],row[1], parse_int(row[2]), parse_int(row[6]), parse_int(row[8]), 
                           parse_int(row[9]), parse_int(row[10]), parse_int(row[11]))
            if len(row[2]) == 0:
                
                return ""
        
            locc.append(cc)
    
    return locc


# Begin testing
start_testing()

# Examples and tests for read
expect(read('california_crime_by_campus_test1.csv'), [CaliCrime('Allan Hancock College','', 11047, 0, 21, 2, 18, 1), 
                                                    CaliCrime('California State Polytechnic University','Pomona',23966, 1, 173, 5, 150, 18),
                                                    CaliCrime('California State Polytechnic University','San Luis Obispo4', 20186, 0, 163, 7, 149, 7)])
expect(read('california_crime_by_campus_test2.csv'), [CaliCrime('California State University','San Marcos', 12154, 0, 59, 2, 57, 0),
                                                     CaliCrime('California State University','Stanislaus', 9045, 0, 72, 1, 70, 1),
                                                     CaliCrime('California State University','Sacramento', 29349, 5, 195, 7, 186, 2)])
# show testing summary
summary()


# In[18]:



###########
# Functions

@typecheck
def read(filename: str) -> List[CaliCrime]:
   """    
   reads information from the specified file and returns a list of california crime data
   """
   #return []  #stub
   # Template from HtDAP
   # locc contains the result so far
   locc = [] # type: List[CaliCrime]

   with open(filename) as csvfile:
       
       reader = csv.reader(csvfile)
       next(reader) # skip header line

       for row in reader:
           
           # you may not need to store all the rows, and you may need
           # to convert some of the strings to other types
       
           
           cc = CaliCrime(row[0],row[1], parse_int(row[2]), parse_int(row[6]), parse_int(row[8]), 
                          parse_int(row[9]), parse_int(row[10]), parse_int(row[11]))
           
           if len(row[2])!= 0:
               locc.append(cc)
   
       return locc
start_testing()

# Examples and tests for read
expect(read('california_crime_by_campus_test1.csv'), [CaliCrime('Allan Hancock College','', 11047, 0, 21, 2, 18, 1), 
                                                   CaliCrime('California State Polytechnic University','Pomona',23966, 1, 173, 5, 150, 18),
                                                   CaliCrime('California State Polytechnic University','San Luis Obispo4', 20186, 0, 163, 7, 149, 7)])
expect(read('california_crime_by_campus_test2.csv'), [CaliCrime('California State University','San Marcos', 12154, 0, 59, 2, 57, 0),
                                                    CaliCrime('California State University','Stanislaus', 9045, 0, 72, 1, 70, 1),
                                                    CaliCrime('California State University','Sacramento', 29349, 5, 195, 7, 186, 2)])
# show testing summary
summary()


# In[23]:


from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]


def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x * 1e-6)


formatter = FuncFormatter(millions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
plt.bar(x, money)
plt.xticks( x,('Bill', 'Fred', 'Mary', 'Sue') )
plt.show()


# In[ ]:




