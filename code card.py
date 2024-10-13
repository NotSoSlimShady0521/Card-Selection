import streamlit as st
streamlit run poker_card_selector.py

# Function to display selected cards
def display_selected_cards(selected_cards):
    if selected_cards:
        st.write(f"Selected Cards: {', '.join(selected_cards)}")
    else:
        st.write("No cards selected.")

# List of poker cards (ranks and suits)
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Generate the deck of poker cards
deck_of_cards = [f"{rank} of {suit}" for rank in ranks for suit in suits]

# Create a sidebar for the card selection process
st.sidebar.title("Poker Card Selector")
st.sidebar.write("Select or deselect your poker cards below:")

# Create checkboxes for each card in the sidebar
selected_cards = []
for card in deck_of_cards:
    if st.sidebar.checkbox(card):
        selected_cards.append(card)

# Main section displaying selected cards
st.title("Poker Card Selection App")
st.write("Use the checkboxes in the sidebar to select or deselect cards.")
display_selected_cards(selected_cards)

# Option to clear all selections
if st.button("Clear Selections"):
    st.caching.clear_cache()
    st.experimental_rerun()
