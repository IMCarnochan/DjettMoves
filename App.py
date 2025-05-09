import streamlit as st
import pandas as pd
import random

# Load the move dataset from your GitHub repo
data_url = "https://raw.githubusercontent.com/imcarnochan/DjettMoves/main/moves.csv"
df = pd.read_csv(data_url)

st.title("Elemental Martial Arts Move Generator")

# Track last rolled moves
if 'last_moves' not in st.session_state:
    st.session_state['last_moves'] = pd.DataFrame()

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

    weapon_quotes = [  # (condensed list, continue in next cell)
        "Precision beats power. Timing beats speed.",
        "Strike with purpose, move with meaning.",
        "A true blade never boasts.",
        "The sword is the soul. Study it well.",
        "The edge remembers what the hand forgets.",
        "You swing a sword like a farmer with a hoe! — Mulan",
        "This is my boomstick! — Army of Darkness",
        "There can be only one. — Highlander",
        "What we do in life echoes in eternity. — Gladiator",
        "The pen is mightier, but the sword is swifter. — Anonymous",
        "You have no idea what I'm capable of. — The Last Samurai",
        "Do not fear the blade. Fear the one who wields it. — 47 Ronin",
        "I know kung fu. — The Matrix",
        "When you can snatch the pebble from my hand, it will be time for you to leave. — Kung Fu",
        "I fight because I must. — Crouching Tiger, Hidden Dragon",
        "To defeat your enemy, you must first understand him. — Star Wars",
        "I am the law. — Judge Dredd",
        "This is the way. — The Mandalorian",
        "The sword obeys the heart. — Hero",
        "You’ve taken your first step into a larger world. — Star Wars"
    ]
grappling_quotes = [
        "To yield is to conquer.",
        "Control the center, control the fight.",
        "Leverage breaks giants.",
        "Balance is the art of staying unthrown.",
        "Even water crushes stone in time.",
        "Ground game wins wars. — Warrior",
        "You either tap, snap, or nap. — BJJ maxim",
        "It’s not about brute strength. It’s about angles. — John Wick",
        "A good throw is silent. — Redbelt",
        "Let them come to you. — Ip Man",
        "Nobody hits harder than life. — Rocky Balboa",
        "You must learn control. — Star Wars",
        "I choose to fight. — The Last Airbender",
        "It’s not the size of the man in the fight, it’s the size of the fight in the man. — Rudy",
        "Pain is weakness leaving the body. — GI Jane",
        "Technique conquers strength. — Ong-Bak",
        "Grapple with the soul before the body. — The Legend of Bagger Vance",
        "You are not your failures. — Creed",
        "Adapt, improvise, overcome. — Heartbreak Ridge",
        "Use their momentum against them. — Sherlock Holmes"
    ]

unarmed_quotes = [
        "Be like water, my friend. — Bruce Lee",
        "A punch is a punch, a kick is a kick—until you master it.",
        "Train not until you get it right. Train until you cannot get it wrong.",
        "The body follows where the mind dares to go.",
        "Mastery is in the mundane. Discipline is the path.",
        "Man who catch fly with chopstick accomplish anything. — The Karate Kid",
        "Wax on, wax off. — The Karate Kid",
        "I don’t hit back. — Enter the Dragon",
        "Boards don’t hit back. — Enter the Dragon",
        "The art of fighting without fighting. — Enter the Dragon",
        "If you’re gonna learn to fight, learn to win. — Bloodsport",
        "Never underestimate your opponent. Expect the unexpected. — Road House",
        "No fear. No distractions. The ability to let that which does not matter truly slide. — Fight Club",
        "You have to let it all go. Fear, doubt, and disbelief. Free your mind. — The Matrix",
        "Don’t think, feel. — Bruce Lee",
        "It’s not about how hard you hit. It’s about how hard you can get hit and keep moving forward. — Rocky Balboa",
        "Stay down. Final warning. — Creed",
        "You fight until the last breath. — Warrior",
        "Only the disciplined ones in life are free. — Kenyan proverb",
        "You are stronger than you believe. — Wonder Woman"
    ]

category = result['Category']
if category == "Weapon":
    quote = random.choice(weapon_quotes)
elif category == "Grappling":
    quote = random.choice(grappling_quotes)
elif category == "Unarmed":
    quote = random.choice(unarmed_quotes)
else:
    quote = random.choice(weapon_quotes + grappling_quotes + unarmed_quotes)

st.caption(flavor)
st.markdown(f"> _{quote}_")
# Buttons and display
if st.button("Roll Weapon Move"):
    result = df[df["Category"] == "Weapon"].sample(1).iloc[0]
    display_move(result, "Weapon Move")
    st.session_state['last_moves'] = 
pd.DataFrame([result])

if st.button("Roll Grappling Move"):
    result = df[df["Category"] == "Grappling"].sample(1).iloc[0]
    display_move(result, "Grappling Move")
    st.session_state['last_moves'] = 
pd.DataFrame([result])

if st.button("Roll One Unarmed Move"):
    result = df[df["Category"] == "Unarmed"].sample(1).iloc[0]
    display_move(result, "Unarmed Move")
    st.session_state['last_moves'] = 
pd.DataFrame([result])

if st.button("Roll Two Unarmed Moves"):
    results = df[df["Category"] == "Unarmed"].sample(2)
    st.session_state['last_moves'] = results.reset_index(drop=True)
for i, (_, result) in enumerate(results.iterrows(), 1):
    display_move(result, f"Unarmed Move {i}")

st.info("Click any button to generate a martial arts move!")

# Download full dataset
st.download_button(
    label="Download Full Move List as CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='moves.csv',
    mime='text/csv'
)

# Download last rolled moves
if st.session_state['last_moves'].shape[0] > 0:
    st.download_button(
        label="Download Last Rolled Moves",
        data=st.session_state['last_moves'].to_csv(index=False).encode('utf-8'),
        file_name='last_moves.csv',
        mime='text/csv'
    )
