import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="סימולטור טיטרציה", layout="wide")

with open("simulator.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1100, scrolling=True)
