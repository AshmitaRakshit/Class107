import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
print(df.groupby("level")["attempt"].mean())

#output
#Level 1    0.751445
#Level 2    0.863281
#Level 3    0.698113
#Level 4    0.734694
#Name: attempt, dtype: float64

#fig=go.Figure(go.Bar(
    #x=df.groupby("level")["attempt"].mean(),
    #y=['Level 1','Level 2','Level 3','Level 4'],
    #orientation='h'
#))
fig=go.Figure(go.Bar(
    y=df.groupby("level")["attempt"].mean(),
    x=['Level 1','Level 2','Level 3','Level 4'],
    orientation='v'
))
fig.show()