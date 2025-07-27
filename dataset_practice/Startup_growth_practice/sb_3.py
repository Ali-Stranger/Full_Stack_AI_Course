import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('D:\Full_Stack_AI\Work\week3\dataset_practice\datasets\Startups in 2021 end.csv',delimiter=",")
#print(df)

xa=df.head(7)
g=sns.displot(data=xa, x="Company" , y="Valuation" , hue="Industry",  kind='hist'  )
g.figure.suptitle("sns.displot(data=xa, x=Company , y=Valuation , hue=Industry,  kind='hist'  )"  )

# Display the plot
g.figure.show()

wait=input("wait........")