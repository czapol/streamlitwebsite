import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Michal Czapski Webpage", page_icon="🧠", layout="wide")
#mojis at https://www.webfx.com/tools/emoji-cheat-sheet/
#layout="wide" - use entire section 

# download graphics from lottie 
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

#---- HEADER SECTION ---
st.subheader("Welcome")
st.title("From messy metrics to confident calls. 🧠")
st.write("I help product & data teams align on the real problem, define metrics that matter, and make better bets—without burning out.")
st.write("[Learn More](https://www.linkedin.com/in/michal-czapski/)")
# Assets
lottie_coding=load_lottieurl("https://lottie.host/20ec146a-5347-42b9-86c5-4b851f2782f3/jz0SzBAbpw.json")
img_offer=Image.open("meeting.png")

# --- What i doo ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Problem")
        st.write("##") #inserting some space
        st.write(
            """
           -  Your team debates metrics but still ships on vibes.
            - Important projects stall; meetings blur; decisions linger.
            - Friction builds (or people avoid the hard convo).
            - You want clear priorities, sane pace, and momentum.


            """



        )

    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')
    
    # --- OFFERING -- 
    with st.container():
        st.write("---")
        st.header("Offering")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            #insert image
            st.image(img_offer)
        with text_column:
            st.subheader("Outcome: shared clarity → crisp decision → owners & next steps.")
            st.write("""
                - Problem framing + decision workshop
                - North-star + guardrails draft
                 - Decision memo & 14-day follow-up
                - FAQ: How do we start? → Free 20-min intro; I right-size the format.
                """         
            )
    #--- CONTACT ---
    with st.container():
        st.write("---")
        st.header("Contact")
        st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/czapski.michal@gmail.com" method="POST">
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
        