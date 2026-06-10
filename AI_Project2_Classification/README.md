# AI Project 2 - Data Classification Using AI

## Objective

Build a basic classification model using supervised machine learning techniques and evaluate its performance using standard classification metrics.

---

## Dataset

**Iris Dataset**

* Total Samples: 150
* Features: 4
* Classes: 3

### Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn

---

## Algorithm Used

### K-Nearest Neighbors (KNN)

KNN is a supervised machine learning algorithm that classifies data points based on the majority class of their nearest neighbors.

**K Value Used:** 5

---

## Project Workflow

1. Load the Iris Dataset
2. Split Data into Training and Testing Sets (80:20)
3. Apply Feature Scaling using StandardScaler
4. Train KNN Classifier
5. Predict Test Data
6. Evaluate Model Performance
7. Generate Confusion Matrix Heatmap

---

## Results

### Accuracy

**100%**

### Confusion Matrix

```text
[[10 0 0]
 [0 9 0]
 [0 0 11]]
```

### Classification Report

* Precision: 1.00
* Recall: 1.00
* F1-Score: 1.00

---

## Visualization

A confusion matrix heatmap was generated using Seaborn and Matplotlib to visualize the model's performance.

Output File:

* confusion_matrix.png

---

## Project Structure

```text
AI_Project2_Classification
│
├── classification.py
├── README.md
├── requirements.txt
└── confusion_matrix.png
```

---

## Conclusion

This project demonstrates the implementation of a supervised machine learning classification model using the Iris dataset. The K-Nearest Neighbors (KNN) classifier achieved 100% accuracy on the test dataset and was evaluated using a confusion matrix, precision, recall, and F1-score metrics. The confusion matrix heatmap provides a clear visual representation of the model's performance.
