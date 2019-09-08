import numpy as np
import random
import pandas as pd
import string
from pandas import DataFrame

marks_randomnums=np.random.randint(100,300,200)
marks=list(marks_randomnums)
#print(marks)
weight_randomnums=np.random.randint(40,60,200)
weight=list(weight_randomnums)
#print(age)

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    gender_list=["male","female"]
    return (random.choice(gender_list))
for i in range(1,201):
        gender=randomString()
        #print(gender)
name=[randomString() for i in range(1,201)]
c=name
students={'marks':[mark for mark in marks],'gender':[gender for gender in c],'weight':[wgt for wgt in weight]}
df = pd.DataFrame(students,columns=['marks','gender','weight'])

#print(df)

df = DataFrame(students,columns=['marks','gender'])

#filter=students['gender']=="male"
df.loc[(df.marks > 200) & (df.gender=="male"), 'Group'] = 'A'
df.loc[(df.marks > 200) & (df.gender=="female"), 'Group'] = 'B'
df.loc[(df.marks <= 200) & (df.gender=="male"), 'Group'] = 'C'
df.loc[(df.marks <= 200) & (df.gender=="female"), 'Group'] = 'D'

#print (df)

df = DataFrame(students,columns=['marks','gender','Group','weight'])
df.loc[(df.Group=='A')|(df.weight>50),'sub_group']='High Risk'
df.loc[(df.Group=='B')|(df.weight>50),'sub_group']='Medium Risk'
df.loc[((df.Group=='C')& (df.Group=='D'))|(df.weight<50),'sub_group']='low Risk'

print(df)
