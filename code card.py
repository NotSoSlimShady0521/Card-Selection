import streamlit as st

# Function to display selected cards
def display_selected_cards(selected_cards):
    if selected_cards:
        st.write(f"Selected Cards: {', '.join(selected_cards)}")
    else:
        st.write("No cards selected.")

# List of poker cards (simplified to just ranks and suits)
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Generate all possible cards
deck_of_cards = [f"{rank} of {suit}" for rank in ranks for suit in suits]

# Create checkboxes for each card
selected_cards = []
st.title("Select and Deselect Poker Cards")

for card in deck_of_cards:
    selected = st.checkbox(card)
    if selected:
        selected_cards.append(card)

# Display the selected cards
display_selected_cards(selected_cards)
