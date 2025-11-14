import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Background image URL (use a direct image URL; replace if needed)
bg_url = "https://images.unsplash.com/photo-1655929299728-93ee15ed7967?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTYzfHxhZ3JpY3VsdHVyZXxlbnwwfHwwfHx8MA%3D%3D"

# Optional: try fetching (not required for CSS background)
def fetch_image(url):
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        return Image.open(BytesIO(resp.content))
    except Exception:
        return None

# Page configuration
st.set_page_config(page_title="Demo Login", page_icon="🔐", layout="wide")

# Fixed CSS: use proper CSS variables, .stApp selector and single card wrapper
css = f"""
<style>
:root {{
    /* make card darker so white text is readable */
    --card-bg: rgba(0, 0, 0, 0.55);
    --text: #ffffff;
    --muted: rgba(255, 255, 255, 0.85);
    --primary: #60a5fa;
}}
/* Ensure app container fills viewport */
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{
    height: 100%;
}}
/* Background on the Streamlit app surface */
.stApp {{
    background-image: linear-gradient(rgba(10,15,25,0.45), rgba(10,15,25,0.45)), url("{bg_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    min-height: 100vh;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}

/* Centered login card */
.login-card{{
    background: var(--card-bg);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 18px 36px rgba(0,0,0,0.28);
    max-width: 360px;
    margin: 0 auto;
}}

/* Center header and subtitle inside the card */
.login-card h2,
.login-card p {{
    text-align: center;
    color: var(--text);
}}
.muted {{
    color: var(--muted) !important;
    text-align: center;
}}

/* Visible, prominent validation alerts */
.alert {{
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 12px;
    font-weight: 600;
    display: flex;
    gap: 10px;
    align-items: center;
}}
.alert.error {{
    background: linear-gradient(90deg, rgba(220,38,38,0.12), rgba(220,38,38,0.08));
    border: 1px solid rgba(220,38,38,0.25);
    color: #ffdddd;
    box-shadow: 0 6px 18px rgba(220,38,38,0.06);
}}
.alert.success {{
    background: linear-gradient(90deg, rgba(34,197,94,0.12), rgba(34,197,94,0.08));
    border: 1px solid rgba(34,197,94,0.25);
    color: #e6ffef;
    box-shadow: 0 6px 18px rgba(34,197,94,0.06);
}}

/* small field-specific error text */
.field-error {{
    color: #ffdddd;
    font-size: 12px;
    margin-top: 6px;
}}

/* Slight shake animation to draw attention */
@keyframes shake {{
  0% {{ transform: translateX(0); }}
  25% {{ transform: translateX(-6px); }}
  50% {{ transform: translateX(6px); }}
  75% {{ transform: translateX(-4px); }}
  100% {{ transform: translateX(0); }}
}}
.alert.shake {{
    animation: shake 360ms ease-in-out;
}}

/* Input styling to be visible on dark card */
.login-card input, .login-card textarea {{
    background: rgba(255,255,255,0.06) !important;
    color: var(--text) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
}}
.login-card input::placeholder {{
    color: rgba(255,255,255,0.7) !important;
}}

/* Hide default Streamlit header/footer for cleaner look */
header[data-testid="stHeader"], footer[data-testid="stFooter"] {{
    display: none;
}}

@media (max-width: 600px) {{
    .login-card {{
        width: 92%;
        padding: 14px;
    }}
}}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Layout: place a single centered card
with st.container():
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

        # placeholder for prominent alert (filled on validation)
        alert_slot = st.empty()

        st.markdown("<h2 style='text-align:center; margin:0 0 6px 0; font-weight:600; color:#ffffff;'>Welcome back</h2>", unsafe_allow_html=True)
        st.markdown("<p style='margin:0 0 12px 0;' class='muted'>Sign in to continue to your dashboard</p>", unsafe_allow_html=True)

        # input placeholders for inline field errors
        email = st.text_input("Email", placeholder="name@example.com", key="email")
        email_err_slot = st.empty()

        password = st.text_input("Password", type="password", placeholder="Enter your password", key="password")
        password_err_slot = st.empty()

        col_remember, col_forgot = st.columns([1, 1])
        with col_remember:
            remember = st.checkbox("Remember me", value=True)
        with col_forgot:
            st.markdown("<div style='text-align:right;'><a href='#' style='font-size:12px; color:var(--primary); text-decoration:none;'>Forgot password?</a></div>", unsafe_allow_html=True)

        st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
        signed_in = st.button("Sign in", use_container_width=True)
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        st.markdown("<p class='muted' style='font-size:12px; text-align:center; margin:0;'>Demo only. No backend connected.</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# validation logic: more visible alerts and inline field errors
if signed_in:
    # clear previous per-field errors/alerts
    try:
        alert_slot.empty()
        email_err_slot.empty()
        password_err_slot.empty()
    except Exception:
        pass

    errors = []
    if not email:
        errors.append("Please enter your email address.")
    if not password:
        errors.append("Please enter your password.")
    # simple email format check
    if email and "@gmail.com" not in email:
        errors.append("Email looks invalid. Include an '@gmail.com'.")

    if errors:
        # build a single prominent error box with list
        list_html = "".join(f"<li style='margin-bottom:4px'>{e}</li>" for e in errors)
        alert_html = f"""
        <div class="alert error shake">
            <span style="font-size:18px;">❗</span>
            <div>
                <div style="font-weight:700; margin-bottom:6px;">Fix the following</div>
                <ul style="margin:0 0 0 18px; padding:0; list-style:disc;">{list_html}</ul>
            </div>
        </div>
        """
        alert_slot.markdown(alert_html, unsafe_allow_html=True)

        # show inline messages under each field
        if not email:
            email_err_slot.markdown("<div class='field-error'>Email is required.</div>", unsafe_allow_html=True)
        elif "@" not in email:
            email_err_slot.markdown("<div class='field-error'>Invalid email format.</div>", unsafe_allow_html=True)
        if not password:
            password_err_slot.markdown("<div class='field-error'>Password is required.</div>", unsafe_allow_html=True)

    else:
        # success
        alert_html = """
        <div class="alert success">
            <span style="font-size:18px;">✅</span>
            <div>
                <div style="font-weight:700;">Signed in</div>
                <div style="font-size:13px; opacity:0.9;">This is a frontend demo — no backend was contacted.</div>
            </div>
        </div>
        """
        alert_slot.markdown(alert_html, unsafe_allow_html=True)
    
