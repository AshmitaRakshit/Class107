import pandas as pd
import csv
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
student_df=df.loc[df['student_id']=="TRL_imb"]
print(student_df.groupby("level")["attempt"].mean())

#output
#Level 1    1.0000
#Level 2    1.0000
#Level 3    0.9375
#Level 4    0.9375
#Name: attempt, dtype: float64
#The student perfirmed best in level 1 and level 2
fig=go.Figure(go.Bar(
    y=student_df.groupby("level")["attempt"].mean(),
    x=['Level 1','Level 2','Level 3','Level 4'],
    orientation='v'
))
fig.show()
