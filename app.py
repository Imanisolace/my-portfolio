import streamlit as st

st.set_page_config(page_title="Daniel Musembi - Portfolio", layout="centered")

st.title("Daniel Musembi 👋")
st.subheader("BSc Applied Mathematics & Computer Science | Kenyatta University")
st.write("I build data dashboards and numerical models to test ideas with code before rollout.")

st.divider()

st.header("Projects")

st.subheader("1. Finance Dashboard")
st.write("Interactive tool for financial data analysis, cleaning, and visualization")
st.link_button("🚀 Open Finance App", "https://financedashbpy-cx8jx3ylrwnf4y3aswzaly.streamlit.app/")
st.caption("**Skills:** Pandas, Plotly, Data Validation, Streamlit")

st.subheader("2. Logistic Growth Model")
st.write("Numerical PDE solver with interactive parameter testing for population dynamics")
st.link_button("🚀 Open Model App", "https://population-logistic-growth.streamlit.app/")
st.caption("**Skills:** NumPy, Matplotlib, Numerical Methods, SciPy")

st.divider()
st.write("**Email:** danielmunyali356@gmail.com")
st.write("**Location:** Nairobi, KE | Open to Data Analyst / Innovation Analyst roles")
