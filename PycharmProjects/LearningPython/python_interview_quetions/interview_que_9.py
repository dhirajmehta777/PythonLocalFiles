#Que9
"""
Q:What is pandas series?
"""
"""
Ans:
1. Series is one dimensional pandas data structure that supports data of almost any type.
2. It supports multiple operations and is used for single dimensional data operations.
"""
import pandas as pd
data=["1", 2, "three", 4.0]
series=pd.Series(data)
print(series)
print(type(series))



