"""
=========================================================
FitSense AI Pro
Module: charts.py

Creates beautiful Plotly charts
for the FitSense AI dashboard.

Author: Anupam Mishra
=========================================================
"""

import plotly.graph_objects as go
import plotly.express as px


# --------------------------------------------------------
# BMI Gauge Chart
# --------------------------------------------------------

def bmi_gauge(bmi):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=bmi,

        title={'text': "Body Mass Index"},

        gauge={

            'axis': {'range': [10, 40]},

            'bar': {'color': "darkblue"},

            'steps': [

                {'range': [10, 18.5], 'color': "#87CEFA"},

                {'range': [18.5, 25], 'color': "#90EE90"},

                {'range': [25, 30], 'color': "#FFD700"},

                {'range': [30, 40], 'color': "#FF7F7F"}

            ]
        }
    ))

    fig.update_layout(height=350)

    return fig


# --------------------------------------------------------
# Macronutrient Pie Chart
# --------------------------------------------------------

def macro_chart(macros):

    labels = list(macros.keys())

    values = list(macros.values())

    fig = px.pie(

        names=labels,

        values=values,

        hole=0.45,

        title="Daily Macronutrient Distribution"

    )

    fig.update_traces(textinfo="percent+label")

    return fig


# --------------------------------------------------------
# Calories Bar Chart
# --------------------------------------------------------

def calorie_chart(calories):

    labels = [

        "Breakfast",

        "Lunch",

        "Dinner",

        "Snacks"

    ]

    values = [

        calories * 0.25,

        calories * 0.35,

        calories * 0.30,

        calories * 0.10

    ]

    fig = px.bar(

        x=labels,

        y=values,

        labels={

            "x": "Meals",

            "y": "Calories"

        },

        title="Suggested Calorie Distribution"

    )

    return fig


# --------------------------------------------------------
# Water Intake Chart
# --------------------------------------------------------

def water_chart(water):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Water Intake"],

            y=[water],

            text=[f"{water} L"],

            textposition="outside"

        )

    )

    fig.update_layout(

        title="Recommended Daily Water Intake",

        yaxis_title="Litres",

        height=350

    )

    return fig


# --------------------------------------------------------
# Health Score Gauge
# --------------------------------------------------------

def health_score_gauge(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        title={'text': "Health Score"},

        gauge={

            'axis': {'range': [0, 100]},

            'bar': {'color': "green"},

            'steps': [

                {'range': [0, 40], 'color': "#ff6b6b"},

                {'range': [40, 70], 'color': "#ffe66d"},

                {'range': [70, 100], 'color': "#6bff95"}

            ]
        }
    ))

    fig.update_layout(height=350)

    return fig


# --------------------------------------------------------
# BMI Comparison Chart
# --------------------------------------------------------

def bmi_comparison(bmi):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Your BMI"],

            y=[bmi]

        )

    )

    fig.add_hline(

        y=18.5,

        line_dash="dash",

        annotation_text="Healthy Minimum"

    )

    fig.add_hline(

        y=24.9,

        line_dash="dash",

        annotation_text="Healthy Maximum"

    )

    fig.update_layout(

        title="BMI Comparison",

        yaxis_title="BMI",

        height=350

    )

    return fig