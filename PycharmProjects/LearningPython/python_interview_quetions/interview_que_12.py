#Que12
"""
Q:How to create dataframe from dictionary?
"""
"""
Ans:
To Create dataframe from dictionary, this is what required:
-A dictionary can be directly passed as an argument to dataframe() function to create the dataframe.
"""
import pandas as pd
df=pd.DataFrame()
bikes=["Bajaj","TVS","Honda","Kawasaki","BMW"]
cars=["Lambhorgini","Masserati","Ferrari","Hyundai","Ford"]
d={"cars":cars,"bikes":bikes}
df=pd.DataFrame(d)

print(df)
