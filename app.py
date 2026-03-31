import streamlit as st
import base64

st.title("🎸 カートコバーン絵描き歌（完全表示版）")

name = st.text_input("名前を入れてね（カートコバーン）")

svg_data = """
<svg xmlns="http://www.w3.org/2000/svg" width="220" height="240" viewBox="0 0 220 240">

    <!-- 髪 -->
    <path d="M40,80 C60,20 160,20 180,80 
             C160,70 140,90 120,85 
             C100,80 80,100 60,85 
             C50,80 45,90 40,80"
          stroke="black" fill="none"/>

    <!-- 顔 -->
    <path d="M70,100 
             C70,160 150,160 150,100
             C150,60 70,60 70,100"
          stroke="black" fill="none"/>

    <!-- 前髪 -->
    <path d="M90,60 C85,120 95,180 100,200" stroke="black" fill="none"/>
    <path d="M110,60 C105,130 115,190 120,200" stroke="black" fill="none"/>

    <!-- 目 -->
    <path d="M90,110 Q100,108 105,110" stroke="black" fill="none"/>
    <path d="M115,115 Q125,115 130,117" stroke="black" fill="none"/>

    <!-- 口 -->
    <path d="M95,140 Q110,145 120,142" stroke="black" fill="none"/>

</svg>
"""

# SVGを画像化
def svg_to_base64(svg):
    return base64.b64encode(svg.encode('utf-8')).decode('utf-8')

if st.button("生成する"):

    if name == "カートコバーン":

        st.write("🧠 特徴")
        st.write("- 顔にかかる長い髪")
        st.write("- 眠そうな目")

        st.write("🎵 絵描き歌")
        st.write("たまごみたいな顔をかいて〜")
        st.write("上から髪をふわっとかぶせて〜")
        st.write("前に落ちる髪を2本たして〜")
        st.write("ねむそうな目をさらっとかいて〜")
        st.write("力のぬけた口でできあがり！")

        st.write("🖼 イラスト")

        img = svg_to_base64(svg_data)
        st.markdown(f'<img src="data:image/svg+xml;base64,{img}"/>', unsafe_allow_html=True)

    else:
        st.write("カートコバーンって入力してね！")
