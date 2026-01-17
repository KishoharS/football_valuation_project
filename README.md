# ⚽ Smart Scout Dashboard

A comprehensive football analytics portfolio project that combines **Machine Learning Valuation** with **Transfer Market Analysis** and **Player Performance Profiling**.

## Features

### 1. Market Value Estimator (`Home.py`)
Predicts a player's current market value using a Machine Learning model (XGBoost/Linear Regression) based on their age, league, stats, and nationality.

### 2. Transfer Market Analysis (`pages/2_Transfer_Market.py`)
*   **Valuation History:** Interactive line chart showing market value trends over time.
*   **Fee vs. Value:** Visual comparison of actual transfer fees paid vs. estimated value at the time.
*   **ROI Calculator:** Tracks total career transfer fees.

### 3. Player Performance Profile (`pages/1_Player_Profile.py`)
*   **Scout Radar:** Radar chart comparing Goals, Assists, and Discipline per 90 mins against benchmarks.
*   **Career Trajectory:** Season-by-season goals and assists.
*   **Event Analysis:** Breakdown of match events (Goals, Cards, Substitutions).

## Installation

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    streamlit run Home.py
    ```

## Data Sources
*   **Transfermarkt (via Kaggle):** Valuations, Transfers, and Player metadata.
*   **Game Events:** Granular match logs for performance analysis.

## Tech Stack
*   **Frontend:** Streamlit
*   **Viz:** Plotly
*   **ML:** Scikit-Learn
*   **Data:** Pandas
