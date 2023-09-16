import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json

st.set_page_config(page_title="My Portfolio", page_icon="👨‍💻",layout="wide")

# # for online
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# for local
def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


#use local css style

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style/index.css")

# Assets
# lottie_coding = load_lottieurl("https://app.lottiefiles.com/animation/d32ce54a-4598-49d0-a31e-afa28ca45a64")

lottie_coding = load_lottiefile("animation_lmm83cw8.json")

image_project1 = Image.open("images/Compressor_io.png")
image_project2 = Image.open("images/flutterAppointmentapp.jpg")


# Header section

st.subheader("Hello, I am Niladri :wave:")
st.title("Full stack developer | Application Developer")
st.write("Highly skilled and motivated Full Stack Developer and Flutter Application Developer with a strong passion for creating innovative and user-centric software solutions. With a diverse background in web and mobile development, I bring a unique blend of technical expertise, creativity, and problem-solving abilities to every project. Committed to delivering high-quality code and exceptional user experiences while staying up-to-date with the latest industry trends and technologies. I am currently studying in [**University of Engineering and Management**](https://uem.edu.in/uem-kolkata/).")
st.write("[Learn More >](https://github.com/niladri60)")


# About section

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Skills")
        st.write("##")
        st.subheader("Full Stack Development: ")
        st.write("""
        - Proficient in both front-end and back-end technologies, including HTML, CSS, JavaScript, Node.js, Express.js, and MongoDB.
        - Experienced in designing and developing responsive web applications and ensuring optimal performance and scalability.
        - Familiar with various front-end frameworks and libraries, such as React, Angular, and Vue.js.
        """)
        
        st.subheader("Flutter Application Development:")
        st.write("""
                - Expertise in building cross-platform mobile applications using Flutter and Dart.
                - Strong understanding of Flutter's widget-based architecture and state management.
                - Familiar with various Flutter packages and libraries, such as Firebase, Bloc, and Provider.
                - Experience in creating visually appealing and interactive UIs for Android and iOS.
                 
                If this sounds insteresting to you, feel free to reach out to me through [LinkedIn](https://www.linkedin.com/in/niladri60/).
                 """)
    with right_column:
        if lottie_coding is not None:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.write("Failed to load Lottie animation.")



# Project section
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(image_project1)

    with text_column:
        st.subheader("Project Image Compressor")
        st.write(
            """ 
            This is a project which is based on **Computer Vision**. In this project, I have used **K-Means Clustering** algorithm to compress the image. I have also used **Streamlit** to build the web app. It is deployed on **Heroku**.
            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(image_project2)

    with text_column:
        st.subheader("Doctor Appointment App")
        st.write(
            """ 
            This is a project which is based on **Flutter**. In this project, I have used **Firebase** as a backend. I have used blockchain technology to store the data of the patients and doctors. It will help to keep the data of the patients and doctors safe and secure. Because blockchain is a decentralized system. It is deployed on **Google Play Store**.
            """
        )

# contact form

with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")
    contact_form = """ 
    <form action="https://formsubmit.co/niladri.nandy2names.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name="message" placeholder = "Your message" required></textarea>
     <button type="submit">Send</button>
     </form> 
     """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    