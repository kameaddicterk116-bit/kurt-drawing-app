import streamlit as st

st.title("絵描き歌ジェネレーター")

name = st.text_input("名前を入れてね")

data = {
    "カートコバーン": {
        "features": ["長い髪", "ぼんやりした目", "ギター"],
        "song": [
            "まあるい顔をひとつかいて〜",
            "ふわっと長い髪をのせて〜",
            "ちょっとぼんやりした目をかいて〜",
            "ギターをそっと持たせたら〜",
            "ロックな気分でできあがり！"
        ],
        "svg": """
        <svg width="200" height="200">
            <circle cx="100" cy="90" r="40" stroke="black" fill="none"/>
            <line x1="60" y1="60" x2="140" y2="60" stroke="black"/>
            <line x1="50" y1="70" x2="150" y2="70" stroke="black"/>
            <circle cx="85" cy="90" r="3" fill="black"/>
            <circle cx="115" cy="90" r="3" fill="black"/>
            <rect x="70" y="130" width="60" height="30" stroke="black" fill="none"/>
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
