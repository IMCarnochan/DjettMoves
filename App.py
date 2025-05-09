import streamlit as st 
import pandas as pd 
import random

# Load pre-generated data (insert your own if running outside ChatGPT)

data_url = "https://raw.githubusercontent.com/imcarnochan/DjettMoves/main/moves.csv"

# For this example, we simulate the dataframe

df = pd.DataFrame({ "Category": ["Weapon", "Grappling", "Unarmed"] * 10, "Martial Art": ["Kendo", "Schwingen", "Boxing"] * 10, "Official Move Name": ["Kote Strike", "Swing Toss", "Overhand"] * 10, "Striking Limb": ["Weapon Arm", "Full Body", "Palm"] * 10, "Speed (1–10)": [8, 10, 6] * 10, "Power (1–10)": [9, 5, 6] * 10, "Element": ["Acid", "Lightning", "Fire"] * 10, "Formal Move Name": ["Beholder's Parry Kote Strike", "Basilisk's Combo Swing Toss", "Gorgon's Feint Overhand"] * 10 })

st.title("Rollin up some Djett Moves! Djett Moves")

def display_move(move, title): st.subheader(title) 
st.write(f"Martial Art: {move['Martial Art']}") 
st.write(f"Move: {move['Official Move Name']}") 
st.write(f"Striking Limb: {move['Striking Limb']}") 
st.write(f"Speed: {move['Speed (1–10)']}") 
st.write(f"Power: {move['Power (1–10)']}") 
st.write(f"Element: {move['Element']}") 
st.markdown(f"Formal Move Name: {move['Formal Move Name']}")

if st.button("Roll Weapon Attack"): move = df[df["Category"] == "Weapon"].sample(1).iloc[0] 
display_move(move, "Weapon Move")

if st.button("Roll Grapple"): move = df[df["Category"] == "Grappling"].sample(1).iloc[0] 
display_move(move, "Grappling Move")

if st.button("Roll Unarmed Attack"): move = df[df["Category"] == "Unarmed"].sample(1).iloc[0] 
display_move(move, "Unarmed Move")

if st.button("Roll Flurry of Blows"): moves = df[df["Category"] == "Unarmed"].sample(2) for i, (_, move) in enumerate(moves.iterrows(), 1): 
display_move(move, f"Unarmed Move {i}")

st.info("Click any button to see what Djett does!")

