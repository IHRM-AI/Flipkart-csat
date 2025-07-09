
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Flipkart CSAT Dashboard", layout="wide")

st.title("📊 Flipkart Customer Service Satisfaction Dashboard")
st.markdown("This dashboard visualizes the performance of the CSAT prediction model built on GCP Vertex AI.")

# Load prediction CSV
df = pd.read_csv("flipkart_csat_predictions.csv")

# --- Summary Stats ---
st.subheader("🔍 Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", f"{len(df):,}")
col2.metric("Average Predicted CSAT", round(df['predicted_csat'].mean(), 2))
col3.metric("Top Agent", df['agent_name'].value_counts().idxmax())

# --- Display Charts ---
st.subheader("📈 Prediction Charts")
chart_folder = "charts"

chart_files = [
    "predicted_csat_distribution.png",
    "prediction_confidence_distribution.png",
    "handling_time_vs_csat.png",
    "item_price_vs_csat.png",
    "agentwise_avg_csat.png",
    "shift_vs_csat.png"
]

for chart in chart_files:
    st.image(os.path.join(chart_folder, chart), use_column_width=True, caption=chart.replace("_", " ").title())

# --- Download Section ---
st.subheader("📥 Download Predictions")
with open("flipkart_csat_predictions.csv", "rb") as f:
    st.download_button("Download Predictions CSV", f, file_name="flipkart_csat_predictions.csv")
