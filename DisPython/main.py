import streamlit as st

from streamlit_option_menu import option_menu

import feedback
import home, trending, account, your, about


def run():
     # app = st.sidebar
    with st.sidebar:
        app = option_menu(
            menu_title='Contents ',
            options=['Home', 'Account', 'Safety Tips', 'Call to action', 'About','Feedback'],
            icons=['house-fill', 'person-circle', 'security-fill', 'telephone-fill', 'info-circle-fill', 'contact-fill'],
            menu_icon='chat-text-fill',
            default_index=1,
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