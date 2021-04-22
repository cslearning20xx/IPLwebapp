# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 08:41:28 2021

@author: 91998
"""


import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("firestorekey.json")

# Create a reference to the Google post.
doc_ref = db.collection("users").document("Chetan")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())
