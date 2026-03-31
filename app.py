import streamlit as st

st.title("🎸 カートコバーン絵描き歌（限界版）")

name = st.text_input("名前を入れてね（カートコバーン）")

data = {
    "カートコバーン": {
        "features": ["顔にかかる長い髪", "左右ズレた眠そうな目", "やる気ない表情"],
        "song": [
            "ズレた丸をだるくかいて〜",
            "顔にかぶさる髪をバサバサ落として〜",
            "左右ちがうねむそうな目をいれて〜",
            "ちょっと曲がった口をかいたら〜",
            "ロックな脱力でできあがり！"
        ],
        "svg": """
<svg width="220" height="220">

    <!-- 髪（大量・ランダム風） -->
    <line x1="20" y1="30" x2="80" y2="120" stroke="black"/>
    <line x1="40" y1="20" x2="100" y2="130" stroke="black"/>
    <line x1="60" y1="25" x2="120" y2="140" stroke="black"/>
    <line x1="80" y1="30" x2="140" y2="130" stroke="black"/>
    <line x1="100" y1="20" x2="160" y2="140" stroke="black"/>
    <line x1="120" y1="30" x2="180" y2="120" stroke="black"/>
    <line x1="140" y1="25" x2="190" y2="130" stroke="black"/>

    <!-- 顔（ズレ） -->
    <circle cx="115" cy="110" r="45" stroke="black" fill="none"/>

    <!-- 目（非対称） -->
    <line x1="85" y1="105" x2="100" y2="103" stroke="black"/>
    <line x1="120" y1="110" x2="140" y2="112" stroke="black"/>

    <!-- 眉（適当） -->
    <line x1="85" y1="95" x2="100" y2="93" stroke="black"/>
    <line x1="120" y1="100" x2="140" y2="98" stroke="black"/>

    <!-- 口（歪み） -->
    <line x1="95" y1="135" x2="125" y2="140" stroke="black"/>

    <!-- 首 -->
    <line x1="105" y1="155" x2="105" y2="175" stroke="black"/>
    <line x1="125" y1="155" x2="125" y2="175" stroke="black"/>

    <!-- ギター（ラフ） -->
    <rect x="70" y="175" width="80" height="25" stroke="black" fill="none"/>

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
