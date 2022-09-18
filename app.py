import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime 
from pil import Image

st.title("Birthday Celebration")
today = datetime.now().strftime("%M%d, %Y)
st.markdown("%s", today)
