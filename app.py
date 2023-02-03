import streamlit as st
from word_gen import generate_word_list

st.set_page_config('Word Generator', layout="wide")

vowels = st.text_input("Vowels")
consonants = st.text_input("Consonants")

pattern = st.text_input("Pattern")

syllables = st.number_input("Syllables", min_value=0)
word_list = st.number_input("Words Output", min_value=0)


gen_button = st.button("Generate")

if gen_button:
    col1, col2 = st.columns(2)
    result = generate_word_list(
        word_list, syllables, vowels=vowels, consonants=consonants, pattern=pattern)
    with col1:
        st.json(result)
    with col2:
        st.info(len(result))
