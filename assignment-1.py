import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv("motorbikes.csv")
DataFrame=pd.DataFrame(data)
dfh=DataFrame.head(20)
dfh.plot(x="make_model",y="price",kind="bar",title="Bike Price",xlabel="Model", ylabel="Price")
plt.show()