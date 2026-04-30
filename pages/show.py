import streamlit as st
import pandas as pd
from db import get_connection, wait_for_db

st.title("Stored Data")

wait_for_db()

conn = get_connection()
df = pd.read_sql("SELECT * FROM users", conn)
conn.close()

st.dataframe(df)