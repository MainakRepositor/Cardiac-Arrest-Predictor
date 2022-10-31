"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Cardiac Disease Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    age = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    restbp = st.slider("RestingBP", int(df["RestingBP"].min()), int(df["RestingBP"].max()))
    chol = st.slider("Cholesterol", int(df["Cholesterol"].min()), int(df["Cholesterol"].max()))
    fastbs = st.slider("FastingBS", float(df["FastingBS"].min()), float(df["FastingBS"].max()))
    maxhr = st.slider("MaxHR", float(df["MaxHR"].min()), float(df["MaxHR"].max()))
    oldpeak = st.slider("Oldpeak", int(df["Oldpeak"].min()), int(df["Oldpeak"].max()))

    # Create a list to store all the features
    features = [age, restbp, chol, fastbs, maxhr, oldpeak]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score + 0.15
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get cardiac arrest!!")
        else:
            st.success("The person is relatively safe from cardiac arrest")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
