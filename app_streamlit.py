import streamlit as st
import pickle
import time

model=open('svc.pkl','rb')
classifier=pickle.load(model)
standard_scaler=open('Scaler.pkl','rb')
scaler=pickle.load(standard_scaler)

def predict_note_authentication(variance, skewness, curtosis, entropy):
    scaling = scaler.transform([[variance, skewness, curtosis, entropy]])
    prediction=classifier.predict(scaling)
    if prediction[0] == 0:
        return 'It is an Authentic Note'
    else:
        return "It is a fake note"


def predict():
    st.markdown("<h1 style='text-align: center; color: black;'>Bank Note Authentication</h1>", unsafe_allow_html=True)
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)
    """
    
    
    """
    variance = st.number_input("Variance")
    skewness = st.number_input("Skewness")
    curtosis = st.number_input("Curtosis")
    entropy = st.number_input("Entropy")
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        with st.spinner(text='In progress'):
            time.sleep(5)
            st.success(result)

if __name__=='__main__':
    predict()
