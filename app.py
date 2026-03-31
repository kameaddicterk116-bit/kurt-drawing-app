import streamlit as st

st.title("🎸 カートコバーン絵描き歌（ちょいリアル）")

name = st.text_input("名前を入れてね（カートコバーン）")

data = {
    "カートコバーン": {
        "features": ["長い髪", "少し細い顔", "眠そうな目"],
        "song": [
            "たまごみたいな顔をかいて〜",
            "上から長い髪を流すようにかいて〜",
            "ねむそうな目をすこしズラしてかいて〜",
            "口を軽くひいたら〜",
            "ロックな雰囲気でできあがり！"
        ],
        "svg": """
<svg width="200" height="220">

    <!-- 顔（少し縦長） -->
    <ellipse cx="100" cy="110" rx="40" ry="50" stroke="black" fill="none"/>

    <!-- 髪（流れ） -->
    <line x1="60" y1="50" x2="80" y2="160" stroke="black"/>
    <line x1="80" y1="50" x2="100" y2="170" stroke="black"/>
    <line x1="100" y1="50" x2="120" y2="165" stroke="black"/>
    <line x1="120" y1="50" x2="140" y2="160" stroke="black"/>

    <!-- 目 -->
    <line x1="80" y1="110" x2="95" y2="108" stroke="black"/>
    <line x1="105" y1="115" x2="120" y2="115" stroke="black"/>

    <!-- 口 -->
    <line x1="90" y1="140" x2="110" y2="142" stroke="black"/>

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
        st.components.v1.html(item["svg"], height=240)

    else:
        st.write("カートコバーンって入力してね！")
