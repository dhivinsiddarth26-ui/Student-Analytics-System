import streamlit as st
import pandas as pd
from db_connection import get_connection

st.title("Student Analytics Dashboard")

conn = get_connection()

query = "SELECT id, name, age, city, course_id FROM students"
df = pd.read_sql(query, conn)

st.subheader("Student Data")
st.write(df)

st.subheader("Average Age")
st.write(df["age"].mean())

st.subheader("Students per City")
city_count = df["city"].value_counts()
st.bar_chart(city_count)

conn.close()