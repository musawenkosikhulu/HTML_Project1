#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


def calculate(list):
  if len(list)<9:
   print("List must contain nine numbers.")
  else:
   a=np.reshape(list,(3,3))
  b=(np.mean(a,axis=0),np.mean(a,axis=1),np.mean(a))
  c=(np.var(a,axis=0),np.var(a,axis=1),np.var(a))
  d=(np.std(a,axis=0),np.std(a,axis=1),np.std(a))
  e=(np.max(a,axis=0),np.max(a,axis=1),np.max(a))
  f=(np.min(a,axis=0),np.min(a,axis=1),np.min(a))
  g=(np.sum(a,axis=0),np.sum(a,axis=1),np.sum(a))
  calculations={  'mean': [b],'variance': [c],'standard deviation': [d],'max': [e],'min': [f],'sum': [g] }
  return calculations
print(calculate([2,6,2,8,4,0,1,5,7]))


# In[39]:


def calculate(list): #This function takes a list arguement
    if len(list) < 9: #This cheecks if list have 9 nine numbers to generate a 3x3 matrix
        print('Error :try again this list can not create a 3x3 matrix') #if the length is less than 9 which cant a 3x3 this message say "try again"
    else: #This else statement will coontinue if the length is met
        output = np.reshape(list,(3,3))
        mean = [(np.mean(output,axis =0).tolist(),np.mean(output,axis =1).tolist(), np.mean(output))] #This calculates the mean for axis = 0, axis = 1 and overall
        Variance = (np.var(output,axis =0).tolist(), np.var(output,axis =1).tolist(), np.var(output)) #This calculates the variance for axis = 0, axis = 1 and overall
        standard_deviation = (np.std(output,axis =0).tolist(), np.std(output,axis =1).tolist(),np.std(output)) #This calculates a mean for axis = 0, axis = 1 and overall
        maximum = (np.max(output,axis =0).tolist(),np.max(output,axis =1).tolist(),np.max(output)) #This calculates the maximum for axis = 0, axis = 1 and overall
        minmum = (np.min(output,axis =0).tolist(),np.min(output,axis =1).tolist(),np.min(output)) #This calculates the minimum for axis = 0, axis = 1 and overall
        Total_Sum = (np.sum(output,axis =0).tolist(),np.sum(output,axis =1).tolist(),np.sum(output)) #This calculates the sum for axis = 0, axis = 1 and overall
        
        results = {'mean' : mean,'Variance' : Variance, 'maximum' : maximum,'minimum': minmum,'Sum': Total_Sum} # This creates put all the results in a tuple
    return results
calculate([1,2,3,4,5,6,7,8,9])       


# In[ ]:




