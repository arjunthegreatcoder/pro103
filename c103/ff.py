import pandas as pd
import plotly.express as px
ct = pd.read_csv("line_chart.csv")
fig = px.scatter(ct,x = "date",y = "cases",title = "covidcase", color = "country")
fig.show()