import streamlit as st
from db import get_connection, wait_for_db, init_db

st.title("User Input")

# Ensure DB is ready
wait_for_db()
init_db()

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Save"):
    if name and email:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        conn.close()
        st.success("Data saved successfully!")
    else:
        st.warning("Please enter both name and email.")