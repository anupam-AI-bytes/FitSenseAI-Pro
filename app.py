"""
=========================================================
FitSense AI Pro
Main Application

Author: Anupam Mishra
Version: 2.0
=========================================================
"""

# --------------------------------------------------------
# Imports
# --------------------------------------------------------

import streamlit as st

from modules.calculations import *
from modules.recommendations import *
from modules.charts import *

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="FitSense AI Pro",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------------
# Custom Styling
# --------------------------------------------------------

st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:42px;
    color:#2E8B57;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:18px;
}

.metric-card{
    padding:20px;
    border-radius:15px;
    background-color:#f8f9fa;
    border:1px solid #dddddd;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# Header
# --------------------------------------------------------

st.markdown(
    "<h1 class='main-title'>💪 FitSense AI Pro</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Your Personal AI Powered Health Dashboard</p>",
    unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------------
# Sidebar
# --------------------------------------------------------

st.sidebar.title("👤 Health Profile")

name = st.sidebar.text_input(
    "Full Name"
)

age = st.sidebar.slider(
    "Age",
    10,
    100,
    25
)

gender = st.sidebar.selectbox(
    "Gender",
    [
        "Male",
        "Female"
    ]
)

height = st.sidebar.number_input(
    "Height (metres)",
    min_value=1.00,
    max_value=2.50,
    value=1.70,
    step=0.01
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=20,
    max_value=250,
    value=70
)

activity = st.sidebar.selectbox(

    "Activity Level",

    [

        "Sedentary",

        "Lightly Active",

        "Moderately Active",

        "Very Active",

        "Extremely Active"

    ]
)

goal = st.sidebar.selectbox(

    "Fitness Goal",

    [

        "Maintain Weight",

        "Lose Weight",

        "Gain Muscle"

    ]
)

sleep = st.sidebar.slider(
    "Sleep (Hours)",
    4,
    12,
    8
)

st.sidebar.markdown("---")

calculate = st.sidebar.button(
    "🚀 Analyze My Health"
)

# --------------------------------------------------------
# Welcome Screen
# --------------------------------------------------------

if not calculate:

    st.info(
        "👈 Fill your health profile from the sidebar and click **Analyze My Health**."
    )

    st.image(
        "https://images.unsplash.com/photo-1517836357463-d25dfeac3438",
        use_container_width=True
    )

    st.stop()

# --------------------------------------------------------
# Perform Calculations
# --------------------------------------------------------

bmi = calculate_bmi(weight, height)

category = bmi_category(bmi)

bmr = calculate_bmr(
    weight,
    height,
    age,
    gender
)

tdee = calculate_tdee(
    bmr,
    activity
)

target = target_calories(
    tdee,
    goal
)

protein = protein_requirement(
    weight,
    goal
)

water = water_requirement(
    weight
)

ideal_min, ideal_max = ideal_weight_range(
    height
)

body_fat = body_fat_percentage(
    bmi,
    age,
    gender
)

lean_mass = lean_body_mass(
    weight,
    body_fat
)

macros = macro_split(
    target
)

score = health_score(
    bmi,
    activity,
    water,
    sleep
)

summary = health_summary(
    category
)
# --------------------------------------------------------
# Dashboard
# --------------------------------------------------------

st.markdown("---")

st.header(f"👋 Welcome {name}")

st.write(
    "Here's your personalized health dashboard based on the information you provided."
)

# --------------------------------------------------------
# Metrics Row 1
# --------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "⚖ BMI",
        f"{bmi:.1f}"
    )

with col2:
    st.metric(
        "❤️ Health Category",
        category
    )

with col3:
    st.metric(
        "⭐ Health Score",
        f"{score}/100"
    )

# --------------------------------------------------------
# Metrics Row 2
# --------------------------------------------------------

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "🔥 BMR",
        f"{bmr:.0f} kcal/day"
    )

with col5:
    st.metric(
        "🍽 Daily Calories",
        f"{target:.0f} kcal"
    )

with col6:
    st.metric(
        "💪 Protein",
        f"{protein:.0f} g/day"
    )

# --------------------------------------------------------
# Metrics Row 3
# --------------------------------------------------------

col7, col8, col9 = st.columns(3)

with col7:
    st.metric(
        "💧 Water",
        f"{water:.1f} L/day"
    )

with col8:
    st.metric(
        "🏋 Lean Body Mass",
        f"{lean_mass:.1f} kg"
    )

with col9:
    st.metric(
        "📉 Body Fat",
        f"{body_fat:.1f}%"
    )

# --------------------------------------------------------
# Ideal Weight
# --------------------------------------------------------

st.markdown("---")

st.subheader("🎯 Ideal Weight Range")

st.success(
    f"{ideal_min:.1f} kg  →  {ideal_max:.1f} kg"
)

# --------------------------------------------------------
# Health Summary
# --------------------------------------------------------

st.subheader("📝 Health Summary")

st.info(summary)
# --------------------------------------------------------
# Dashboard Charts
# --------------------------------------------------------

st.markdown("---")

st.header("📊 Health Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        bmi_gauge(bmi),
        use_container_width=True
    )

with col2:

    st.plotly_chart(
        health_score_gauge(score),
        use_container_width=True
    )

st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    st.plotly_chart(
        macro_chart(macros),
        use_container_width=True
    )

with col4:

    st.plotly_chart(
        calorie_chart(target),
        use_container_width=True
    )

st.markdown("---")

col5, col6 = st.columns(2)

with col5:

    st.plotly_chart(
        water_chart(water),
        use_container_width=True
    )

with col6:

    st.plotly_chart(
        bmi_comparison(bmi),
        use_container_width=True
    )

# --------------------------------------------------------
# Health Insights
# --------------------------------------------------------

st.markdown("---")

st.header("📌 Quick Health Insights")

insight1, insight2, insight3 = st.columns(3)

with insight1:

    st.success(
        f"🏆 BMI Category: **{category}**"
    )

with insight2:

    st.info(
        f"🔥 Daily Calories Target: **{target} kcal**"
    )

with insight3:

    st.warning(
        f"💧 Drink around **{water:.1f} litres** of water today."
    )

# --------------------------------------------------------
# Expandable Details
# --------------------------------------------------------

with st.expander("📖 View Complete Body Analysis"):

    st.write(f"**BMI:** {bmi:.2f}")

    st.write(f"**Body Fat Percentage:** {body_fat:.1f}%")

    st.write(f"**Lean Body Mass:** {lean_mass:.1f} kg")

    st.write(f"**BMR:** {bmr} kcal/day")

    st.write(f"**TDEE:** {tdee} kcal/day")

    st.write(f"**Target Calories:** {target} kcal/day")

    st.write(
        f"**Ideal Weight Range:** {ideal_min:.1f} kg - {ideal_max:.1f} kg"
    )

    st.write(f"**Protein Requirement:** {protein} g/day")

    st.write(f"**Water Requirement:** {water:.1f} litres/day")

    st.write(f"**Health Score:** {score}/100")