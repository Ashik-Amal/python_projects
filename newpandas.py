import pandas as pd
#version
print(pd.__version__)

#index and series
s= pd.Series([10,20,30],index =["a","b","c"])
print(s)

#dataframe
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NY", "LA", "SF"]
}

df = pd.DataFrame(data)
print(df)

#series
data2 =[1,3,4,5,7]
vr = pd.Series(data2)
print(vr)
print(vr.loc[3])

