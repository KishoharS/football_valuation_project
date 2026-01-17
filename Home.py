import streamlit as st
import pandas as pd
import numpy as np
import joblib
from src.data_loader import load_players, load_transfers
from src.ui import apply_custom_style, render_sidebar

st.set_page_config(page_title="Smart Scout", layout="wide", page_icon="⚽")
apply_custom_style()
render_sidebar()

model = joblib.load('/Users/kishohars/Projects/football_valuation_project/models/linear_regression.pkl')
features = joblib.load('/Users/kishohars/Projects/football_valuation_project/models/linear_regression_features.pkl')

st.title("⚽ Smart Scout Dashboard")
st.markdown("### The future of AI-driven football scouting.")
st.markdown("Welcome to your command center. Use the **Market Value Estimator** below or explore player careers in the sidebar.")

players = load_players()
transfers = load_transfers()

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric("Total Players Database", f"{len(players):,}", delta="Live Data")
with col_b:
    st.metric("Transfer Records", f"{len(transfers):,}", delta="Updated")
with col_c:
    st.metric("Prediction Model", "XGBoost v1.0", delta="Active")

st.markdown("---")

with st.container():
    st.subheader("💡 Market Value Estimator")
    st.info("Predict the theoretical market value of a player based on their stats and profile.")

country_features = [f for f in features if f.startswith('country_of_citizenship_')]
countries = [f.replace('country_of_citizenship_', '') for f in country_features]
countries.sort()

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 16, 45, 25)
    league = st.selectbox("League Rank", [1,2,3,4,5,6,7,8,9,10,11,12,13,14])
    position = st.selectbox("Position", ["Attack", "Midfield", "Defender", "Goalkeeper"])
    country = st.selectbox("Country of Citizenship", countries)

with col2:
    goals = st.number_input("Goals per 90 minutes", min_value=0.0, max_value=2.0, value=0.1, step=0.01)
    assists = st.number_input("Assists per 90 minutes", min_value=0.0, max_value=2.0, value=0.1, step=0.01)
    last_season = st.number_input("last_season", min_value = 2012, max_value = 2024, step = 1)

if st.button("Predict Market Value"):
    input_data = pd.DataFrame(0, index=[0], columns=features)
    
    input_data['age'] = age
    input_data['league_rank'] = league
    input_data['goals_per90'] = goals
    input_data['assists_per90'] = assists
    input_data['last_season'] = last_season

    position_col = f"position_{position}"
    if position_col in features:
        input_data[position_col] = 1
    
    country_col = f"country_of_citizenship_{country}"
    if country_col in features:
        input_data[country_col] = 1
    
    prediction = model.predict(input_data)[0]
    
    if 'target_log' in features:
        prediction = np.exp(prediction)
    
    st.success(f"The estimated market value is: €{prediction:,.2f} Million")
    
    with st.expander("Debug Information"):
        st.write(f"Model expects {len(features)} features")
        st.write(f"Input data shape: {input_data.shape}")
        st.write("Non-zero features in input:")
        non_zero = input_data.loc[0, input_data.loc[0] != 0]
        st.write(non_zero)