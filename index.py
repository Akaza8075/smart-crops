import streamlit as st
from datetime import date

# Title of the app
st.title("Interactive Crop Information Form")

# Use various input widgets for diversity

# Country: Selectbox (dropdown)
countries = ["USA", "India", "Brazil", "China", "Australia"]
country = st.selectbox("Select Country", countries)

# Crop Type: Radio buttons
crop_types = ["Wheat", "Rice", "Corn", "Soybean", "Barley"]
crop_type = st.radio("Choose Crop Type", crop_types)

# Soil pH: Slider
soil_ph = st.slider("Soil pH Level", min_value=0.0, max_value=14.0, value=7.0, step=0.1)

# Soil Moisture: Number input
soil_moisture = st.number_input("Soil Moisture (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

# Temperature: Slider (another slider for variety, but different range)
temperature = st.slider("Average Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.5)

# Humidity: Number input (with format)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=1.0, format="%.1f")

# Irrigation Type: Multiselect (for pill-like tags, even if single, user can select one)
irrigation_types = ["Drip", "Sprinkler", "Flood", "Pivot", "Surface"]
irrigation = st.multiselect("Select Irrigation Type (pills/tags)", irrigation_types, max_selections=1)
irrigation_type = irrigation[0] if irrigation else None

# Fertilizer Type: Text input
fertilizer_type = st.text_input("Enter Fertilizer Type", value="Organic")

# Sowing Date: Date input
sowing_date = st.date_input("Sowing Date", value=date.today())

# Harvest Date: Date input (with min/max for variety)
harvest_date = st.date_input("Harvest Date", value=date.today(), min_value=date.today())

# Submit button
if st.button("Submit Form"):
    st.success("Form Submitted Successfully!")
    st.write("### Submitted Data:")
    st.write(f"**Country:** {country}")
    st.write(f"**Crop Type:** {crop_type}")
    st.write(f"**Soil pH:** {soil_ph}")
    st.write(f"**Soil Moisture:** {soil_moisture}")
    st.write(f"**Temperature:** {temperature}")
    st.write(f"**Humidity:** {humidity}")
    st.write(f"**Irrigation Type:** {irrigation_type}")
    st.write(f"**Fertilizer Type:** {fertilizer_type}")
    st.write(f"**Sowing Date:** {sowing_date}")
    st.write(f"**Harvest Date:** {harvest_date}")

# Additional Streamlit elements for interactivity and variety
st.sidebar.header("Additional Controls")
theme = st.sidebar.checkbox("Enable Dark Theme")
if theme:
    st.markdown("<style>body { background-color: #333; color: #fff; }</style>", unsafe_allow_html=True)

info_expander = st.expander("Info")
info_expander.write("This form is used to collect data and predict possible outcomes for agriculture")
