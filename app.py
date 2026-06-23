import streamlit as st

# Load CSS from external file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.set_page_config(page_title="Daniel Mwangi | Portfolio", page_icon="📊", layout="wide")
load_css('style.css')

# --- HEADER ---
st.title("Daniel Mwangi")
st.subheader("Risk & Credit Analyst | Data-Driven Portfolio")
st.write("I build tools that turn messy risk data into clear decisions.")

# --- PROJECTS ---
st.markdown("---")
st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Risk Dashboard")
    st.write("Interactive dashboard for monitoring credit risk exposure in real-time.")
    st.link_button("Live App", "https://your-risk-app.streamlit.app")
    st.link_button("View Code", "https://github.com/yourusername/risk-dashboard")
    
    st.subheader("2. Credit Scoring Model")
    st.write("ML model predicting default probability with 89% accuracy using XGBoost.")
    st.link_button("Live Demo", "https://your-credit-app.streamlit.app")
    st.link_button("View Code", "https://github.com/yourusername/credit-model")

with col2:
    st.subheader("3. Portfolio Optimizer")
    st.write("Tool for optimizing asset allocation based on risk tolerance and returns.")
    st.link_button("Live App", "https://your-portfolio-app.streamlit.app")
    st.link_button("View Code", "https://github.com/yourusername/portfolio-opt")

# --- CONTACT ---
st.markdown("---")
st.header("Contact")
st.write("📧 daniel.email@example.com")
st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
st.write("🐙 [GitHub](https://github.com/yourusername)")

st.markdown('<p class="caption">Built with Streamlit • Deployed on Streamlit Cloud</p>', unsafe_allow_html=True)
