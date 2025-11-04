import streamlit as st
import requests
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

#---- HEADER SECTION ---
st.subheader("Welcome")
st.title("From messy metrics to confident calls. 🧠")
st.write("I help product & data teams align on the real problem, define metrics that matter, and make better bets—without burning out.")
st.write("[Learn More](https://www.linkedin.com/in/michal-czapski/)")
lottie_coding='https://lottie.host/embed/0b8870f1-6663-49c1-be8e-679c2a6c09b3/LpeivluRKg.lottie'

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