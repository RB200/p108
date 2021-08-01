import plotly.figure_factory as ff
import pandas as pd
import statistics
df=pd.read_csv('data.csv')
data=df['Avg Rating']
mean=statistics.mean(data)
print(mean)

# Plotting graph

fig=ff.create_distplot([data],['Avg rating'],show_hist=False)
fig.show()