# Hex-a-thon: Mental Health in Tech ("The Silent Burnout")

[![Hex App](https://img.shields.io/badge/Hex-Live_App-blue?style=for-the-badge&logo=hex)](https://app.hex.tech/virtual-hackathon/app/The-Silent-Burnout-0328dghwRZcpUauEx0hJne/latest)

This project analyzes the [OSMI Mental Health in Tech Survey 2014](https://www.kaggle.com/osmi/mental-health-in-tech-survey) to uncover trends in workplace mental health and predict factors that influence seeking treatment.

## 📽️ Demo Video

[![Watch the Demo](https://img.youtube.com/vi/fX6BQgnKAQk/0.jpg)](https://youtu.be/fX6BQgnKAQk)

## 🚀 Project Overview

We are building a data narrative that explores:
*   **Demographics**: Who is working in tech and how do they identify?
*   **Workplace Support**: Do tech companies provide adequate mental health benefits?
*   **Prediction**: Can we predict if an employee is likely to seek treatment based on their workplace environment?

## ✅ Current Progress (Accomplished)

*   **Data Pipeline**: 
    *   Established a raw data loader and validation script (`data_check.py`).
    *   Successfully handled messy data input, particularly standardizing the free-text `Gender` column.
    *   **Full Scale Analysis**: Processed the complete dataset (~1,260 rows).
*   **Predictive Modeling**: 
    *   Developed `model.py` and Hex Random Forest pipeline.
    *   Implemented a **Random Forest Classifier** to predict the `treatment` variable.
    *   **Result**: Achieved **64.1% Accuracy** identifying key drivers like `care_options` and `benefits`.
*   **Exploratory Analysis**: 
    *   Created `analysis.ipynb` and Hex Logic.

## 🏁 Project Roadmap (Completed)

*   [x] **Full Scale Analysis**: Run the pipeline on the complete 1,200+ row dataset.
*   [x] **Hex Integration**: Live "Data App" completed with Country filters and interactive charts.
*   [x] **Submission**: Video recorded and project **Submitted to Devpost & Hex**!

## 🛠️ How to Run Locally

1.  **Install Dependencies**:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn
    ```

2.  **Verify Data**:
    ```bash
    python data_check.py
    ```

3.  **Train Model**:
    ```bash
    python model.py
    ```

4.  **Explore Analysis**:
    ```bash
    jupyter notebook analysis.ipynb
    ```
