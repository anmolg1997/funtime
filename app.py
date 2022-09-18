import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime 
from PIL import Image
from streamlit.components.v1 import html
import time
import base64
import random

st.set_page_config()

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

original_title = '<h2 style="font-family:Courier; color:red; font-size: 50px;">Birthday Celebration</h2>'
tattasur = '<h3> <span style="font-family:Courier; color:blue; font-size: 40px;">AMAR MANI TRIPATHI</span> <span style=color:black>urf</span> <span style="font-family:Courier; color:blue; font-size: 40px;"> TATTASUR</span></h3>'
st.markdown(original_title, unsafe_allow_html=True)
today = datetime.now() #.strftime("%b%d, %Y")
bday = '2022-09-27'
bday_date = datetime.strptime(bday, '%Y-%m-%d')
ts = round((bday_date - today).total_seconds())
rm=ts//60
rs=ts%60
st.markdown("#### Abhi ka Waqt : %s" %today.strftime("%b%d, %Y"))
st.markdown(tattasur, unsafe_allow_html=True)

html_body = """
<body>
  <h1>Chodu's Birthday Celebration <br> Starts in <span id="time">{0}:{1:02}</span> minutes!</h1>
</body>
""".format(rm,rs)

my_html = """
<script>
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

window.onload = function () {
    var timedisplay = """ + str(ts) + """,
        display = document.querySelector('#time');
    startTimer(timedisplay, display);
};
</script>
""" + html_body

html(my_html)
flag = True
# while flag:
#     st.balloons()
#     time.sleep(2)
surprise_text = '<p style="font-family:Courier; color:green; font-size:40px;">Surprise >>> On the way .... </p>'
st.markdown("### Although"+surprise_text, unsafe_allow_html=True)
st.write("#### But if Can't Wait till B'day - Qk aapke me keeda hai")
st.markdown("## Then Click Below for *temporary pleasure* ")

img_list=np.arange(1,7,1)
if st.button("Wank in Amar's Tank"):

    add_bg_from_local("assets/{}.jpg".format(random.choice(img_list)))
    st.balloons()


