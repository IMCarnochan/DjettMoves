import streamlit as st
import pandas as pd

# Load the move dataset from your GitHub repo
data_url = "https://raw.githubusercontent.com/imcarnochan/DjettMoves/main/moves.csv"
df = pd.read_csv(data_url)

st.title("Clickin up some Djett Moves! Djett Moves!!!")

def display_move(result, title):
    st.subheader(title)
    st.write(f"**Martial Art:** {result['Martial Art']}")
    st.write(f"**Move:** {result['Official Move Name']}")
    st.write(f"**Striking Limb:** {result['Striking Limb']}")
    st.write(f"**Speed:** {result['Speed (1–10)']}")
    st.write(f"**Power:** {result['Power (1–10)']}")
    st.write(f"**Element:** {result['Element']}")
    st.markdown(f"**Formal Move Name:** *{result['Formal Move Name']}*")

if st.button("You call that a knife?"):
    result = df[df["Category"] == "Weapon"].sample(1).iloc[0]
    display_move(result, "Weapon Move")

if st.button("Wrasslin'"):
    result = df[df["Category"] == "Grappling"].sample(1).iloc[0]
    display_move(result, "Grappling Move")

if st.button("Attack!"):
    result = df[df["Category"] == "Unarmed"].sample(1).iloc[0]
    display_move(result, "Unarmed Move")

if st.button("Flurry of Blows"):
    results = df[df["Category"] == "Unarmed"].sample(2)
    for i, (_, result) in enumerate(results.iterrows(), 1):
        display_move(result, f"Strike {i}")

st.info("Click any button to make Djett dance!")
