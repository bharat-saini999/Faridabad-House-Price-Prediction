import joblib
import streamlit as st

model_loaded=joblib.load("C:\\Users\\Hp\\Downloads\\model.pickle")

def Predict_no(my_list):
    prediction = model_loaded.predict([my_list])
    return prediction



st.title("Faridabad House Price Prediction")

left, right = st.columns(2)   
with left:
    area = st.number_input("Enter area in Sq. m", max_value=99999, step=1)
        
    bath = st.radio("Select no. of Bathrooms",[1,2,3,4,5], horizontal=True)

with right:
    locality = st.selectbox("Select the location: ",["Greater Faridabad","Old Faridabad","New Industrial Town","Ballabgarh","Village Area"], placeholder="Hello")
    if locality == "Ballabgarh":
        locality_list = [1, 0, 0, 0, 0]
    elif locality == "Greater Faridabad":
        locality_list = [0, 1, 0, 0, 0]
    elif locality == "New Industrial Town":
        locality_list = [0, 0, 1, 0, 0]
    elif locality == "Old Faridabad":
        locality_list = [0, 0, 0, 1, 0]
    elif locality == "Village Area":
        locality_list = [0, 0, 0, 0, 1]
    else:
        locality_list = [0, 0, 0, 0, 0]

    bhk = st.radio("Select No. of BHK",[1,2,3,4,5], horizontal=True)

st.write("You have selected ",area,"Sq. m at ", locality," location which has ", bhk," bhk and ",bath," bathrooms.")

input = [area,bath, bhk]
input=input+locality_list
result = Predict_no(input)
result = abs(int(result * area * 1000))

if st.button("Predict"):
    st.success("The output is ₹ {:,}".format(result),icon="✅")

st.subheader("CREATED BY BHARAT SAINI")
