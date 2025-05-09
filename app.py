import streamlit as st
import pandas as pd
import random

# Load your CSV data
data_url = "https://raw.githubusercontent.com/imcarnochan/DjettMoves/main/moves.csv"
df = pd.read_csv(data_url)

st.title("Elemental Martial Arts Move Generator")

# Track last rolled moves
if 'last_moves' not in st.session_state:
    st.session_state['last_moves'] = pd.DataFrame()

# Function to display one move
def display_move(result, title):
    st.subheader(title)
    st.write(f"**Martial Art:** {result['Martial Art']}")
    st.write(f"**Move:** {result['Official Move Name']}")
    st.write(f"**Striking Limb:** {result['Striking Limb']}")
    st.write(f"**Speed:** {result['Speed (1–10)']}")
    st.write(f"**Power:** {result['Power (1–10)']}")
    st.write(f"**Element:** {result['Element']}")
    st.markdown(f"**Formal Move Name:** *{result['Formal Move Name']}*")

    flavor_texts = {
        "Weapon": "Forged in steel and sharpened in battle, this technique strikes with precision and mythic force.",
        "Grappling": "Twist, lock, and crash—this move seizes the body like a tidal surge of raw control.",
        "Unarmed": "A blur of fists and fury, born from breath, balance, and elemental mastery."
    }
    flavor = flavor_texts.get(result['Category'], "A mysterious force flows through this motion.")

    quotes = {
        "Weapon": [
            "Precision beats power. Timing beats speed.",
            "Strike with purpose, move with meaning.",
            "You swing a sword like a farmer with a hoe! — Mulan",
            "What we do in life echoes in eternity. — Gladiator",
            "The sword obeys the heart. — Hero",
        ],
        "Grappling": [
            "To yield is to conquer.",
            "Control the center, control the fight.",
            "Leverage breaks giants.",
            "It’s not about brute strength. It’s about angles. — John Wick",
            "Use their momentum against them. — Sherlock Holmes"
        ],
        "Unarmed": [
            "Be like water, my friend. — Bruce Lee",
            "Train until you cannot get it wrong.",
            "Boards don’t hit back. — Enter the Dragon",
            "The art of fighting without fighting. — Enter the Dragon",
            "You fight until the last breath. — Warrior"
        ]
    }

    category = result['Category']
    quote_pool = quotes.get(category, [])
    if quote_pool:
        quote = random.choice(quote_pool)
        st.caption(flavor)
        st.markdown(f"> _{quote}_")

# Buttons
if st.button("Roll Weapon Move"):
    result = df[df["Category"] == "Weapon"].sample(1).iloc[0]
    display_move(result, "Weapon Move")
    st.session_state['last_moves'] = pd.DataFrame([result])

if st.button("Roll Grappling Move"):
    result = df[df["Category"] == "Grappling"].sample(1).iloc[0]
    display_move(result, "Grappling Move")
    st.session_state['last_moves'] = pd.DataFrame([result])

if st.button("Roll One Unarmed Move"):
    result = df[df["Category"] == "Unarmed"].sample(1).iloc[0]
    display_move(result, "Unarmed Move")
    st.session_state['last_moves'] = pd.DataFrame([result])

if st.button("Roll Two Unarmed Moves"):
    results = df[df["Category"] == "Unarmed"].sample(2).reset_index(drop=True)
    st.session_state['last_moves'] = results
    for i, (_, result) in enumerate(results.iterrows(), 1):
        display_move(result, f"Unarmed Move {i}")

st.info("Click any button to generate a martial arts move!")

# Downloads
st.download_button(
    label="Download Full Move List as CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='moves.csv',
    mime='text/csv'
)

if not st.session_state['last_moves'].empty:
    st.download_button(
        label="Download Last Rolled Moves",
        data=st.session_state['last_moves'].to_csv(index=False).encode('utf-8'),
        file_name='last_moves.csv',
        mime='text/csv'
    )
