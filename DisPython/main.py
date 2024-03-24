import streamlit as st

from streamlit_option_menu import option_menu

import feedback
import home, trending, account, your, about


def set_background_image(image_url):
    # Define the CSS styles
    styles = f"""
        <style>
            body {{
                background-image: url("{image_url}");
                background-size: cover;
            }}
        </style>
    """

    # Inject the CSS styles into the streamlit app
    st.markdown(styles, unsafe_allow_html=True)


# Main function to run the app
def run():
    set_background_image("bg69.jpg")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1519071711965-f84a1482a05e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8ZGlzYXN0ZXIlMjBkYXJrfGVufDB8MHwwfHx8MA%3D%3D");
             background-attachment: fixed;
             background-size: cover,
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
def run():
     # app = st.sidebar
    with st.sidebar:
        app = option_menu(
            menu_title='Contents ',
            options=['Home', 'Account', 'Safety Tips', 'Call to action', 'About','Feedback','Daily Alerts'],
            icons=['house-fill', 'person-circle', 'shield-fill', 'telephone-fill', 'info-circle-fill', 'chat-fill', 'bell-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"}, }

        )

    if app == "Home":
        home.app()
    if app == "Account":
        account.app()
    if app == "Safety tips":
        trending.app()
    if app == 'Call to action':
        your.app()
    if app == 'about':
        about.app()
    if app == 'Feedback':
        feedback.app()


run()