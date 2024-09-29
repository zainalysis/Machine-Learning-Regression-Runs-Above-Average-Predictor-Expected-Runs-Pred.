import streamlit as st
import pandas as pd
import joblib

# Function to load the model
def load_model():
    model_path = 'linear_regression_model.pkl'
    return joblib.load(model_path)

# Loaded model
loaded_model = load_model()

st.title("T20 Expected Runs Predictor On Nth Ball")

# Input fields
nth_ball = st.number_input("Enter The Ball Number:", min_value=0, max_value=120, step=1)
cur_bat_bf = st.number_input("Enter The Ball Number Batter Faced:", min_value=0, max_value=nth_ball, step=1)  # Ensure cur_bat_bf is <= nth_ball
inns_wkts = st.number_input("Enter No. of Wickets Down:", min_value=0, max_value=9, step=1)
inns_rr = st.number_input("Enter Innings Run Rate:", min_value=0.0, max_value=36.0, step=0.1)

# Button to predict total runs
if st.button("Predict Expected Runs"):
    if cur_bat_bf > nth_ball:
        st.error("Error: The number of balls faced by the batter cannot be greater than the ball number.")
    else:
        # Create a DataFrame from the input data
        input_data = pd.DataFrame({
            'nth_ball': [nth_ball],
            'cur_bat_bf': [cur_bat_bf],
            'inns_wkts': [inns_wkts],
            'inns_rr': [inns_rr]
        })

        # Predict using the loaded model
        prediction = loaded_model.predict(input_data)

        # Display the prediction as a floated value rounded to 2 decimal places
        st.success(f"Expected Runs: {prediction[0]:.2f}")
        
# Developer credit
st.markdown("---")  # Adds a horizontal line
st.markdown("Developed by [Zain Ul Hassan](https://twitter.com/zainalysis) (@zainalysis)")