import streamlit as st

st.set_page_config(
    page_title="Innovation & Risk Analytics", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM STYLING
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0A192F 0%, #112240 100%);
    }
    h1, h2, h3, p, span {
        color: #E6F1FF !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #0A192F !important;
        font-weight: 700;
        border: none;
        border-radius: 12px;
        padding: 14px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(255, 215, 0, 0.3);
    }
    div[data-testid="stLinkButton"]>a {
        background: #112240;
        border: 2px solid #FFD700;
        color: #FFD700 !important;
        border-radius: 10px;
        padding: 12px;
        font-weight: 600;
        text-align: center;
    }
    div[data-testid="stLinkButton"]>a:hover {
        background: #FFD700;
        color: #0A192F !important;
    }
    hr {
        border-top: 1px solid #233554;
    }
    .caption {
        color: #8892B0 !important;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# --- PAGE STATE ---
if "page" not in st.session_state:
    st.session_state.page = "home"

def go_home(): st.session_state.page = "home"
def go_projects(): st.session_state.page = "projects" 
def go_contact(): st.session_state.page = "contact"

# --- HOME ---
if st.session_state.page == "home":
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Innovation & Risk Analytics")
    st.subheader("Daniel Musembi | Applied Mathematics + Computer Science, Kenyatta University")
    st.write("I build decision tools for insurance & finance: models that test risk before rollout, dashboards that turn messy customer data into clear action.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.button("View Tools", type="primary", use_container_width=True, on_click=go_projects)
    with col2:
        st.button("Contact Me", use_container_width=True, on_click=go_contact)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p class="caption">Targeting: Innovation Analyst / Business Analytics roles | Nairobi, KE</p>', unsafe_allow_html=True)

# --- PROJECTS ---
elif st.session_state.page == "projects":
    st.button("← Back", on_click=go_home)
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Tools Built for Business Impact")
    
    st.markdown("---")
    st.subheader("1. Financial Risk Dashboard")
    st.write("Interactive dashboard for financial data validation + scenario testing. Built to flag portfolio risks and support client reporting decisions fast.")
    st.link_button("🚀 Launch Dashboard", "https://financedashbpy-cx8jx3ylrwnf4y3aswzaly.streamlit.app/", use_container_width=True)
    st.markdown('<p class="caption">Britam Relevance: Risk validation, Portfolio monitoring | Stack: Pandas, Plotly, Data Integrity</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("2. Predictive Growth Model")
    st.write("Numerical PDE solver for growth/claim forecasting. Test 'what-if' parameters before committing capital. Built for actuarial + strategy teams.")
    st.link_button("🚀 Run Model", "https://population-logistic-growth.streamlit.app/", use_container_width=True)
    st.markdown('<p class="caption">Britam Relevance: Claims forecasting, Stress testing | Stack: NumPy, SciPy, Numerical Methods</p>', unsafe_allow_html=True)

# --- CONTACT ---
elif st.session_state.page == "contact":
    st.button("← Back", on_click=go_home)
    st.markdown("<br>", unsafe_allow_html=True)
    st.title("Let's Build Together")
    st.markdown("---")
    st.write("**Daniel Musembi**")
    st.write("BSc Applied Mathematics & Computer Science, Kenyatta University")
    st.write("**Email:** danielmunyali356@gmail.com")
    st.write("**whatsapp:** https://wa.me/qr/ATOJA2XM3OEPG1")
    st.write("**Location:** Nairobi, KE")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Looking to join teams using analytics to reduce risk, improve customer experience, and drive innovation at scale.")
