#!/usr/bin/env python
# coding: utf-8

# # Project Final Submission Template

# ### Step 1a: Planning 
# #### Identify the information in the file your program will read
# 
# 
# The file contains information about California crime by campus. It shows the 
# university/college name, campus, student enrollment, violent crime, murder and nonnegligent manslaughter, rape (revised definition), robbery, aggravated assault, property crime, burglary, larceny-theft, motor vehicle theft, and arson.

# ### Step 1b: Planning 
# #### Write a description of what your program will produce
# 
# 1. Which school has the most crimes, and what is the number of cases in each crime. Show with a pie chart.
# 
# 2. Calculate the ratio of 3 different kinds of violent crimes(Violent crime,murder,rape) 
#     that may happen to per student (in per mil) versus the ratio of 5 different kinds of crimes
#     (Robbery,Property crime,Burglary,Larceny-theft,Motor vehicle theft) 
#     that may happen to per student (in per mil) in 10 different schools, then turn it into a scatter plot.
# 
# 3. Show whether crime cases are related to the number of student enrollment. Show by using a line chart, x-axis: number of student enrollment, y-axis: crime commited (Choose the top 5 crime cases commited and the least 5 commited (in total of 10 cases))
# 
# I chose to do number 2.
# 
# 
# You must brainstorm at least three ideas for graphs or charts that your program could produce and choose the one that you'd like to work on. You can choose between a line chart, histogram, bar chart, scatterplot, or pie chart.

# ### Step 1c: Planning 
# #### Write or draw examples of what your program will produce
# 
# Double click this cell to edit. !
# ![0.jpg](attachment:0.jpg)
# You must include an image that shows what your chart or plot will look like. You can insert an image using the Insert Image command near the bottom of the Edit menu.

# ### Step 2a: Building
# #### Design data definitions
# 
# Double click this cell to edit.
# 
# Before you design data definitions in the code cell below, you must explicitly document here which information in the file you chose to represent and why that information is crucial to the chart or graph that you'll produce when you complete step 2c.

# In[82]:


from cs103 import *
from typing import NamedTuple, List
from enum import Enum
import csv

##################
# Data Definitions
CaliCrime = NamedTuple('CaliCrime',[('student_enrollment', int),
                                   ('violent', int),
                                   ('murder', int),
                                   ('rape',int),
                                   ('robbery', int), 
                                   ('property_crime', int),
                                   ('burglary', int), 
                                   ('larceny_theft',int), 
                                   ('motor_vehicle_theft',int)])

# interp. the California crime containing information of 
#violent crime, murder,rape, student enrollment, 
#robbery, property crime, burglary, larceny-theft,and motor vehicle theft.

CC1 = CaliCrime(11047,0, 0, 0, 0, 21, 2, 18, 1)
CC2 = CaliCrime(23966, 3,0,2, 1, 173, 5, 150, 18)
CC3 = CaliCrime(36809,6,0,4,1,148,12,129,7)
CC4 = CaliCrime(32713,29,0,2,5, 442,30,397,15)
CC5 = CaliCrime(24488,14,0,2,0,147,23,119,5)
#template based on compound and reference rule
@typecheck
def fn_for_cali_crime(cc:CaliCrime) -> ...:
    return ...(cc.student_enrollment,cc.violent, cc.murder,cc.rape, cc.robbery,
               cc.property_crime, cc.burglary, cc.larceny_theft, cc.motor_vehicle_theft)

# List[CaliCrime]
# interp. a list of California crime

LOCC0 = []
LOCC1 = [CC1, CC2,CC3, CC4,CC5]

@typecheck
def fn_for_locc(locc: List[CaliCrime]) -> ...: # template based on arbitrary-sized data and reference rule
    #description of accumulator
    acc = ... #type: ...
    
    for cc in locc:
        acc = ...(acc, fn_for_cali_crime(cc))
    return ... (acc)


# ### Step 2b and 2c: Building
# #### Design a function to read the information and store it as data in your program
# #### Design functions to analyze the data
# 
# 
# Complete these steps in the code cell below. You will likely want to rename the analyze function so that the function name describes what your analysis function does.

# In[89]:


###########
# Functions
import matplotlib.pyplot as pyplot
@typecheck
def main(filename: str) -> None:
    """
    Reads the file from given filename and plots a graph showing how 
    the ratio of 3 different kinds of violent crimes(Violent crime,murder,rape) 
    that may happen to per student versus the ratio of 5 different kinds of crimes
    (Robbery,Property crime,Burglary,Larceny-theft,Motor vehicle theft) 
    that may happen to per student in 10 different schools, return None
    """
    # Template from HtDAP, based on function composition 
    return plot_data(read(filename)) 

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
        
            
            cc = CaliCrime(parse_int(row[2]),parse_int(row[3]),parse_int(row[4]),
                           parse_int(row[5]), parse_int(row[6]), parse_int(row[8]), 
                           parse_int(row[9]), parse_int(row[10]), parse_int(row[11]))
            
            locc.append(cc)
    
        return locc
@typecheck
def plot_data(locc: List[CaliCrime]) -> None: 
    """ 
    Plots the ratio of 3 different kinds of violent crimes(Violent crime,murder,rape) 
    that may happen to per student versus the ratio of 5 different kinds of crimes
    (Robbery,Property crime,Burglary,Larceny-theft,Motor vehicle theft) 
    that may happen to per student in 10 different schools, return None
    """ 
    #return None #stub
    #template based on visualization
    
    pyplot.xlabel('Violent Crime / per person (‰)')
    pyplot.ylabel('Property Crimes/per person(‰)')
    pyplot.title('Violent vs Property Crime')
    pyplot.axis([0, 21, 0, 280])
    
    x_vals = get_ratio_violent(locc)
    y_vals = get_ratio_property(locc)
    
    pyplot.scatter(x_vals, y_vals,marker='o', c='r', s=30)

    pyplot.show()

    return None

