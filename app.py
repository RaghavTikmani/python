import streamlit as st
import json

st.set_page_config(page_title="MUBI Demo", layout="wide")

# Load movie data
with open("movies.json", "r", encoding="utf-8") as f:
    movies = json.load(f)

st.title("🎬 MUBI — curated cinema, Streamlit demo")

# Featured movie (first in list)
featured = movies[0]

st.subheader("⭐ Featured Film")
col1, col2 = st.columns([1, 2])

with col1:
    st.image(featured["poster"], use_column_width=True)

with col2:
    st.markdown(f"## {featured['title']} ({featured['year']})")
    st.markdown(f"**Director:** {featured['director']}")
    st.write(featured["description"])
    st.button("Watch Now")

st.markdown("---")

# Catalog section
st.subheader("📚 Film Catalogue")

cols = st.columns(3)

for idx, movie in enumerate(movies):
    with cols[idx % 3]:
        st.image(movie["poster"], use_column_width=True)
        st.markdown(f"### {movie['title']}")
        st.write(f"{movie['year']} — {movie['director']}")
        st.caption(movie["description"])
        st.button(f"View details", key=f"details_{idx}")
