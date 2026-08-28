import streamlit as st

st.set_page_config(page_title="Negative Play % Calculator", page_icon="🏈")

st.title("🏈 Negative Play % Calculator")
st.write("Enter a quarterback's minus plays and total plays to calculate their Negative Play %.")

# --- Player input ---
player_name = st.text_input("Player Name (optional)")

col1, col2 = st.columns(2)
with col1:
    minus_plays = st.number_input("Minus Plays", min_value=0, step=1, value=0)
with col2:
    total_plays = st.number_input("Total Plays", min_value=0, step=1, value=0)

# --- Calculation ---
if st.button("Calculate Negative Play %"):
    if total_plays == 0:
        st.error("Total plays must be greater than 0.")
    elif minus_plays > total_plays:
        st.error("Minus plays can't be more than total plays.")
    else:
        negative_pct = (minus_plays / total_plays) * 100

        label = f"{player_name}'s Negative Play %" if player_name else "Negative Play %"
        st.metric(label=label, value=f"{negative_pct:.1f}%")

        # Optional: simple qualitative tier (lower is better here)
        if negative_pct <= 5:
            tier = "Excellent"
        elif negative_pct <= 10:
            tier = "Solid"
        elif negative_pct <= 15:
            tier = "Average"
        else:
            tier = "Needs Improvement"

        st.write(f"**Performance Tier:** {tier}")
        st.progress(min(int(negative_pct), 100))

        st.caption(f"{minus_plays} minus plays out of {total_plays} total plays")
