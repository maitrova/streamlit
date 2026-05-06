import streamlit as st
import os
from dotenv import load_dotenv

# Load variables from .env file (for local development)
load_dotenv()

# Read from Streamlit secrets (cloud) or .env (local)
my_data = st.secrets.get("MY_DATA") or os.getenv("MY_DATA")
my_data1 = st.secrets.get("MY_DATA1") or os.getenv("MY_DATA1")

st.title("My Streamlit App")
st.write("### Data from variable:")
st.info(my_data)
st.info(my_data1)
