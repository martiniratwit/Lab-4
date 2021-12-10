#!/usr/bin/env python
# coding: utf-8

# In[134]:


import pandas as pd

data = pd.read_csv("pong_data.csv")
data


# In[135]:


X=data.drop("paddle_y", axis=1)
y = data.iloc[:,5]

print(X.head())


# In[136]:


from sklearn import linear_model
model = linear_model.LinearRegression().fit(X, y)
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)


# In[ ]:





# In[137]:


#X=data.drop("paddle_direction", axis=1)
#y = data.iloc[:,4]

#print(X.head())


# In[138]:


#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)


# In[139]:


#from sklearn.naive_bayes import GaussianNB # 1. choose model class
#model = GaussianNB()                       # 2. instantiate model
#model.fit(X_train, y_train)                  # 3. fit model to data
#y_model = model.predict(X_test)             # 4. predict on new data


# In[140]:


#from sklearn.metrics import accuracy_score
#accuracy_score(y_test, y_model)


# In[141]:


#X_test.to_csv('X_test.csv',index=False)
#y_test.to_csv('y_test.csv',index=False)


# In[142]:


from joblib import dump, load
dump(model, 'mymodel.joblib') 


# In[143]:


#input_dict = {'ball_x': 770, 'ball_y': 200, 'ball_vx': -12, 'ball_vy': -1, 'paddle_y': 200, 'Ball.RADIUS': 10, 'Paddle.L': 80, 'Paddle.STEP': 20, 'WIDTH': 800, 'HEIGHT': 400, 'BORDER': 20, 'VELOCITY ': 12, 'FPS': 30}
#input_df = pd.DataFrame([input_dict])
#print(input_df)


# In[130]:


#model.predict(input_df)[0]


# In[ ]:





# In[ ]:




