import pandas as pd
import streamlit as st
from scraper import scrape_linkedin   


PRIMARY = "#415E72"
BG = "#F3E2D4"
SECONDARY = "#C5B0CD"
TEXT = "#17313E"

st.set_page_config(page_title="LinkedIn Job Scraper", layout="wide")

st.markdown(f"""
<style>
    .stApp {{ background-color: {BG}; color: {TEXT}; }}
    .stButton>button {{
        background-color: {PRIMARY};
        color: white; border-radius: 10px; padding: .5rem 1rem;
        border: none;
    }}
    .stButton>button:hover {{ background-color: {SECONDARY}; color: {TEXT}; }}
    .metric-card {{
        background: white; border-radius: 14px; padding: 1rem; border: 1px solid #e8e8e8;
    }}
</style>
""", unsafe_allow_html=True)

st.title("Linkedin Job Scraper")
st.caption("Scrape jobs directly from LinkedIn")

col1, col2, col3 = st.columns([1.5, 1, 1])
with col1:
    keyword = st.text_input("Job Keyword", "Java Developer")
with col2:
    location = st.text_input("Location", "Pune")
with col3:
    pages = st.number_input("Pages to Scrape", min_value=1, max_value=5, value=1)

run = st.button(" Scrape Jobs")

jobs_df = None
if run:
    with st.spinner("Scraping LinkedIn..."):
        jobs_df = scrape_linkedin(keyword, location, int(pages), headless=True)

    if jobs_df is not None and not jobs_df.empty:
        st.success(f"Found {len(jobs_df)} jobs from LinkedIn.")
        st.dataframe(jobs_df, use_container_width=True)
        st.download_button("📥 Download CSV", jobs_df.to_csv(index=False), "linkedin_jobs.csv", mime="text/csv")
    else:
        st.warning("No jobs found on LinkedIn (try logging in).")
