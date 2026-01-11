# Hex-a-thon: Mental Health in Tech ("The Silent Burnout")

This project analyzes the [OSMI Mental Health in Tech Survey 2014](https://www.kaggle.com/osmi/mental-health-in-tech-survey) to uncover trends in workplace mental health and predict factors that influence seeking treatment.

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
    *   Developed `model.py` using **Scikit-Learn**.
    *   Implemented a **Random Forest Classifier** to predict the `treatment` variable.
    *   **Result**: Achieved **80% Accuracy** on the test set.
*   **Exploratory Analysis**: 
    *   Created `analysis.ipynb` for initial EDA and visualizations.

## 📋 Next Steps (Roadmap)

*   [x] **Full Scale Analysis**: Run the pipeline on the complete 1,200+ row dataset.
*   [ ] **Hex Integration**: Port the cleaning and analysis logic into a **Hex Project** for interactive dashboards.
*   [ ] **Storytelling**: Refine the "Silent Burnout" narrative for the final submission.
*   [ ] **Submission**: Record the 3-minute demo video and submit to Devpost.

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
