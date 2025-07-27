import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('D:\Full_Stack_AI\Work\week3\dataset_practice\datasets\RealEstate-USA.csv',delimiter=",")
#print(df)

xa=df.head(30)
g=sns.displot(data=xa, x="bed" , y="bath" , hue="acre_lot",  kind='hist'  )
g.figure.suptitle("sns.displot(data=xa, x=bed , y=bath , hue=acre_lot,  kind='hist'  )"  )

# Display the plot
g.figure.show()

wait=input("wait........")