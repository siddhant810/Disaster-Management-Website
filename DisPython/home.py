import base64
import streamlit as st


def get_base64_of_bin_file(bin_file):
  """
  Encodes a binary file (image) into base64 format for Streamlit.
  """
  with open(bin_file, 'rb') as f:
    data = f.read()
  return base64.b64encode(data).decode()

# Replace 'your_image.png' with the actual filename of your downloaded image
img_encoded = get_base64_of_bin_file("bg69.jpg")

page_bg_img = '''<style>
body {
  background-image: url("data:image/png;base64,%s");
  background-size: cover;
  background-attachment: fixed;  /* Optional: Fix image to screen */
}
</style>''' % img_encoded

st.markdown(page_bg_img, unsafe_allow_html=True)



""""

page_bg_image = 
<style>
[data_testid="stAppViewContainer""] {
background-image: url("https://img.freepik.com/free-vector/gradient-black-background-with-wavy-lines_52683-76100.jpg?t=st=1710917533~exp=1710921133~hmac=5fee3f533b09b41ee7732f7e5441b50e769f57a6e19a11d5470faf2b9ced8156&w=1060")
background-size: cover;
}
</style>

"""
def app():
    st.title("Disaster Relief Portal")
    st.write("Welcome to our Disaster Management website!"
            "As the apex body for disaster management in World,we are committed to safeguarding"
            "lives, minimizing damage,and building a resilient world.")
    st.subheader("**Our Vision:**")
    st.write("*Prevention, Mitigation, Preparedness, and Response:*")
    st.write("We envision an ethos where all stakeholders work together to prevent, mitigate, prepare for and respond"
             "effectively to disasters.")
    st.write("**Technology-Driven Approach:**")
    st.write("We adopt a technology-driven, multi-hazard, and multisectoral strategy to create a safer and disaster-resilient World.")



    st.header("Types of Disaster")
    col1,col2=st.columns(2)
    col1.subheader("Natural Disaster")
    col1.button("Cyclone")
    col1.button("Earthquakes")
    col1.button("Floods")
    col2.subheader("Man-made Disasters")
    col2.button("Chemical")
    col2.button("Nuclear")
    col2.button("Biological")



# Add HTML/CSS to set background image
st.markdown(
    """
    <style>
    body {
        background-image: url('bg69.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Your homepage content goes here
st.write("Welcome to the Homepage!")








