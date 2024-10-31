import streamlit as st
import requests

# Define the FastAPI endpoint URL
API_URL = 'https://api-913491001221.europe-west1.run.app/predict'

# Streamlit app
def main():
    st.title("Heart Disease Prediction")
    
    # Sidebar for input data
    st.sidebar.header("Input Data")
    
    age = st.sidebar.number_input("Age", min_value=0, value=50)  # Défault 50 ans
    sex = st.sidebar.selectbox("Sex", [0, 1], index=1)  # Défault homme car classe majoritaire
    dataset = st.sidebar.text_input("Dataset", value="Cleveland")  # Cleveland
    cp = st.sidebar.selectbox("CP", [1, 2, 3, 4], index=0)  # Défault 1
    trestbps = st.sidebar.number_input("Trestbps", min_value=0.0, value=120.0) 
    chol = st.sidebar.number_input("Chol", min_value=0.0, value=200.0)  
    fbs = st.sidebar.checkbox("Fbs", value=False)
    restecg = st.sidebar.selectbox("Restecg", ["normal", "lv hypertrophy", "st-t abnormality"], index=0)  # ATTENTION ABNORMAL
    thalch = st.sidebar.number_input("Thalch", min_value=0.0, value=120.0)  
    exang = st.sidebar.checkbox("Exang", value=False) 
    oldpeak = st.sidebar.number_input("Oldpeak", min_value=0.0, value=0.0)  
    slope = st.sidebar.selectbox("Slope", ["flat", "upsloping", "downsloping"], index=0)
    ca = st.sidebar.number_input("Ca", min_value=0.0, value=0.0)  # Default to 0.0
    thal = st.sidebar.selectbox("Thal", ["normal", "reversable defect", "fixed defect"], index=0)  # Default to "normal"
    
    # Submit button
    if st.sidebar.button("Submit"):
        # Prepare the payload
        payload = {
            'age': age,
            'sex': sex,
            'dataset': dataset,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalch': thalch,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope' : slope,
            'ca': ca,
            'thal': thal,
        }
        
        # Send the request to the API
        response = requests.get(API_URL, params=payload)
        
        # Display the prediction
        if response.status_code == 200:
            prediction = response.json().get('prediction')
            st.write(f"Prediction: {prediction}")
        else:
            st.write("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
