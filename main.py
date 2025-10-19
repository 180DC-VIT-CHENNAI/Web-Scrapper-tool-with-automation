import streamlit as st
import subprocess
import os

st.title("Web Scrapper Interface")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    if url:
        # Run the JS script with the URL as an argument
        result = subprocess.run([
        "node", "scrapper.js", url
        ], capture_output=True, text=True, encoding="utf-8")
        st.write("Output:")
        st.code(result.stdout)
        if result.stderr:
            st.error(result.stderr)
    else:
        st.warning("Please enter a URL.")
