# AI Project 2 - Data Classification Using AI

## Objective

Build a basic classification model using a small dataset and apply supervised learning techniques to classify data accurately.

## Dataset

Iris Dataset

* Total Samples: 150
* Features: 4
* Classes: 3

Features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

Classes:

* Setosa
* Versicolor
* Virginica

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn

## Algorithm Used

### K-Nearest Neighbors (KNN)

KNN is a supervised machine learning algorithm that classifies a data point based on the majority class of its nearest neighbors.

Value of K used:

* K = 5

## Project Workflow

1. Load Iris Dataset
2. Explore Dataset
3. Split Data into Training and Testing Sets (80:20)
4. Apply Feature Scaling using StandardScaler
5. Train KNN Classifier
6. Predict Test Data
7. Evaluate Performance
8. Generate Confusion Matrix Heatmap

## Results

### Accuracy

Accuracy: 100%

### Confusion Matrix

[[10 0 0]
[0 9 0]
[0 0 11]]

### Classification Metrics

* Precision: 1.00
* Recall: 1.00
* F1-Score: 1.00

## Visualization

A confusion matrix heatmap was generated using Seaborn and Matplotlib to visually evaluate model performance.

Output File:

* confusion_matrix.png

## Project Structure

AI_project2_classification

├── classification.py

├── README.md

├── requirements.txt

└── confusion_matrix.png

## Conclusion

This project demonstrates the implementation of a supervised machine learning classification model using the Iris dataset. The KNN classifier successfully classified all test samples with 100% accuracy. The model was evaluated using a confusion matrix, precision, recall, and F1-score, and the results were visualized through a confusion matrix heatmap.
