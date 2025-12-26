import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model and features
model = joblib.load('/Users/kishohars/Projects/football_valuation_project/models/linear_regression.pkl')
features = joblib.load('/Users/kishohars/Projects/football_valuation_project/models/linear_regression_features.pkl')

st.title("Football Player Market Value Predictor")
st.write("Enter the player's details below to estimate their market valuation.")

# Extract unique countries from the feature list
country_features = [f for f in features if f.startswith('country_of_citizenship_')]
countries = [f.replace('country_of_citizenship_', '') for f in country_features]
countries.sort()

# Create input fields for the user
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

# Predict Button
if st.button("Predict Market Value"):
    # Create a DataFrame with all features initialized to 0
    input_data = pd.DataFrame(0, index=[0], columns=features)
    
    # Fill in the numerical features
    input_data['age'] = age
    input_data['league_rank'] = league
    input_data['goals_per90'] = goals
    input_data['assists_per90'] = assists
    input_data['last_season'] = last_season

    # One-hot encode position
    position_col = f"position_{position}"
    if position_col in features:
        input_data[position_col] = 1
    
    # One-hot encode country
    country_col = f"country_of_citizenship_{country}"
    if country_col in features:
        input_data[country_col] = 1
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Check if the model was trained on log-transformed values
    # If 'target_log' is in features, the prediction is in log scale
    if 'target_log' in features:
        prediction = np.exp(prediction)
    
    # Display result
    st.success(f"The estimated market value is: €{prediction:,.2f} Million")
    
    # Show debug info
    with st.expander("Debug Information"):
        st.write(f"Model expects {len(features)} features")
        st.write(f"Input data shape: {input_data.shape}")
        st.write("Non-zero features in input:")
        non_zero = input_data.loc[0, input_data.loc[0] != 0]
        st.write(non_zero)