# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 08:41:28 2021

@author: 91998
"""


import streamlit as st
from datetime import datetime
from google.cloud import firestore
import pandas as pd
import pytz

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestorekey.json")

user = st.selectbox( 'Please chose your login name', ( 'Bot', 'Chetan', 'Rajat', 'Sethu', 'Shivam', 'Havish', 'Utsav', 'Kshitiz' , 'Rajesh' ))
st.write('Welcome ', user, '  !')

tz_India = pytz.timezone('Asia/Calcutta') 
currtime = datetime.now(tz_India)
st.write("Current time: ", currtime.strftime("%H:%M:%S"))


df = pd.read_csv('IPLdata.csv')
print(df.head())

# Create a reference to the Google post.
doc_ref = db.collection("users").document("Chetan")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
