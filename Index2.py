import streamlit as st
from datetime import date

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Agri App", page_icon="🌱", layout="wide")

# ----------------------------
# SESSION STATE
# ----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# ----------------------------
# BACKGROUND IMAGE
# ----------------------------
bg_url = "https://images.unsplash.com/photo-1655929299728-93ee15ed7967?w=1200"

# ----------------------------
# GLOBAL CSS
# ----------------------------
css = f"""
<style>
html, body {{
    margin: 0;
}}

.stApp {{
    background-image: linear-gradient(rgba(10,15,25,0.5), rgba(10,15,25,0.5)), url("{bg_url}");
    background-size: cover;
    background-attachment: fixed;
}}

header[data-testid="stHeader"], footer[data-testid="stFooter"] {{
    display: none;
}}

/* ---------- TASKBAR ---------- */
.taskbar {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: rgba(15, 23, 42, 0.95);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    z-index: 9999;
    box-shadow: 0 4px 14px rgba(0,0,0,0.4);
}}

.taskbar .title {{
    color: #fff;
    font-size: 20px;
    font-weight: 600;
}}

.taskbar .right {{
    display: flex;
    align-items: center;
    gap: 16px;
    color: #e5e7eb;
    font-size: 14px;
}}

/* ---------- LOGIN CARD ---------- */
.login-card {{
    background: rgba(0,0,0,0.55);
    border-radius: 12px;
    padding: 18px;
    max-width: 300px;   /* SMALLER CARD */
    margin: 120px auto;
    color: white;
}}

/* Smaller button */
.narrow-input button {{
    padding: 4px 12px !important;
    font-size: 13px !important;
}}

/* ---------- CONTENT OFFSET ---------- */
.main-content {{
    margin-top: 80px;
    padding: 20px;
}}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# =====================================================
# LOGIN PAGE
# =====================================================
if not st.session_state.logged_in:

    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;margin-bottom:10px;'>Welcome Back</h3>", unsafe_allow_html=True)

    # Extra narrow center column
    col_l, col_c, col_r = st.columns([1.5, 1, 1.5])

    with col_c:
        email = st.text_input("Email", placeholder="user@gmail.com")
        password = st.text_input("Password", type="password")

        st.markdown("<div class='narrow-input'>", unsafe_allow_html=True)
        login_clicked = st.button("Sign in")
        st.markdown("</div>", unsafe_allow_html=True)

    if login_clicked:
        if email and password and email.endswith("@gmail.com"):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.rerun()
        else:
            st.error("Invalid login details")

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# MAIN APP (AFTER LOGIN)
# =====================================================
else:
    # ---------- TASKBAR ----------
    st.markdown(
        f"""
        <div class="taskbar">
            <div class="title">🌱 Agri Dashboard</div>
            <div class="right">
                <span>{st.session_state.user_email}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Logout button
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # ---------- MAIN CONTENT ----------
    st.markdown("<div class='main-content'>", unsafe_allow_html=True)

    st.title("🌾 Interactive Crop Information Form")

    # Form inputs
    country = st.selectbox("Select Country", ["USA", "India", "Brazil", "China", "Australia"])
    crop = st.radio("Crop Type", ["Wheat", "Rice", "Corn", "Soybean", "Barley"])
    soil_ph = st.slider("Soil pH", 0.0, 14.0, 7.0)
    moisture = st.number_input("Soil Moisture (%)", 0.0, 100.0, 50.0)
    temp = st.slider("Temperature (°C)", -10.0, 50.0, 25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
    irrigation = st.selectbox("Irrigation Type", ["Drip", "Sprinkler", "Flood"])
    fertilizer = st.text_input("Fertilizer Type", "Organic")
    sow_date = st.date_input("Sowing Date", date.today())
    harv_date = st.date_input("Harvest Date", date.today())

    # Submit button with normal output
    if st.button("Submit"):
        st.success("✅ Form Submitted")
        st.write("### Submitted Data:")
        st.write(f"**Country:** {country}")
        st.write(f"**Crop Type:** {crop}")
        st.write(f"**Soil pH:** {soil_ph}")
        st.write(f"**Soil Moisture (%):** {moisture}")
        st.write(f"**Temperature (°C):** {temp}")
        st.write(f"**Humidity (%):** {humidity}")
        st.write(f"**Irrigation Type:** {irrigation}")
        st.write(f"**Fertilizer Type:** {fertilizer}")
        st.write(f"**Sowing Date:** {sow_date}")
        st.write(f"**Harvest Date:** {harv_date}")

    st.markdown("</div>", unsafe_allow_html=True)
