#Que10
"""
Q:What is the use of pandas groupby() function?
"""
"""
Ans:
1. Groupby is a feature supported by pandas which is used to split and group an object
2. Like the SQL, MYSQL and Oracle groupby, it is used to group data by classes and entities which can be 
fruther used for aggregations.

"""
import pandas as pd
df=pd.DataFrame({'Vehicle':['Kia','Lamborghini','KTM RC390','Pulsar 200NS'],'Type':["car","car","motorcycle","motorcycle"]})
print(df)
print(df.groupby("Type").count())


