from pandas import *
from math import ceil
from sklearn.ensemble import GradientBoostingRegressor, VotingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np

# Load the data
print('Reading the data...')
data = read_csv("insurance.csv")
print('Read completed.\n')

# One-hot encoding
print('Preprocessing data...')
data = get_dummies(data, columns=['sex', 'smoker', 'region'], drop_first=True)

# Format and Split the data
x = data[['age', 'bmi', 'children', 'sex_male', 'smoker_yes', 'region_northwest', 'region_southeast', 'region_southwest']]
y = data['charges']

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.4)
print('Preprocessing completed.\n')

# Train the model and make predictions
r1 = GradientBoostingRegressor(loss='huber', learning_rate=0.13, max_features='auto', alpha=0.7, random_state=1)
r2 = GradientBoostingRegressor(loss='huber', learning_rate=0.13, max_features='auto', alpha=0.7, random_state=1)
model = VotingRegressor([('gbr1', r1), ('gbr2', r2)])
model.fit(train_x, train_y)

print('Testing the model...')
predicted = model.predict(test_x)
mae = mean_absolute_error(test_y, predicted)
print('Mean Absolute Error : ',mae)
print('Testing completed.\n')

# Predict cost for a sample customer
print('Running for one sample...')
sample = DataFrame({
            'age': 26,
            'bmi': 25.44,
            'children': 1,
            'sex_male': 1, 
            'smoker_yes' : 0,
            'region_northeast': 0,
            'region_southeast': 0,
            'region_southwest': 1,
          }, [1])
print('Sample data : ',sample)
cost = model.predict(sample)[0]
print('Predicted cost : ', cost)
print('Sample run completed.\n')

print('Calculating premium...')
# Calculate premium
def compute_monthly_premium(cost):
    multiplier = 1.1
    return ceil(cost*multiplier)/12

print('Monthly Premium : ',compute_monthly_premium(cost))
print('Premium calculated.\n')

print('Program completed.')

print('Mean Absolute Error : ',mae)
