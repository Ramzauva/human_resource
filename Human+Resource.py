
# coding: utf-8

# In[2]:

import pandas as px
import numpy as nm


# In[4]:

books = px.read_csv("C:\\Users\\Ramzauva\\Downloads\\Documents\\HR_comma_sep.csv")
# print(books.describe())
print(books.head())


# In[55]:

sales_second = px.Series(books['sales'])
satisfaction_rate = px.Series(books['satisfaction_level'])
working_hours_per_week = px.Series(books['average_montly_hours'])
salaries = px.Series(books['salary'])
low, medium, high = 0, 0, 0
mean_working_hours = 0
count_hours, count, totalsats, working_hours = 0, 0, 0, 0
salarie = [0, 0, 0]
# for x in range(0, 14999):
#     total_hours = total_hours + working_hours_per_week[x]/4
# print("Average Working Hours: ", (total_hours.sum()/14999))
count_low, count_medium, count_high = 0, 0, 0

for x in range(0, 14999):
    mean_working_hours = mean_working_hours + working_hours_per_week[x]/4
print("Average Working Hour per day: ", mean_working_hours/(5*14999))

for x in range(0, 14999):
    if(working_hours_per_week[x]/4 > (mean_working_hours/(5*14999))):
        
        # print("Working hours more than average: ", x)
        # count_hours = count_hours + 1
        if(salaries[x]=='low' and satisfaction_rate[x] <=.50):
            count_low = count_low + 1
            salarie[0] = count_low
            
        elif(salaries[x]=='medium' and satisfaction_rate[x] <=.50):
            count_medium = count_medium + 1
            salarie[1] = count_medium
            
        elif(salaries[x]=='high' and satisfaction_rate[x] <=.50):
            count_high = count_high + 1
            salarie[2] = count_high
            

    if(sales_second[x]=='accounting'):
        count = count+1
        # print('Record no:', x, ' on Accounting with Satisfaction: ', satisfaction_rate[x], " and working hours per week ", (working_hours_per_week[x]/4))
        totalsats = totalsats + satisfaction_rate[x]
        if (count==767):
            print('Mean Satisfaction out of 1: ', (totalsats/count))
            print('Number of Accountants', count)
            


percentage_low = (salarie[0]/7316)*100
percentage_medium = (salarie[1]/6446)*100
percentage_high = (salarie[2]/1237)*100
print(salaries.describe(), '\n')
print("LOW salary and satisfaction below .50 out of 1 are \t", salarie[0],"out of 7316. Percentage is: {1}", percentage_low)
print("MEDIUM salary and satisfaction below .50 out of 1 are\t ", salarie[1]," out of 6446. Percentage is: {1}", percentage_medium)
print("HIGH salary and satisfaction below .50 out of 1 are \t ",salarie[2] ,"out of 1237. Percentage is: {1}", percentage_high)

if(percentage_high < percentage_medium <percentage_low):
    print("The more the satisfaction, the more the salary or in other words the more the salary, the more the satisfaction")


# In[40]:

# example_dict = [0]

# for i in range(0, 10):
#     example_dict[0] = example_dict[0] + 1
    
# print(example_dict)
# print(books.promotion_last_5years.unique())
# print(salaries.describe())

count_lw, count_mid, count_hi = 0, 0, 0
contency = [0, 0, 0]
for x in range(0, 14999):
        # print("Working hours more than average: ", x)
        # count_hours = count_hours + 1
        if(salaries[x]=='low' and satisfaction_rate[x] >.50):
            count_lw = count_lw + 1
            contency[0] = count_lw
            
        elif(salaries[x]=='medium' and satisfaction_rate[x] > .50):
            count_mid = count_mid + 1
            contency[1] = count_mid
            
        elif(salaries[x]=='high' and satisfaction_rate[x] > .50):
            count_hi = count_hi + 1
            contency[2] = count_hi
            
print("People with 'LOW' salary and satisfaction above .50 out of 1 are \t", contency[0], 'in number.')
print("People with 'MEDIUM' salary and satisfaction above .50 out of 1 are\t ", contency[1], 'in number.')
print("People with 'HIGH' salary and satisfaction above .50 out of 1 are \t", contency[2], 'in number.')


# In[42]:

count_lw_1, count_mid_1, count_hi_1 = 0, 0, 0
contency_tt = [0, 0, 0]
for x in range(0, 14999):
        if(salaries[x]=='low'):
            count_lw_1 = count_lw_1 + 1
            contency_tt[0] = count_lw_1
            
        elif(salaries[x]=='medium'):
            count_mid_1 = count_mid_1 + 1
            contency_tt[1] = count_mid_1
            
        elif(salaries[x]=='high'):
            count_hi_1 = count_hi_1 + 1
            contency_tt[2] = count_hi_1
            
print(contency_tt)

