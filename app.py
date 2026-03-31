import streamlit as st

st.title("🎸 カートコバーン絵描き歌（無料版）")

name = st.text_input("名前を入れてね（カートコバーン）")

data = {
    "カートコバーン": {
        "features": ["長い髪", "眠そうな目", "ラフな雰囲気"],
        "song": [
            "まあるい顔をだるそうにかいて〜",
            "前にたらす長い髪をかぶせて〜",
            "ねむそうな目をちょこんとかいて〜",
            "力のぬけた顔にしたら〜",
            "ロックな気分でできあがり！"
        ],
        "svg": """
<svg width="200" height="200">
    <!-- 顔 -->
    <circle cx="100" cy="90" r="40" stroke="black" fill="none"/>

    <!-- 髪（前にかかる感じ） -->
    <line x1="50" y1="50" x2="150" y2="50" stroke="black"/>
    <line x1="60" y1="55" x2="140" y2="55" stroke="black"/>
    <line x1="70" y1="60" x2="130" y2="60" stroke="black"/>

    <!-- 目（眠そう） -->
    <line x1="80" y1="90" x2="95" y2="90" stroke="black"/>
    <line x1="105" y1="90" x2="120" y2="90" stroke="black"/>

    <!-- 口（やる気ない） -->
    <line x1="90" y1="110" x2="110" y2="110" stroke="black"/>

    <!-- ギター -->
    <rect x="70" y="130" width="60" height="25" stroke="black" fill="none"/>
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
        st.components.v1.html(item["svg"], height=220)

    else:
        st.write("カートコバーンって入力してね！")
