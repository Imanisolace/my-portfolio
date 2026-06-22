import streamlit as st

st.set_page_config(page_title="Daniel Musembi", layout="centered")

# Track which page we're on
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_home():
    st.session_state.page = "home"

def go_projects():
    st.session_state.page = "projects" 

def go_contact():
    st.session_state.page = "contact"

# --- HOME PAGE ---
if st.session_state.page == "home":
    st.title("Data Science & Analytics")
    st.write("Transforming complex data into actionable insights through Python, Streamlit, and numerical modeling.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("View Projects", type="primary", use_container_width=True, on_click=go_projects)
    with col2:
        st.button("Get In Touch", use_container_width=True, on_click=go_contact)

# --- PROJECTS PAGE ---
elif st.session_state.page == "projects":
    st.button("← Back", on_click=go_home)
    st.title("Projects")
    
    st.subheader("1. Finance Dashboard")
    st.write("Interactive tool for financial data analysis + visualization")
    st.link_button("🚀 Open App", "https://financedashbpy-cx8jx3ylrwnf4y3aswzaly.streamlit.app/")
    st.caption("Skills: Pandas, Plotly, Data Validation")
    
    st.subheader("2. Logistic Growth Model")
    st.write("Numerical PDE solver with interactive parameter testing")
    st.link_button("🚀 Open Model", "https://population-logistic-growth.streamlit.app/")
    st.caption("Skills: NumPy, Matplotlib, Numerical Methods")

# --- CONTACT PAGE ---
elif st.session_state.page == "contact":
    st.button("← Back", on_click=go_home)
    st.title("Get In Touch")
    st.write("**Email:** danielmunyali356@gmail.com")
    st.write("**Location:** Nairobi, KE")
    st.write("**Open to:** Data Analyst / Innovation Analyst roles")
