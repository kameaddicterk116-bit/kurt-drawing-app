import streamlit as st

st.title("🔥絶対変わるテスト🔥")

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
    <!-- 髪（塊で強調） -->
    <rect x="40" y="40" width="120" height="40" stroke="black" fill="none"/>

    <!-- 顔 -->
    <circle cx="100" cy="100" r="40" stroke="black" fill="none"/>

    <!-- 目（かなり眠そう） -->
    <line x1="75" y1="100" x2="95" y2="100" stroke="black"/>
    <line x1="105" y1="100" x2="125" y2="100" stroke="black"/>

    <!-- 口 -->
    <line x1="90" y1="120" x2="110" y2="120" stroke="black"/>

    <!-- ギター -->
    <rect x="70" y="140" width="60" height="20" stroke="black" fill="none"/>
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
