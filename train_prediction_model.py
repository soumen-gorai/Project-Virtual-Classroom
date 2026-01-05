"""
Script to train a student performance prediction model using an online dataset
and integrate it with EduConnect.

This script demonstrates how to:
1. Download and preprocess an online student performance dataset
2. Train a machine learning model for predicting student performance
3. Save the model for use in EduConnect backend
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

def download_sample_dataset():
    """
    Create a sample student performance dataset for demonstration purposes.
    In a real scenario, you would download an actual dataset from sources like:
    - UCI Machine Learning Repository
    - Kaggle
    - OpenML
    """
    # Create sample data that mimics real student performance data
    np.random.seed(42)
    
    # Generate sample data
    n_students = 1000
    
    data = {
        'student_id': [f'STU{i:04d}' for i in range(1, n_students + 1)],
        'attendance_rate': np.random.normal(85, 10, n_students),
        'assignment_score': np.random.normal(80, 15, n_students),
        'exam_score': np.random.normal(75, 20, n_students),
        'course_load': np.random.choice([3, 4, 5, 6], n_students, p=[0.2, 0.5, 0.25, 0.05]),
        'previous_gpa': np.random.normal(3.0, 0.5, n_students),
        'study_hours_per_week': np.random.normal(15, 5, n_students),
        'participation_score': np.random.normal(70, 20, n_students)
    }
    
    # Ensure values are within reasonable bounds
    data['attendance_rate'] = np.clip(data['attendance_rate'], 0, 100)
    data['assignment_score'] = np.clip(data['assignment_score'], 0, 100)
    data['exam_score'] = np.clip(data['exam_score'], 0, 100)
    data['previous_gpa'] = np.clip(data['previous_gpa'], 0, 4.0)
    data['study_hours_per_week'] = np.clip(data['study_hours_per_week'], 0, 50)
    data['participation_score'] = np.clip(data['participation_score'], 0, 100)
    
    # Create target variable (final grade) based on features
    # This creates a realistic relationship between features and target
    target = (
        0.25 * data['attendance_rate'] +
        0.20 * data['assignment_score'] +
        0.30 * data['exam_score'] +
        0.10 * data['previous_gpa'] * 25 +  # Scale GPA to 0-100 range
        0.05 * data['study_hours_per_week'] * 2 +  # Scale study hours
        0.10 * data['participation_score'] +
        np.random.normal(0, 5, n_students)  # Add some noise
    )
    
    # Ensure target is within 0-100 range
    data['final_grade'] = np.clip(target, 0, 100)
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save dataset to CSV file
    df.to_csv('student_performance_dataset.csv', index=False)
    
    print("Sample dataset created and saved as 'student_performance_dataset.csv':")
    print(df.head())
    print(f"\nDataset shape: {df.shape}")
    print(f"\nDataset info:")
    print(df.describe())
    
    return df

def preprocess_data(df):
    """
    Preprocess the dataset for machine learning
    """
    # Handle missing values (if any) - only for numeric columns
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    # Define features and target
    feature_columns = [
        'attendance_rate', 
        'assignment_score', 
        'exam_score', 
        'course_load', 
        'previous_gpa',
        'study_hours_per_week',
        'participation_score'
    ]
    
    X = df[feature_columns]
    y = df['final_grade']
    
    return X, y

def train_model(X, y):
    """
    Train a Random Forest Regressor model
    """
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Create and train the model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R² Score: {r2:.4f}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\nFeature Importance:")
    print(feature_importance)
    
    return model, X_test, y_test, y_pred

def save_model(model, filename='student_performance_model.pkl'):
    """
    Save the trained model to disk
    """
    # Save model
    joblib.dump(model, filename)
    print(f"\nModel saved as {filename}")
    
    # Also save as JSON for inspection (optional)
    import json
    model_info = {
        'model_type': 'RandomForestRegressor',
        'n_estimators': 100,
        'max_depth': 10,
        'random_state': 42
    }
    
    with open('model_info.json', 'w') as f:
        json.dump(model_info, f, indent=2)
    
    print("Model information saved as model_info.json")

def demonstrate_prediction(model, X_sample):
    """
    Demonstrate how to use the model for prediction
    """
    # Make predictions on sample data
    predictions = model.predict(X_sample[:5])
    
    print("\nSample Predictions:")
    print("Actual Features -> Predicted Grade")
    for i in range(5):
        features = X_sample.iloc[i].to_dict()
        prediction = predictions[i]
        print(f"{features} -> {prediction:.2f}")

def main():
    """
    Main function to orchestrate the training process
    """
    print("=== Student Performance Prediction Model Training ===\n")
    
    # Step 1: Download/Create dataset
    print("1. Creating sample dataset...")
    df = download_sample_dataset()
    
    # Step 2: Preprocess data
    print("\n2. Preprocessing data...")
    X, y = preprocess_data(df)
    
    # Step 3: Train model
    print("\n3. Training model...")
    model, X_test, y_test, y_pred = train_model(X, y)
    
    # Step 4: Demonstrate prediction
    print("\n4. Demonstrating prediction...")
    demonstrate_prediction(model, X_test)
    
    # Step 5: Save model
    print("\n5. Saving model...")
    save_model(model, 'student_performance_model.pkl')
    
    print("\n=== Training Complete ===")
    print("\nTo integrate with EduConnect:")
    print("1. Copy 'student_performance_model.pkl' to EduConnect/backend/models/")
    print("2. Update prediction.controller.js to load and use the trained model")
    print("3. Modify the prediction logic to use actual student data from MongoDB")

if __name__ == "__main__":
    main()