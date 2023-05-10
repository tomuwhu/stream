import streamlit as st
import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

s1 = st.text_input("Filmcím")
n1 = st.number_input("Megjelenés éve", min_value=1900, max_value=2023, value=2000, step=1)
n2 = st.number_input("IMDB Score", min_value=0, max_value=10, value=5.0, step=0.1)

if st.button("Rögzít"):
    cur.execute(f"INSERT INTO movie VALUES ('{s1}', {n1}, {n2})")
    con.commit()

if st.button("Töröl mind"):
    cur.execute(f"DELETE FROM movie")
    con.commit()

res = cur.execute("SELECT * FROM movie")

a = res.fetchall()

a
