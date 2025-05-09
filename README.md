# DjettMoves: Elemental Martial Arts Move Generator

A fantasy-inspired martial arts move generator built with Streamlit. Each move draws from real-world martial arts and is assigned an elemental flair and a legendary creature name to form a unique, flavorful technique.

## Features

- Generate randomized martial arts moves by category:
  - Weapon-based
  - Grappling-based
  - Unarmed (1 or 2 at a time)
- Each move includes:
  - Martial art origin
  - Realistic technique name
  - Speed and power ratings (1–10)
  - Elemental type (Fire, Acid, Lightning, etc.)
  - A fantasy-styled formal name (e.g. *“Beholder’s Parry Kote Strike”*)

## How to Use

This app runs on [Streamlit Cloud](https://streamlit.io/cloud).

To try it:

1. Visit: [https://djettmoves.streamlit.app](https://djettmoves.streamlit.app)
2. Click any button to generate cool new moves!
3. Get inspired for D&D, writing, game design, or just martial arts fun.

## Run Locally

### Requirements
- Python 3.7+
- `streamlit`, `pandas`

### Setup

```bash
git clone https://github.com/imcarnochan/DjettMoves.git
cd DjettMoves
pip install -r requirements.txt  # or just install pandas and streamlit
streamlit run app.py
