import streamlit as st
import time

# Configure page
st.set_page_config(
    page_title="ML Prediction App",
    page_icon="🤖",
    layout="wide"
)

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
        f1_pregnant = st.number_input("Feature 1: Pregnancies", min_value=0, max_value=25, value=1, step=1)
        f2_bps = st.number_input("Feature 2: Blood Pressure", min_value=0, max_value=200, value=80, step=1)
        f3_age = st.number_input("Feature 3: Age", min_value=1, max_value=120, value=30, step=1)
        f4_BMI = st.number_input("Feature 4: BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)

with col2:
    st.header("📈 Prediction Output")
    st.write("Model predictions will be displayed here.")
    prediction_button = st.button("Analyze & Predict", 
                                  key="predict_button",
                                  help="Click to run the model prediction.",
                                  type="primary",
                                  width="stretch",
                                  icon="🚀"
                                  )
    
    if prediction_button:
        # st.status("Running prediction...")
        # time.sleep(2)  # Simulate prediction time
        # st.success("Prediction complete!")
        # st.write("Predicted Value: 42")  # Placeholder for actual prediction result
        # st.balloons()
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
        
        
    

# Footer
st.markdown("---")
st.write("Developed by Shivansh Shukla :)")
st.markdown("💡 **Tip:** Models can make mistakes. Use predictions wisely!")


def select_model():
    pass