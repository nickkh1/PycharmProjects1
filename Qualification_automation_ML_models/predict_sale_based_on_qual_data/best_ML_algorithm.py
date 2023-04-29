import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# Load your dataset
from dataset_prepared import df_no_NA
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

# Define a list of classifiers to test
classifiers = [
    ('Logistic Regression', LogisticRegression(max_iter=1000)),
    ('k-NN', KNeighborsClassifier()),
    ('Decision Tree', DecisionTreeClassifier()),
    ('Random Forest', RandomForestClassifier()),
    ('SVM', SVC(probability=True)),
    ('Gradient Boosting', GradientBoostingClassifier())
]

# Evaluate each classifier
best_accuracy = 0
best_classifier = None

for name, classifier in classifiers:
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', classifier)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"{name} accuracy: {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_classifier = name

print(f"\nThe best classifier is: {best_classifier} with an accuracy of {best_accuracy:.4f}")