@typecheck
def get_ratio_violent(locc:List[CaliCrime]) -> List[float]:
    """
    Produce a list of the ratio of 3 different kinds of violent crimes(Violent crime,murder,rape) 
    that may happen to per student. 
    """
    #return [] #stub
    #template copied from List[CaliCrime]
    #acc is the list of ratio seen so far
    acc = [] #type:[float]
    for cc in locc:
        acc.append(calculate_ratio_violent(cc))
    return acc
@typecheck
def calculate_ratio_violent(cc:CaliCrime) -> float:
    """
    Calculate the ratio of the ratio of 3 different kinds of violent crimes(Violent crime,murder,rape) 
    that may happen to per student in each school
    """
    #return 0.0 #stub
    #template copied from CaliCrime
    return round(((cc.violent + cc.murder + cc.rape)*1000 / (cc.student_enrollment)), 2)
@typecheck
def get_ratio_property(locc:List[CaliCrime]) -> List[float]:
    """
    Produce a list of the ratio of 5 different kinds of crimes(Robbery,
    Property crime,Burglary,Larceny-theft,Motor vehicle theft)
    that may happen to per student in each school. 
    """
    #return [] #stub
    #template copied from List[CaliCrime]
    #ratio is the list of ratio seen so far
    ratio = [] #type:[float]
    for cc in locc:
        ratio.append(calculate_ratio_property(cc))
    return ratio

@typecheck
def calculate_ratio_property(cc:CaliCrime) -> float:
    """
    Calculate the ratio of 5 different kinds of crimes(Robbery,
    Property crime,Burglary,Larceny-theft,Motor vehicle theft)
    that may happen to per student in each school
    """
    #return 0.0 #stub
    #template copied from CaliCrime
    return round((cc.robbery + cc.property_crime + cc.burglary + 
            cc.larceny_theft + cc.motor_vehicle_theft)*1000 / (cc.student_enrollment))
start_testing()
expect(main('california_crime_by_campus_empty.csv'),None)
expect(main('california_crime_by_campus_test1.csv'),None)
expect(main('california_crime_by_campus_test2.csv'),None)
#expect(main('california_crime_by_campus.csv'),None)
summary()

start_testing()
# Examples and tests for read
expect(read('california_crime_by_campus_empty.csv'), [])
expect(read('california_crime_by_campus_test1.csv'), [CaliCrime(11047, 0, 0, 0, 0, 21, 2, 18, 1), 
                                                      CaliCrime(23966, 6, 0, 4, 1, 173, 5, 150, 18),
                                                      CaliCrime(20186, 3, 0, 2, 0, 163, 7, 149, 7),
                                                      CaliCrime(18205, 1, 0, 0, 0, 46, 4, 40, 2),
                                                      CaliCrime(23144, 5, 0, 2, 0, 86, 10, 72, 4), 
                                                      CaliCrime(8720, 1, 0, 0, 0, 78, 12, 65, 1), 
                                                      CaliCrime(5879, 2, 0, 0, 1, 62, 7, 54, 1),
                                                      CaliCrime(17287, 7, 0, 3, 1, 254, 13, 235, 6),
                                                      CaliCrime(14687, 4, 0, 0, 0, 72, 5, 65, 2),
                                                      CaliCrime(14823, 2, 0, 2, 0, 97, 11, 80, 6)])
expect(read('california_crime_by_campus_test2.csv'), [CaliCrime(6268, 11, 0, 3, 0, 23, 2, 19, 2), 
                                                      CaliCrime(21498, 10, 0, 3, 6, 291, 28, 250, 13), 
                                                      CaliCrime(30709, 7, 0, 1, 1, 511, 28, 461, 22),
                                                      CaliCrime(3170, 15, 0, 1, 4, 437, 34, 387, 16), 
                                                      CaliCrime(23051, 28, 0, 15, 2, 203, 17, 186, 0),
                                                      CaliCrime(37565, 35, 0, 9, 12, 749, 43, 688, 18),
                                                      CaliCrime(34508, 22, 0, 13, 4, 600, 27, 568, 5),
                                                      CaliCrime(1003, 19, 0, 1, 4, 40, 4, 36, 0), 
                                                      CaliCrime(30051, 22, 0, 9, 4, 467, 45, 405, 17),
                                                      CaliCrime(41845, 97, 0, 27, 22, 817, 136, 663, 18)])
# show testing summary
summary()

start_testing()

# Examples and tests for main
expect(plot_data([]), None)
expect(plot_data(LOCC1),None)


summary()

start_testing()

# Examples and tests for main
expect(get_ratio_violent([CC1,CC2]), [0, 0.21])
expect(get_ratio_violent([CC3,CC4,CC5]), [0.27, 0.95, 0.65])
expect(get_ratio_violent([]), [])
summary()

start_testing()

# Examples and tests for read
expect(get_ratio_property([CC1,CC2]), [4, 14])
expect(get_ratio_property([CC3,CC4,CC5]), [8, 27, 12])
expect(get_ratio_property([]), [])

summary()

start_testing()

# Examples and tests for analyze 
expect(calculate_ratio_violent(CC1), 0)
expect(calculate_ratio_violent(CC2), 0.21)
expect(calculate_ratio_violent(CC3), 0.27)
summary()

start_testing()

# Examples and tests for analyze 
expect(calculate_ratio_property(CC1), 4)
expect(calculate_ratio_property(CC2), 14)
expect(calculate_ratio_property(CC3), 8)
summary()

    


# In[84]:


main('california_crime_by_campus_test0.csv')

