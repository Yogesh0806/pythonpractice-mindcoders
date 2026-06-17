import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats

saleries = [22,28,35,55,48,60,72,85,30,45,52,65,28,34,41,58,75,90]

# mean = np.mean(saleries)
# median = np.median(saleries)
# mode = stats.mode(saleries, keepdims=True).mode[0]

# print(f'Mean (Average): Rs. {mean : .1f}K')
# print(f'Median (middle value): Rs. {median}K')
# print(f'Mode (most common): Rs. {mode}K') 


#Spread - how varied is the data ?

std = np.std(saleries)
var = np.var(saleries)
rng = max(saleries)- min(saleries)
q1 = np.percentile(saleries,25)
q3 = np.percentile(saleries,75)
iqr = q3 - q1
print(f'std Deviation: {std : .2f}K (Most important spread measure)')
print(f'IQR:{iqr}K (Q1={q1}, Q3={q3})')

#Outlier detection using iqr (Interquartile Range)
lower = q1 - 1.5*iqr
upper = q1 + 1.5*iqr
outliers = [x for x in saleries if x <lower or x> upper]
print(f'Outliers : {outliers}')