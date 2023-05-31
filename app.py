from PIL import Image
import requests
import streamlit as st
# from streamlit_lottie import st_lottie



st.set_page_config(page_title="MY webpage”, page_icon=“:tada”, layout=“wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("./style/style.css")


lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bP3BLu.json")
img_contact_form = Image.open("images/mail.jpg")
img_lottie_animation = Image.open("images/ch.jpg")


with st.container():
    st.subheader("どうも:wave:")
    st.title("やっと最近pythonを始めました")
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
            pythonでスタイルを設定する方法は:
            - cssでデザインを適用するには .
            - アニメーションをウェブに上げるには .
            - 画像・動画を載せるには.
            - メールを適用するには.

            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")  

 # ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("アニメーションとStreamlitをインテグレーション する")
        st.write(
            """
            Streamlit で Lottie ファイルを使用する方法を学びましょう! 
            アニメーションは Web アプリをより魅力的で楽しいものにします。
            Lottie Files はそれを行う最も簡単な方法です。 
            このチュートリアルでは、その方法を正確に説明しています。
            """
        )
        st.markdown("[参考 Video...](https://youtu.be/TXSOitGoINE)")    
with st.container():
    image_column, text_column = st.columns((1, 2))  
    with image_column:
        st.image(img_contact_form)         
    
    with text_column:
        st.subheader("問い合わせフォームを追加する方法")
        st.write(
            """
        　　 Web サイトに問い合わせフォームを追加したいです
            以下では、無料サービス「Form Submit」を使用して、
            Streamlit アプリに問い合わせフォームを実装する方法を説明。
            
            """
        )
        st.markdown("[こちら Video...](https://youtu.be/FOULV9Xij_8)")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("ご連絡はこちらから!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/masumoto.naomichi@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
