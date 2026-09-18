"""
train_model.py
----------------
Generates a synthetic (but realistic) dataset of student attendance % and
marks %, labels each student's overall performance, and trains a
RandomForestClassifier to predict performance category from
(attendance, marks).

Run this once before starting the Flask server:
    python train_model.py

It writes two files into model/:
    model/performance_model.pkl   -> trained scikit-learn classifier
    model/scaler.pkl              -> fitted StandardScaler used at inference
"""

import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)

N_SAMPLES = 4000


def label_performance(attendance: float, marks: float) -> str:
    """
    Ground-truth labeling rule used to build the synthetic training set.

    Overall score is a weighted blend of attendance and marks (marks
    matter a bit more than attendance, which mirrors how most institutions
    weigh continuous assessment vs. attendance).
    """
    score = 0.35 * attendance + 0.65 * marks

    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"


def generate_dataset(n=N_SAMPLES):
    # Attendance and marks are correlated in real life (students who attend
    # more tend to score higher), so we simulate that instead of drawing
    # them fully independently.
    attendance = np.clip(np.random.normal(75, 15, n), 0, 100)
    noise = np.random.normal(0, 12, n)
    marks = np.clip(0.6 * attendance + 0.4 * np.random.normal(70, 20, n) + noise, 0, 100)

    labels = np.array([label_performance(a, m) for a, m in zip(attendance, marks)])

    X = np.column_stack([attendance, marks])
    return X, labels


def main():
    X, y = generate_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=6,
        random_state=42,
        class_weight="balanced",
    )
    clf.fit(X_train_scaled, y_train)

    y_pred = clf.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)

    print(f"Test accuracy: {acc * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    joblib.dump(clf, "model/performance_model.pkl")
    joblib.dump(scaler, "model/scaler.pkl")
    print("Saved model/performance_model.pkl and model/scaler.pkl")


if __name__ == "__main__":
    main()
