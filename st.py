import streamlit as st

data = st.text_input("Title")

st.write(data)

data = st.file_uploader("Fájl feltöltése")

if data is not None:
    st.code(f"""
    {data.getvalue().decode("utf-8")}
    """)

for i in range(1, 7):
    st.write(f"{i} - {i ** 2}")

l = [[4, 6, 3, 1],[1, 2, 3, 4], [5, 6, 7.2 ,2], [4, 7, 6.7 ,6], [6, 7, 5.3 ,5.8]]
edited=st.experimental_data_editor(l)
st.bar_chart(l)

img = st.camera_input("Cica")

st.snow()