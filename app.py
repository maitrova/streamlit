import streamlit as st
import os
from dotenv import load_dotenv

# Load variables from .env file (for local development)
load_dotenv()

# Read the variable from environment
my_data = os.getenv("MY_DATA")
my_data1 = os.getenv("MY_DATA1")

st.title("My Streamlit App")
st.write("### Data from variable:")
st.info(my_data)
st.info(my_data1)
