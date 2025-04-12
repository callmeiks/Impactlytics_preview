import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import base64
from streamlit_option_menu import option_menu


# Login setup
__login__obj = __login__(
    auth_token="courier_auth_token",
    company_name="Shims",
    width=200,
    height=250,
    logout_button_name='Logout',
    hide_menu_bool=False,
    hide_footer_bool=False,
    lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json'
)


# Add logo to sidebar with rounded edges
logo_path = "img/usc.png"
with open(logo_path, "rb") as image_file:
    logo_base64 = base64.b64encode(image_file.read()).decode()

# HTML with CSS to round the image (50% = perfect circle if width == height)
logo_html = f"""
    <div style="text-align: center; padding-bottom: 1rem;">
        <img src="data:image/webp;base64,{logo_base64}" 
             alt="Logo" width="250" height="100"
             style="border-radius: 20px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1);">
    </div>
"""
st.sidebar.markdown(logo_html, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Impactlytics - Testing App")

# overview text
st.sidebar.markdown(
    """
This research overcomes limitations of prior correlational studies by using a formal causal framework and experimental data from platform APIs. Impactlytics reveals true cause-effect links between content features and performance, bridging behavioral theory and practical optimization.
    """
)

# sponsess text
st.sidebar.markdown(
    """
    Sponsored by **USC Marshall**.
    """
)


# Authentication
LOGGED_IN = __login__obj.build_login_ui()
username = __login__obj.get_username()

# only allow authorized USC users
st.sidebar.markdown("only **Authorized** USC users can access this app.")



