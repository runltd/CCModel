import streamlit as st
import matplotlib.pyplot as plt

def calculate_requirements(power_cook, voltage_cook, duration, inverter_eff, solar_eff):
    energy_cook = power_cook * duration / 1000  # kWh
    battery_capacity = energy_cook / inverter_eff  # kWh
    battery_size_ah = (battery_capacity * 1000) / voltage_cook  # Ah
    solar_power = power_cook / solar_eff  # W
    
    return energy_cook, battery_capacity, battery_size_ah, solar_power

# Streamlit App
st.set_page_config(page_title="Clean Cooking Device Model", page_icon="solarchef logo-yellow.png", layout="wide")
st.title("Clean Cooking Device Specification Model")

# Custom Styling
st.markdown(
    """
    <style>
        body {
            background-color: #1b1612;
            color: #ffd300;
        }
        .stSlider, .stSelectbox, .stButton {
            color: #f590c7 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# User Inputs
power_cook = st.slider("Cooking Appliance Power (W)", min_value=100, max_value=3000, value=700, step=50)
voltage_cook = st.selectbox("Cooking Appliance Voltage (V)", [12, 24, 48, 220], index=1)
duration = st.slider("Cooking Duration (hrs)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
inverter_eff = st.slider("Inverter Efficiency (%)", min_value=70, max_value=100, value=90, step=1) / 100
solar_eff = st.slider("Solar Panel Efficiency (%)", min_value=0, max_value=100, value=22, step=1) / 100

# Calculate Requirements
energy_cook, battery_capacity, battery_size_ah, solar_power = calculate_requirements(
    power_cook, voltage_cook, duration, inverter_eff, solar_eff
)

# Display Results
st.subheader("Calculated Requirements")
st.write(f"Energy Required: {energy_cook:.2f} kWh")
st.write(f"Minimum Battery Capacity: {battery_capacity:.2f} kWh")
st.write(f"Battery Size: {battery_size_ah:.2f} Ah (at {voltage_cook}V)")
st.write(f"Solar Panel Power Required: {solar_power:.0f} W")

# Visualization
labels = ["Energy Consumption (kWh)", "Battery Capacity (kWh)", "Solar Power (W)"]
values = [energy_cook, battery_capacity, solar_power]

fig, ax = plt.subplots()
ax.bar(labels, values, color=["#ffd300", "#f590c7", "#1b1612"])
ax.set_ylabel("Value")
ax.set_title("System Requirements", color="#ffd300")
ax.tick_params(colors="#ffd300")
st.pyplot(fig)
