# -*- coding: utf-8 -*-
"""LVADUSR160_Final Assessment_Anomaly.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WO4OQxv76pJHqJUE0WdvnhcWp2YCMRN8
"""

import pandas as pd

df_m=pd.read_csv('/content/anomaly_train.csv')

df = df_m.iloc[:225,:]
df_test = df_m.iloc[225:,:]
df.info()

df.describe()

df.isnull().sum()

duplicates = df.duplicated(keep=False)
df['dup_bool'] = duplicates
print(df[df['dup_bool'] == True].count())
df.drop('dup_bool',axis=1,inplace=True)
df.head(1)

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(df['Type'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(df, x='Location', y='Type', inner='stick', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

from sklearn.ensemble import IsolationForest
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

features = ["Amount", "Time", "User"]

X = df[features]

model = IsolationForest()

model.fit(X)

y_pred = model.predict(X)
df["anomaly_score"] = model.decision_function(X)

anomalies = df.loc[df["anomaly_score"] < 0]

x=df_test[["Amount", "Time", "User"]]
df_values=x.values

find=df_values

result=[]
for i in find:
  z=model.predict([i])
  if z==[1]:
    result.append('Not Anomaly')
  elif z==[-1]:
    result.append('Anomaly')

df_test['Anomaly']=result
print(df_test)

plt.scatter(df["Location"], df["Amount"], label="Not Anomaly")
plt.scatter(anomalies["Location"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Location")
plt.ylabel("Amount")
plt.legend()
plt.show()

df_test.head()