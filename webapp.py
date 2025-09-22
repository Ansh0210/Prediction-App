import streamlit as st
import time
import pickle
import numpy as np
import pandas as pd
import os

# Configure page
st.set_page_config(
    page_title="ML Prediction App",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def load_diabetes_model():
    try:
        with open('./Diabetes Prediction/diabetes_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
        return None
    
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Define model options
MODELS_OPTIONS = {"Model 1": "Predict House Prices in California",
                 "Model 2": "Predict Diabetes Likelihood for Women",
                }

# Title and description
st.title("🤖 Predictive ML Web App")
st.write("This is a simple web application for ML model predictions. Select a model from the sidebar menu.")

# Add a sidebar with a dropdown menu
st.sidebar.header("Model Selection")
selected_model = st.sidebar.selectbox("Select a model:", 
                                      list(MODELS_OPTIONS.keys()),
                                      help="Choose a machine learning model to see its description.",
                                      disabled=False,
                                      key="model_selector"
                                      )

if selected_model:
    st.sidebar.markdown(f"**Description:** {MODELS_OPTIONS[selected_model]}")

st.sidebar.divider()
st.sidebar.write("More models coming soon!")

st.write(f"You selected: {selected_model}")

# Load the diabetes model if Model 2 is selected
diabetes_model = None
if selected_model == "Model 2":
    diabetes_model = load_diabetes_model()
elif selected_model == "Model 1":
    st.info("Model 1 is a placeholder. Model loading not implemented.")
else:
    st.warning("Please select a valid model.")

# create two columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Input Features")
    st.write("Feature inputs will go here.")
    
    if selected_model == "Model 1":
        f1_medInc = st.number_input("Feature 1: Median Income", min_value=0.0, max_value=20.0, value=0.0, step=0.1)
        f2_aveRooms = st.number_input("Feature 2: Average Rooms", min_value=0, max_value=20, value=1, step=1)
        f3_aveBedrms = st.number_input("Feature 3: Average Bedrooms", min_value=1, max_value=20, value=1, step=1)
        f4_longitude = st.number_input("Feature 4: Longitude", min_value=-180.0, max_value=180.0, value=0.0, step=1.0)
        f5_latitude = st.number_input("Feature 5: Latitude", min_value=-90.0, max_value=90.0, value=0.0, step=1.0)

    elif selected_model == "Model 2":
        # feat1_pregnant = st.number_input("Feature 1: Pregnancies", min_value=0, max_value=25, value=1, step=1)
        # feat2_bps = st.number_input("Feature 2: Blood Pressure", min_value=0, max_value=200, value=80, step=1)
        # feat3_age = st.number_input("Feature 3: Age", min_value=1, max_value=120, value=30, step=1)
        # feat4_BMI = st.number_input("Feature 4: BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
        # feat5_glucose = st.number_input("Feature 5: Glucose Level", min_value=0, max_value=300, value=100, step=1)
        
        feat1_pregnant = st.number_input("Feature 1: Pregnancies", 
                                         min_value=0, max_value=25, 
                                         value=1, step=1, 
                                         help="Number of times pregnant")
        
        feat2_glucose = st.number_input("Feature 2: Glucose Level", 
                                        min_value=0, max_value=300, 
                                        value=100, step=1, 
                                        help="Plasma glucose concentration (mg/dL)")
        
        feat3_insulin = st.number_input("Feature 3: Insulin Level", 
                                        min_value=0, max_value=900, 
                                        value=80, step=1, 
                                        help="2-Hour serum insulin (mu U/ml)")
        
        feat4_BMI = st.number_input("Feature 4: BMI", 
                                    min_value=0.0, max_value=70.0, 
                                    value=25.0, step=0.1, 
                                    help="Body Mass Index (weight in kg/(height in m)^2)")
        
        feat5_DiabetesPedigree = st.number_input("Feature 5: Diabetes Pedigree Function",
                                                min_value=0.0, max_value=3.0,
                                                value=0.5, step=0.01,
                                                help="Diabetes pedigree function (genetic influence)")
        
        feat6_age = st.number_input("Feature 6: Age", 
                                   min_value=1, max_value=120, 
                                   value=30, step=1, 
                                   help="Age in years")
        
with col2:
    st.header("📈 Prediction Output")
    st.write("Model predictions will be displayed here.")
    
    predict_disabled = selected_model == "Model 2" and diabetes_model is None
    
    prediction_button = st.button("Analyze & Predict", 
                                  key="predict_button",
                                  help="Click to run the model prediction.",
                                  type="primary",
                                  width="stretch",
                                  icon="🚀",
                                  disabled=predict_disabled
                                  )
    
    if prediction_button:
        # st.status("Running prediction...")
        # time.sleep(2)  # Simulate prediction time
        # st.success("Prediction complete!")
        # st.write("Predicted Value: 42")  # Placeholder for actual prediction result
        # st.balloons()
        
        if selected_model == "Model 1":
            with st.status("Predicting...", expanded=True) as status:
                st.write("Analyzing input features...")
                time.sleep(1.5)
                st.write("Running model...")
                time.sleep(1)
                st.write("Finalizing results...")
                time.sleep(1)
                status.update(label="Done!", state="complete", expanded=False)
                

            # st.balloons()
            st.success("✅ Prediction complete!")

            st.metric("Predicted Value: ", "Placeholder")  # Placeholder for actual prediction result
            st.balloons()
        
        elif selected_model == "Model 2" and diabetes_model is not None:
            try:
                input_data = np.array([[feat1_pregnant, feat2_glucose, feat3_insulin, feat4_BMI, feat5_DiabetesPedigree, feat6_age]])
                
                with st.status("Predicting...", expanded=True) as status:
                    st.write("Analyzing patient data...")
                    time.sleep(1.5)
                    
                    prediction = diabetes_model.predict(input_data)
                    # prediction_proba = diabetes_model.predict_proba(input_data)
                    
                    st.write("Running diabetes risk assessment...")
                    time.sleep(1)
                    st.write("Finalizing results...")
                    time.sleep(1)
                    status.update(label="Analysis Complete!", state="complete", expanded=False)
                    
                st.success("✅ Diabetes risk prediction complete!")
                
                if prediction[0] == 1:
                    st.error("⚠️ High Risk of Diabetes")
                    risk_level = "High Risk!"
                else:
                    st.success("✅ Low Risk of Diabetes")
                    risk_level = "Low Risk!"
                    
                st.metric("Diabetes Prediction: ", risk_level)
            
            # Disclaimer
                st.info("⚕️ **Medical Disclaimer:** This prediction is for educational purposes only and should not replace professional medical advice. Please consult with a healthcare provider for proper diagnosis and treatment.")

            except Exception as e:
                st.error(f"Error during prediction: {e}")
                st.write("Please check the input values and try again.")

# Footer
st.markdown("---")
st.write("Developed by Shivansh Shukla :)")
st.markdown("💡 **Tip:** Models can make mistakes. Use predictions wisely!")
