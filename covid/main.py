import pandas as pd
import plotly.express as px

df1 = pd.read_csv("covid.csv")
figure1 = px.scatter(df1,x="cases",y="countrey",title="cases of covid ")
figure1.show()