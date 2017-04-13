
# coding: utf-8

# In[1]:

import pandas as px
import numpy as nm


# In[5]:

px.DataFrame({
    'First':[1., 2., 3., nm.nan, 5., 6., 7., 8., 9., 10.]},
    index = px.date_range('20150101 09:00:00', periods=10, freq='s')
    )


# In[2]:

first = px.read_csv("C:\\Users\\Ramzauva\\Downloads\\Documents\\database_2.csv")


# In[3]:

second = px.Series(first["Latitude"])
third = px.Series(first["Longitude"])
fourth = px.Series(first["Magnitude"])
fifth = px.Series(first["Date"])

for x in range(0, 23412):
    if(76.845245 < second[x] < 97.40238 and 6.74678 < third[x] < 35.674520):
        print("Record no:",x, '\tLongitude: ', third[x], '\t Latitude: ', second[x], 'Date,Time:',first['Date'][x], first['Time'][x], 'of Magnitude:', first['Magnitude'][x])
#         for i in range(0, 4):
#                 earth_quake_India = px.DataFrame([second[x],third[x],fifth[x],fourth[x] ], index=['Latitude', 'Longitude', 'Date', 'Magnitude'])
#                 new_earth_India[0:i] = px.Series(earth_quake_India)
# print(new_earth_India)


# In[84]:

secondary.mean()

