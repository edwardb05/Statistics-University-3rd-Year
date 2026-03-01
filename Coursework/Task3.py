import pandas as pd
from numpy import random

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats
from statsmodels.graphics.gofplots import qqplot
#Set random seed without leading 0 in CID
random.seed(2399744)

df_concentration =pd.read_csv("eb1723_PM10.csv")
df_weather =pd.read_csv("eb1723_weather.csv")

#Change the date format of weather data for easier merging with concentration data
df_weather["Date"] = pd.to_datetime(df_weather[["Year", "Month", "Day"]])

# Change concentration date to datetime format for easier merging with weather data
df_concentration["Date"] = pd.to_datetime(df_concentration["Date"], dayfirst=True)

#Merge the two dataframes using inner to drop any rows with missing data in either dataframe
df_merged = df_weather.merge(df_concentration, on="Date", how="inner")

#Drop any rows with missing data in either dataframe (represented by "-")
df_merged = df_merged[df_merged.ne("-").all(axis=1)]

#Drop the Year, Month and Day columns as they are no longer needed after merging
df_merged = df_merged.drop(columns=["Year", "Month", "Day"])

#Change the data type of PM10 column to numeric for easier analysis and plotting
df_merged["PM10"] = pd.to_numeric(df_merged["PM10"], errors="coerce")

#Part b plotting histogram
columns = ["Wind", "Temperature", "Humidity", "Cloud", "PM10"]

plt.figure(figsize=(14, 8))

for i, column in enumerate(columns, 1):
    data = df_merged[column].dropna()
    mean = data.mean()
    median = data.median()
    std = data.std()
    data_range = data.max() - data.min()
    
    plt.subplot(2, 3, i)
    plt.hist(data, bins=20)
    
    plt.title(column)
    

    text = (
        f"Mean: {mean:.2f}\n"
        f"Median: {median:.2f}\n"
        f"Std: {std:.2f}\n"
        f"Range: {data_range:.2f}"
    )
    plt.text(data.max(), max(plt.ylim()), text,
         ha='right', va='top')
    


plt.tight_layout()
plt.show()

#Part 2 linear regression of PM10 against the other weather variables

columns = ["Wind", "Temperature", "Humidity", "Cloud"]

plt.figure(figsize=(14, 8))

for i, column in enumerate(columns, 1):
    
    X = df_merged[[column]]     
    y = df_merged["PM10"]        

    model = LinearRegression()
    model.fit(X, y)

 
    print(f"R² value of {column} is {model.score(X,y):.2f}")
 
    

  

#Plot the wind scatter plot with regression line
plt.subplot(1, 1, 1)
X = df_merged[["Wind"]]
y = df_merged["PM10"]
model = LinearRegression()
model.fit(X, y)

text = (
    f"$R^2$: {model.score(X,y):.2f}"
)
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Wind")
plt.ylabel("PM10")
plt.text(X["Wind"].max(), max(plt.ylim())-1, text,
        ha='right', va='top')
plt.title(f'linear regression with PM10 against Wind')
plt.tight_layout(pad=2.0)
plt.show()
    

#Part C - Calculate residuals for best model (Wind)
y_hat = model.predict(X)
residuals = y - y_hat


qqplot(residuals, dist=stats.norm, fit=True, line='45')

plt.title("QQ Plot of Residuals")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()