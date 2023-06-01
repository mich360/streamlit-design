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
    # with right_column:
    #     st.write('右カラム、アニメーションをここに製作中')
import streamlit.components.v1 as components

# LottieファイルのURL
# lottie_url = "https://assets7.lottiefiles.com/packages/lf20_bP3BLu.json"


# HTMLコードを生成して表示
# html_code = f"""
# <div id="lottie-container"></div>
# <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.5/lottie.min.js"></script>
# <script>
#     var animationData = {json.dumps(lottie_data)};
#     var container = document.getElementById('lottie-container');
#     var anim = lottie.loadAnimation({{
#         container: container,
#         renderer: 'svg',
#         loop: true,
#         autoplay: true,
#         animationData: animationData
#     }});
# </script>
# """
# HTMLコードを生成して表示（縮小表示）
html_code = f"""
<div id="lottie-container" style="transform: scale(0.7);"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.5/lottie.min.js"></script>
<script>
    var animationData = {json.dumps(lottie_data)};
    var container = document.getElementById('lottie-container');
    var anim = lottie.loadAnimation({{
        container: container,
        renderer: 'svg',
        loop: true,
        autoplay: true,
        animationData: animationData
    }});
</script>
"""
with right_column:
    st.subheader("アニメーション")
    st.write(
        """
         lottiefiles.comで今回は「cat」を検索し選ぶと、Lottie Animation UR　からコピーして
         lottie_url =　"この部分に貼り付ける"
        """
    )  
    # Lottieアニメーションを表示
    components.html(html_code, height=350)

# components.html(html_code, height=800)



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
        st.subheader("問い合わせフォームを追加する方法")
        st.write(
            """
            Webサイトに
            Webサイトに問い合わせフォームを追加したいです。
            以下では、無料サービス「Form Submit」を使用して、
            Streamlitアプリに問い合わせフォームを実装する方法
            解説ありがとう。
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
st.warning("[前のページ >](https://canape2020.stars.ne.jp/python/)")
