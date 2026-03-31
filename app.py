import streamlit as st

st.title("🎸 表示テスト")

name = st.text_input("名前を入れてね")

if st.button("生成する"):

    st.write("🖼 イラスト")

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3d/Kurt_Cobain_1992.jpg")
