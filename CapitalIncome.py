import pandas as pd
import plotly.express as px
df=pd.read_csv("CapitalIncome.csv")
graph=px.scatter(df,x="date", y="cases", color="Country") 
graph.show()
print(df)