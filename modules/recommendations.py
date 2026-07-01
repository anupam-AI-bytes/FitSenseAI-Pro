"""
=========================================================
FitSense AI Pro
Module: recommendations.py

This module generates personalized
health recommendations.

Author: Anupam Mishra
=========================================================
"""


# --------------------------------------------------------
# Diet Recommendation
# --------------------------------------------------------

def diet_recommendation(goal):

    if goal == "Lose Weight":

        return [
            "🥗 Eat more vegetables and fruits.",
            "🍗 Include lean protein in every meal.",
            "🚫 Reduce sugary drinks and junk food.",
            "🥜 Snack on nuts and seeds in moderation.",
            "🥣 Prefer whole grains over refined grains."
        ]

    elif goal == "Gain Muscle":

        return [
            "🥩 Eat protein-rich foods.",
            "🍚 Increase healthy carbohydrates.",
            "🥛 Drink milk or protein shakes.",
            "🥚 Include eggs, paneer or tofu.",
            "🥜 Eat healthy fats from nuts and peanut butter."
        ]

    else:

        return [
            "🥗 Maintain a balanced diet.",
            "🍎 Eat seasonal fruits.",
            "🥦 Include vegetables daily.",
            "💧 Stay hydrated.",
            "🥜 Consume healthy fats."
        ]


# --------------------------------------------------------
# Workout Recommendation
# --------------------------------------------------------

def workout_recommendation(goal, activity):

    if goal == "Lose Weight":

        return [
            "🚶 Walk 8,000–10,000 steps daily.",
            "🏃 Cardio 30–45 minutes.",
            "🏋 Strength training 3–4 times/week.",
            "🧘 Stretch after every workout."
        ]

    elif goal == "Gain Muscle":

        return [
            "🏋 Progressive strength training.",
            "💪 Focus on compound exercises.",
            "🥛 Eat protein after workouts.",
            "😴 Sleep at least 8 hours."
        ]

    else:

        return [
            "🚶 Stay active daily.",
            "🏃 Cardio 3 times/week.",
            "🏋 Strength train twice/week.",
            "🧘 Practice flexibility exercises."
        ]


# --------------------------------------------------------
# Water Reminder
# --------------------------------------------------------

def water_tip(water):

    if water < 2:

        return (
            "💧 Your estimated intake is below "
            "2 litres. Keep a water bottle with you."
        )

    elif water < 3:

        return (
            "💧 Your hydration target looks good. "
            "Drink water consistently throughout the day."
        )

    else:

        return (
            "💧 Great! Make sure you spread your "
            "water intake throughout the day."
        )


# --------------------------------------------------------
# Sleep Recommendation
# --------------------------------------------------------

def sleep_tip(age):

    if age < 18:

        return "😴 Aim for 8–10 hours of sleep."

    elif age < 65:

        return "😴 Aim for 7–9 hours of quality sleep."

    else:

        return "😴 Aim for 7–8 hours of sleep."


# --------------------------------------------------------
# BMI Advice
# --------------------------------------------------------

def bmi_advice(category):

    advice = {

        "Underweight":
        "⚠ You are underweight. Increase healthy calories and strength training.",

        "Healthy":
        "✅ Great! Maintain your current lifestyle and exercise regularly.",

        "Overweight":
        "⚠ Try to create a calorie deficit through diet and activity.",

        "Obese":
        "🚨 Consider gradual weight loss and consult a healthcare professional if needed."
    }

    return advice.get(category)


# --------------------------------------------------------
# Daily Motivation
# --------------------------------------------------------

def daily_motivation():

    return (
        "🌟 Small healthy habits repeated every day "
        "lead to big results over time."
    )


# --------------------------------------------------------
# Lifestyle Tips
# --------------------------------------------------------

def lifestyle_tips():

    return [

        "🥗 Eat slowly and mindfully.",

        "🚶 Walk after meals.",

        "📵 Reduce screen time before bed.",

        "💧 Carry a water bottle.",

        "🍎 Include fruits daily.",

        "🥦 Eat more vegetables.",

        "🏋 Exercise at least 150 minutes/week.",

        "😴 Maintain a consistent sleep schedule.",

        "🧘 Manage stress with meditation.",

        "🚭 Avoid smoking and excessive alcohol."
    ]


# --------------------------------------------------------
# Health Risk Indicator
# --------------------------------------------------------

def risk_level(category):

    if category == "Healthy":

        return "🟢 Low Risk"

    elif category == "Underweight":

        return "🟡 Mild Risk"

    elif category == "Overweight":

        return "🟠 Moderate Risk"

    else:

        return "🔴 High Risk"


# --------------------------------------------------------
# Weekly Challenge
# --------------------------------------------------------

def weekly_challenge():

    return [

        "✅ Drink 2–3 litres of water daily",

        "✅ Walk at least 8,000 steps",

        "✅ Exercise 4 times this week",

        "✅ Sleep before 11 PM",

        "✅ Eat one fruit every day"
    ]