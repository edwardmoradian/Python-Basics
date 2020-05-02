#!/usr/bin/env python
# coding: utf-8

# In[324]:


import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
print(f"TensorFlow version {tf.__version__}")
np.set_printoptions(threshold=np.inf)
pd.set_option('display.max_rows', 800)


# In[307]:


#cheesee
data = pd.read_csv("C:/Users/emoradia/OneDrive - Capgemini/Desktop/Home/kaggle/house prices/train.csv")
submit_data = pd.read_csv("C:/Users/emoradia/OneDrive - Capgemini/Desktop/Home/kaggle/house prices/test.csv")


# In[308]:


num_columns = []
cat_columns = []

for column in data.keys():
    if data[column].dtype == object:
        cat_columns.append(column)
    else:
        num_columns.append(column)

# remove Id variable
num_columns.remove("Id")
        
print(f"Number of numeric columns: {len(num_columns)}")
print(f"Number of categorical columns: {len(cat_columns)}")
print("The target numeric variable is SalePrice")


# In[309]:


# use sklearn model selection to split the data
train_data, test_data = train_test_split(data,test_size=0.2)


# In[310]:


print(f"Test Samples: {len(test_data)}")
print(f"Train Samples: {len(train_data)}")


# In[311]:


for column in cat_columns:
    train_data[column].fillna(value="Missing",inplace=True)
    test_data[column].fillna(value="Missing",inplace=True)


# In[312]:


for column in num_columns:
    train_data[column].fillna(train_data[column].median(), inplace = True)
    test_data[column].fillna(test_data[column].median(), inplace = True)


# In[313]:


train_data, val_data = train_test_split(train_data, test_size=0.2)


# In[314]:


scaler = StandardScaler()

train_data[num_columns] = scaler.fit_transform(train_data[num_columns])
val_data[num_columns] = scaler.transform(val_data[num_columns])
test_data[num_columns] = scaler.transform(test_data[num_columns])


# In[315]:


def df_to_dataset(dataframe, shuffle=True,batch_size=32):
    dataframe = dataframe.copy()
    labels = dataframe.pop('SalePrice')
    ds = tf.data.Dataset.from_tensor_slices((dict(dataframe),labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    return ds

batch_size = 32
train_ds = df_to_dataset(train_data, batch_size=batch_size)
val_ds = df_to_dataset(val_data, shuffle=False, batch_size=batch_size)
test_data['SalePrice'] = 0
test_ds = df_to_dataset(test_data, shuffle=False, batch_size=batch_size)


# In[316]:


for feature_batch, label_batch in train_ds.take(1):
    print('Every feature:', list(feature_batch.keys()))
    print('A batch of alleys:', feature_batch['Alley'])
    print('A batch of targets:', label_batch )


# In[317]:


feature_columns = []

num_columns.remove('SalePrice')

for column in num_columns:
    column = tf.feature_column.numeric_column(column)
    feature_columns.append(column)

for column in cat_columns:
    column = tf.feature_column.indicator_column(tf.feature_column.categorical_column_with_vocabulary_list(column,list(train_data[column].unique())))
    feature_columns.append(column)

feature_layer = tf.keras.layers.DenseFeatures(feature_columns)


# In[318]:


def get_model():
    model = Sequential([
        feature_layer,
        Dense(64, activation="relu",name="Dense_2"),
        BatchNormalization(),
        Dropout(0.1),
        Dense(128, activation="relu",name="Dense_3"),
        BatchNormalization(),
        Dropout(0.1),
        Dense(256, activation="relu",name="Dense_4"),
        BatchNormalization(),
        Dropout(0.1),
        Dense(128, activation="relu",name="Dense_5"),
        BatchNormalization(),
        Dropout(0.1),
        Dense(64, activation="relu",name="Dense_6"),
        BatchNormalization(),
        Dropout(0.1),
        Dense(1)      
    ])
    return model
    


# In[319]:


# print the model summary
model = get_model()


# In[320]:


model.compile(loss='mse',
                optimizer=tf.keras.optimizers.Adam(.0001),
                metrics=['mse'])


# In[276]:


z=0
for i in (val_data.isna().sum() == 0):
    if i == False:
        z=z+1
z


# In[297]:


train_data["SalePrice"]


# In[322]:


history = model.fit(train_ds,validation_data=val_ds,epochs=50,verbose=1)


# In[39]:


history


# In[323]:


loss, mse = model.evaluate(test_ds)
print("mse", mse)


# In[ ]:




