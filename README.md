Flipkart Customer Service Satisfaction Classification

This repository contains the complete end-to-end machine learning pipeline to classify Flipkart customer service satisfaction (CSAT) scores using Google Cloud Platform (GCP).

📌 Objective
Predict the CSAT (Customer Satisfaction) score based on support data using a classification model trained with Google Vertex AI AutoML.

📁 Project Structure
Flipkart-csat/
├── cleaned_customer_support_data.csv        # Preprocessed dataset used for training
├── predict_input.csv                        # Input data for batch prediction
├── flipkart_csat_predictions.csv            # Final predictions from Vertex AI model
├── flipkart_csat_notebook.ipynb             # Jupyter notebook (end-to-end pipeline)
├── charts/                                  # Generated visualizations (PNG/CSV)
├── Flipkart_CSAT_Report.pdf                 # Final presentation/report
└── README.md                                # This file


🚀 Pipeline Steps
Data PreparationCleaned and uploaded CSAT dataset to Google Cloud Storage.
Model TrainingTrained a classification model using Vertex AI AutoML with a 1-node hour budget.
EvaluationAnalyzed accuracy, ROC-AUC, PR-AUC, and feature importance.
PredictionPerformed batch prediction and generated confidence scores.
Result ExportCombined all results into a single CSV and uploaded to GitHub.

🔍 Model Details
Model Type: Vertex AI AutoML Tabular (Classification)
Target Column: csat_score
Evaluation Metrics:
ROC AUC: 0.901
PR AUC: 0.727
F1 Score: 0.718

📈 Charts and Visualizations

Charts include:
Class distribution of predicted CSAT scores
Confidence distribution for each prediction
These are stored in the charts/ folder.

📦 Dependencies
Python 3.11
Google Colab
Google Cloud SDK
Libraries: pandas, matplotlib, google-cloud-storage, google-cloud-aiplatform

🔗 Live Resources
🔍 Prediction Results (CSV)
📊 Report: Flipkart_CSAT_Report.pdf
👨‍💻 Author

Ishan Mishra  | BTech Graduate | AI/ML Developer | GCP PractitionerEmail: ihrm.aiml@gmail.com
