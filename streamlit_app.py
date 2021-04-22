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

tz_India = pytz.timezone('Asia/Calcutta') 
currtime = datetime.now(tz_India)

df = pd.read_csv('IPLdata.csv', parse_dates= ['Time'])
s = pd.to_datetime(df['Time'])
df['Time1'] = s.dt.tz_localize('Asia/Calcutta')
dftemp = df[df["Time1"] > currtime ]
row = dftemp.iloc[0]
print(row['Team1'])

st.write( "Welcome! Please submit you response for ", row['Team1'], " v/s", row['Team2'], " match at ", row['Time'])

players = ( 'Bot', 'Chetan', 'Rajat', 'Sethu', 'Shivam', 'Havish', 'Utsav', 'Kshitiz' , 'Rajesh' )
user = st.selectbox( 'Please chose your login name', players )

team_selected = st.selectbox( 'Please chose your team', ( 'None', row['Team1'], row['Team2'] ))                                                  

doc_ref = db.collection("users").document(user)
submit = st.button('Submit Response')

if submit: 
  doc_ref.update( {row['MatchId']: team_selected } )
  st.write('Your response has been submitted, good luck!')

choicedict = {}
for player in players:
  tempdoc_ref = db.collection("users").document(player)
  tempdoc = doc_ref.get()
  try:
    choicedict.update( {player, tempdoc.to_dict()[row['MatchId']]})
  except:
    print("ignore error")
                                                        
if len(choicedict) > 0:
  st.write(choicedict)
                                                 
  
