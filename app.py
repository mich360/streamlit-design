from PIL import Image
import requests
import streamlit as st
import json

st.set_page_config(page_title="MY webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# CSSファイルのロード
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./style/style.css")

# LottieアニメーションのURLをロード
lottie_url = "https://assets7.lottiefiles.com/packages/lf20_bP3BLu.json"
lottie_data = load_lottieurl(lottie_url)

with st.container():
    st.subheader("どうも👋")
    st.title("やっと最近Pythonを始めました")
    st.write("プログラムを効率よく活用することに情熱を持ち続けたいと思います。")
    st.write("[こちらを参考にしました >](https://pythonandvba.com)")

with st.container():
    st.write("---") 
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")  
        st.write("##") 
        st.write(
            """
            Pythonでスタイルを設定する方法は:
            - CSSでデザインを適用するには.
            - アニメーションをウェブに上げるには.
            - 画像・動画を載せるには.
            - メールを適用するには.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st.write('右カラム、アニメーションをここに製作中')

with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(Image.open("images/ch.jpg"))
    with text_column:
        st.subheader("アニメーションとStreamlitをインテグレーションする")
        st.write(
            """
            StreamlitでLottieファイルを使用する方法を学びましょう！
            アニメーションはWebアプリをより魅力的で楽しいものにします。
            Lottie Filesはそれを行う最も簡単な方法です。
            このチュートリアルでは、その方法を正確に説明しています。
            """
        )
        st.markdown("[参考 Video...](https://youtu.be/TXSOitGoINE)")

with st.container():
    image_column, text_column = st.columns((1, 2))  
    with image_column:
        st.image(Image.open("images/mail.jpg"))
    
    with text_column:
       
