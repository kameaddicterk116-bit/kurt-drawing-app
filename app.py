import streamlit as st

st.title("🎸 カートコバーン絵描き歌（表示修正版）")

name = st.text_input("名前を入れてね（カートコバーン）")

data = {
    "カートコバーン": {
        "features": ["顔にかかる長い髪", "眠そうな目", "ラフな雰囲気"],
        "song": [
            "たまごみたいな顔をかいて〜",
            "上から髪をふわっとかぶせて〜",
            "前に落ちる髪を2本たして〜",
            "ねむそうな目をさらっとかいて〜",
            "力のぬけた口でできあがり！"
        ],
        "svg": """
<svg width="220" height="240" viewBox="0 0 220 240">

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
    }
}

if st.button("生成する"):

    if name == "カートコバーン":

        item = data[name]

        st.write("🧠 特徴")
        for f in item["features"]:
            st.write("-", f)

        st.write("🎵 絵描き歌")
        for line in item["song"]:
            st.write(line)

        st.write("🖼 イラスト")
        st.components.v1.html(item["svg"], height=260)

    else:
        st.write("カートコバーンって入力してね！")
