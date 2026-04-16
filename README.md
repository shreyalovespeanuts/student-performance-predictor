# student-performance-predictor
Machine learning-based system to predict student academic performance using academic and behavioral data, with data visualization for actionable insights.

🎓 Student Performance Predictor
A smart machine learning system designed to predict student academic performance using a combination of academic, behavioral, and lifestyle factors. The project focuses on generating accurate predictions as well as meaningful insights to support better academic decision-making.
Project Overview
Educational institutions often rely only on academic scores to evaluate students. However, real performance depends on multiple factors such as study habits, lifestyle, and mental health.
This project builds an **end-to-end machine learning pipeline** that integrates these dimensions to improve prediction accuracy and provide deeper insights into student success.
Key Features
* Combines **academic + behavioral + lifestyle data**
* Performs detailed **Exploratory Data Analysis (EDA)**
* Implements multiple ML models:
  * Logistic Regression
  * Decision Tree
  * Random Forest
* Evaluates models using:
  * Accuracy
  * Confusion Matrix
  * Precision, Recall, F1-score
* Identifies key factors affecting student performance
Dataset
* Source: Kaggle
* Features used:
  * Study hours
  * Attendance percentage
  * Sleep duration
  * Social media usage
  * Mental health rating
  * Exam scores
   The dataset combines both academic and lifestyle attributes to provide a holistic understanding of performance.
Tech Stack
* **Language:** Python
* **Libraries:**
  * Pandas
  * NumPy
  * Scikit-learn
  * Matplotlib
  * Seaborn
Workflow
1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Feature Selection
5. Model Training
6. Model Evaluation
7. Visualization & Insights
Model Performance

🔹 Logistic Regression
* Accuracy: **94.5%**
* Strong balance between precision and recall
Class 0 → Precision: 0.81 | Recall: 0.79 | F1-score: 0.80  
Class 1 → Precision: 0.97 | Recall: 0.97 | F1-score: 0.97  
🔹 Decision Tree
* Accuracy: **90.5%**
* Slightly lower performance due to overfitting tendencies
```id="dt_cr"
Class 0 → Precision: 0.65 | Recall: 0.71 | F1-score: 0.68  
Class 1 → Precision: 0.95 | Recall: 0.94 | F1-score: 0.94  
```
🔹 Random Forest
* Accuracy: **94.0%**
* High recall for majority class and robust performance
Confusion Matrix:
```id="rf_cm"
[[17 11]
 [ 1 171]]
```
Classification Report:
```id="rf_cr"
Class 0 → Precision: 0.94 | Recall: 0.61 | F1-score: 0.74  
Class 1 → Precision: 0.94 | Recall: 0.99 | F1-score: 0.97  
```
Key Insights
* Logistic Regression achieved the **highest accuracy (94.5%)**
* Random Forest provided **strong generalization and high recall**
* Decision Tree showed comparatively lower performance
* Behavioral factors (study time, engagement) significantly influence outcomes
* Combining lifestyle + academic data improves prediction accuracy
Sample Outputs

Live Demo

Project Structure
```id="proj_struct"
student-performance-predictor/
│
├── student-performance-predictor.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```
Future Improvements
* Deploy as a full interactive web application
* Integrate real-time student data input
* Apply advanced models (XGBoost, Neural Networks)
* Add recommendation system for students
👩‍💻 Author
**Shreya Samadhiya**
* B.Tech CSE (3rd Year)
* Interested in Data Analytics, UI/UX, and Product Development
⭐ Acknowledgements
* Kaggle for dataset
* Open-source ML community
* Educational Data Mining research

⭐ If you found this project useful, consider giving it a star!
