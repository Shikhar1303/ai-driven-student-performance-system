# 🤖 AI Attendance-to-Performance Analyzer

A lightweight **browser-based AI application** that analyzes attendance, punctuality, and consecutive absences to predict a student's **performance rating**.

The project uses **TensorFlow.js** to build and train a small Artificial Neural Network directly inside the user's browser. No backend or server is required.

---

## 📌 Project Overview

The **AI Attendance-to-Performance Analyzer** takes three inputs:

* 📊 Attendance Percentage
* ⏰ Punctuality Rate
* 📅 Maximum Consecutive Absences

Using these parameters, the application runs a trained neural network and generates:

* Predicted Performance Score
* Performance Category
* AI-generated Insights
* Recommendations for improvement

The entire AI model runs **locally in the browser** using TensorFlow.js.

---

## ✨ Features

* 🧠 Browser-based Artificial Neural Network
* ⚡ Real-time performance prediction
* 🌐 No backend/server required
* 🔒 Input data stays in the browser
* 📱 Responsive web interface
* 📊 Performance score displayed as a percentage
* 📝 Automatic insights and recommendations
* 🎨 Clean and simple user interface
* 🚀 Easy to run and deploy

---

## 🛠️ Technologies Used

| Technology                    | Purpose                       |
| ----------------------------- | ----------------------------- |
| **HTML5**                     | Web page structure            |
| **CSS3**                      | User interface and styling    |
| **JavaScript**                | Application logic             |
| **TensorFlow.js**             | Neural network and prediction |
| **Artificial Neural Network** | Performance prediction        |

---

## 🧠 How the AI Works

The application creates a simple neural network using TensorFlow.js.

### Neural Network Architecture

```text
Input Layer
    │
    ├── Attendance
    ├── Punctuality
    └── Consecutive Absences
    │
    ▼
Dense Layer (8 neurons)
    │
    ▼
Dense Layer (4 neurons)
    │
    ▼
Output Layer (1 neuron)
    │
    ▼
Performance Score
```

The model uses:

* **ReLU** activation in hidden layers
* **Sigmoid** activation in the output layer
* **Adam** optimizer
* **Mean Squared Error** loss function
* **150 training epochs**

---

## 📊 Input Processing

Before prediction, the inputs are normalized between approximately `0` and `1`.

### Attendance

```text
Normalized Attendance = Attendance / 100
```

### Punctuality

```text
Normalized Punctuality = Punctuality / 100
```

### Consecutive Absences

```text
Normalized Absence = 1 - (Consecutive Absences / 10)
```

The normalized values are passed into the neural network.

---

## 📈 Performance Categories

The predicted score is converted into a percentage.

| Score             | Category             |
| ----------------- | -------------------- |
| **80% and above** | High Performer       |
| **60% – 79.9%**   | Moderate Performer   |
| **Below 60%**     | At-Risk / Low Output |

The application also generates recommendations based on the predicted category.

---

## 🗂️ Project Structure

```text
AI-Attendance-Performance-Analyzer/
│
├── index.html
└── README.md
```

The current version contains the complete application inside `index.html`.

---

## 🚀 How to Run

### Method 1 — Open Directly

1. Download or clone this repository.
2. Open the project folder.
3. Double-click:

```text
index.html
```

The application will open in your browser.

### Method 2 — VS Code

Open the project folder in **Visual Studio Code**.

Then open `index.html` in a browser.

You can also use the **Live Server** extension in VS Code for easier development.

---

## 🌐 TensorFlow.js

TensorFlow.js is loaded through the jsDelivr CDN:

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.10.0/dist/tf.min.js"></script>
```

This allows the neural network to run directly in the browser without requiring Python, a server, or a separate ML backend.

---

## 🔄 Application Workflow

```text
User enters data
       ↓
Attendance
Punctuality
Consecutive Absences
       ↓
Input Normalization
       ↓
TensorFlow.js Neural Network
       ↓
Performance Prediction
       ↓
Performance Score
       ↓
Category + Recommendation
```

---

## 🔐 Privacy

This project performs its calculations locally in the browser.

The application does not require:

* ❌ Database
* ❌ Backend server
* ❌ User account
* ❌ API key
* ❌ External prediction API

The entered attendance and performance-related values are processed locally by the browser.

---

## ⚠️ Important Note

This project uses **synthetic training data** created for demonstration and educational purposes.

Therefore, the predicted performance score should **not be considered a scientifically validated prediction of actual academic performance**.

For a production-grade system, the model should be trained and evaluated using a sufficiently large, representative real-world dataset with appropriate validation and privacy safeguards.

---

## 🔮 Future Improvements

Possible improvements include:

* 📚 Train the model using a real academic dataset
* 📊 Add study hours as an input
* 📝 Add assignment/quiz performance
* 🎯 Add previous semester performance
* 📈 Add performance history charts
* 💾 Store historical predictions
* 🔐 Add authentication
* 🗄️ Connect to a database
* 🖥️ Build a teacher/admin dashboard
* 📱 Improve mobile UI
* 🤖 Experiment with more advanced ML models
* 📊 Add model evaluation metrics such as MAE and R²

---

## 🎯 Learning Objectives

This project demonstrates:

* Fundamentals of Artificial Intelligence
* Neural Network architecture
* Data normalization
* Model training
* Model inference
* TensorFlow.js
* JavaScript-based machine learning
* Frontend development
* AI integration into web applications

---

## 👨‍💻 Author

**Shikhar Khare**

B.Tech — Artificial Intelligence

---

## ⭐ Project Purpose

This project was developed as an educational AI/ML project to demonstrate how a machine learning model can be integrated into a web application and executed directly inside a user's browser.

If you find this project useful, consider giving the repository a ⭐.
