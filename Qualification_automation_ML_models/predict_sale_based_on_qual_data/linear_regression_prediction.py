import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score



# Load your dataset
from Qualification_automation_ML_models.predict_sale_based_on_qual_data.dataset_prepared import df_no_NA
data = df_no_NA

# Split the dataset into features and target variable
X = data[['Current salary', 'Education', 'Goal for Study', 'Work experience']]
y = data['Lead Stage']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define preprocessing steps
categorical_features = ['Current salary', 'Education', 'Goal for Study', 'Work experience']
categorical_transformer = OneHotEncoder()

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)])

linear_regression = LinearRegression()
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', linear_regression)])

pipeline.fit(X_train, y_train)
'''измеряем accuracy'''
y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.4f}")
print(f"Mean Squared Error: {mse:.4f}")
print(f"Root Mean Squared Error: {rmse:.4f}")
print(f"R-squared: {r2:.4f}")


new_data = pd.DataFrame({'Current salary': ['5-7'],
                         'Education': ['Non-IT degree'],
                         'Goal for Study': ['Grow in the same career'],
                         'Work experience': ['No experience']})

predicted_value = pipeline.predict(new_data)
print("Predicted Value:", predicted_value[0])

'''
3-5          7855
0-3          7633
No salary    6127
5-7          3092
10+          2421
7-8          1428
9-10         1056
Name: Current salary

Switch career              23224
Grow in the same career     6388
Name: Goal for Study

Non-IT degree    18586
Other             4591
Degree in IT      4212
No degree         1927
Don't know         175
Name: Education

0-3              14938
3+                9880
No experience     4794
Name: Work experience
'''