import pandas as pd
import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.line(df,x="date",y="cases",color='country',title='Covid 19 Cases In Countries')
fig.show()
