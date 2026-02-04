import streamlit as st
import subprocess
import os
import send_to_gsheets

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
            st.success("Data exported as data.json, push data to Google Sheets using the below button.", icon = "✅")
    else:
        st.warning("Please enter a URL.")

if st.button("Push to GSheets"):
    result = send_to_gsheets.core_operations()
    if (result == "success"):
        st.success("Data sent to Google Sheets successfully!", icon = "✅")
    else:
        st.error(result)