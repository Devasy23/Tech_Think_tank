from tkinter import HORIZONTAL, OptionMenu
import streamlit as st
st.set_page_config(layout="wide")

# with open("styles.css") as f:
    # st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

import pyrebase
import streamlit as st
from datetime import datetime
import json
from firebase_admin import credentials,firestore

#Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyBSKjGpX9DMdnRxy_WwZBW3NpJcyySdtro",
    'authDomain': "automated-inventory-ab4a2.firebaseapp.com",
    'projectId': "automated-inventory-ab4a2",
    'databaseURL': "https://automated-inventory-ab4a2-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'storageBucket': "automated-inventory-ab4a2.appspot.com",
    'messagingSenderId': "291072185162",
    'appId': "1:291072185162:web:86222e93eb060524ada7b3"
}

#Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#Databases
db = firebase.database()
storage = firebase.storage()

if 'key' not in st.session_state:
    st.session_state['key'] = False
if(st.session_state['key'] != True):

    st.title("Welcome to Automated Inventory Management System!")
    c1, c2, c3 = st.columns(3)
    col1, col2, col3 = st.columns([1, 4, 1])
    choice = st.selectbox("Login",["Login", "Signup"])
    # choice = OptionMenu("Login",["Login", "Signup"])
    if choice=='Signup':
        email = st.text_input('Please enter your email id: ')
        password = st.text_input('Please enter your password: ')
        submit = st.sidebar.button('Create my Account')
        if submit:
            user = auth.create_user_with_email_and_password(email,password)
            st.success('Your Account is created successfully!')
            st.balloons()
    if (choice == "Login"):
        email = st.text_input('Please enter your email id: ')
        password = st.text_input('Please enter your password: ')
        if st.button("Login"):
            try:
                user = auth.sign_in_with_email_and_password(email,password)
                st.session_state['key'] = True
            except:
                st.title("Invalid password entered")
else:
    st.title("Welcome")
    db.update({
        "Papercups": 5,
        "Laptop": 1
    })
    users = db.child().get()
    st.write(users.val())