#Que11
"""
Q:How to create dataframe from lists?
"""
"""
Ans:
To Create dataframe from lists, this is what required:
-An empty dataframe
-Addition of lists as individual columns in the dataframe
"""
import pandas as pd
df=pd.DataFrame()
bikes=["Bajaj","TVS","Honda","Kawasaki","BMW"]
cars=["Lambhorgini","Masserati","Ferrari","Hyundai","Ford"]
df["cars"]=cars
df["bikes"]=bikes
print(df)
