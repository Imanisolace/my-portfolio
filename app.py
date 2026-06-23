import streamlit as st

# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Daniel Munyali | Portfolio", page_icon="📊", layout="wide")
load_css('style.css')

# --- HEADER ---
st.title("Daniel Munyali")
st.subheader("Risk & Credit Analyst | Data-Driven Portfolio")
st.write("I build tools that turn messy risk data into clear decisions.")

# --- PROJECTS ---
st.markdown("---")
st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Population Logistic Growth")
    st.write("Interactive model showing population growth using logistic equation.")
    st.link_button("Live App", "https://population-logistic-growth.streamlit.app/")
    st.link_button("GitHub Code", "https://github.com/Imanisolace/P-logistic-growth")
    
with col2:
    st.subheader("2. Finance Dashboard")
    st.write("Dashboard for visualizing financial data and key metrics.")
    st.link_button("Live App", "https://financedashbpy-cx8jx3ylrwnf4y3aswzaly.streamlit.app/")
    st.link_button("GitHub Code", "https://github.com/Imanisolace/gdp-dashboard")

# --- CONTACT ---
st.markdown("---")
st.header("Contact")
st.write("📨 [email](mailto:danielmunyali356@gmail.com)")
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/daniel-musembi-691040347)")
st.write("🐙 [GitHub](https://github.com/imanisolace)")
st.write("🗨️ [whatsapp](https://wa.me/qr/ATOJA2XM3OEPG1)")
st.markdown('<p class="caption">Built with Streamlit • Deployed on Streamlit Cloud</p>', unsafe_allow_html=True)
