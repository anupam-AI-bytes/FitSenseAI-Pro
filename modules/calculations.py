"""
=========================================================
FitSense AI Pro
Module: calculations.py

This module contains all health-related calculations.

Author: Anupam Mishra
=========================================================
"""

import math


# --------------------------------------------------------
# BMI
# --------------------------------------------------------

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    weight -> kilograms
    height -> metres
    """
    if height <= 0:
        return 0

    return round(weight / (height ** 2), 2)


# --------------------------------------------------------
# BMI Category
# --------------------------------------------------------

def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Healthy"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# --------------------------------------------------------
# BMR
# Mifflin-St Jeor Equation
# --------------------------------------------------------

def calculate_bmr(weight, height, age, gender):

    height_cm = height * 100

    if gender == "Male":

        bmr = (
            (10 * weight)
            + (6.25 * height_cm)
            - (5 * age)
            + 5
        )

    else:

        bmr = (
            (10 * weight)
            + (6.25 * height_cm)
            - (5 * age)
            - 161
        )

    return round(bmr)


# --------------------------------------------------------
# Activity Multiplier
# --------------------------------------------------------

def activity_factor(activity):

    factors = {

        "Sedentary": 1.20,

        "Lightly Active": 1.375,

        "Moderately Active": 1.55,

        "Very Active": 1.725,

        "Extremely Active": 1.90
    }

    return factors.get(activity, 1.20)


# --------------------------------------------------------
# TDEE
# --------------------------------------------------------

def calculate_tdee(bmr, activity):

    factor = activity_factor(activity)

    return round(bmr * factor)


# --------------------------------------------------------
# Goal Calories
# --------------------------------------------------------

def target_calories(tdee, goal):

    if goal == "Lose Weight":

        return tdee - 500

    elif goal == "Gain Muscle":

        return tdee + 300

    else:

        return tdee


# --------------------------------------------------------
# Daily Protein
# --------------------------------------------------------

def protein_requirement(weight, goal):

    if goal == "Lose Weight":

        return round(weight * 1.6)

    elif goal == "Gain Muscle":

        return round(weight * 2.0)

    else:

        return round(weight * 1.2)


# --------------------------------------------------------
# Daily Water
# --------------------------------------------------------

def water_requirement(weight):

    return round(weight * 0.035, 1)


# --------------------------------------------------------
# Ideal Weight Range
# Based on BMI 18.5 - 24.9
# --------------------------------------------------------

def ideal_weight_range(height):

    minimum = 18.5 * (height ** 2)

    maximum = 24.9 * (height ** 2)

    return round(minimum, 1), round(maximum, 1)


# --------------------------------------------------------
# Body Fat %
# Deurenberg Formula
# --------------------------------------------------------

def body_fat_percentage(bmi, age, gender):

    gender_value = 1 if gender == "Male" else 0

    body_fat = (

        (1.20 * bmi)

        + (0.23 * age)

        - (10.8 * gender_value)

        - 5.4
    )

    return round(body_fat, 1)


# --------------------------------------------------------
# Lean Body Mass
# --------------------------------------------------------

def lean_body_mass(weight, body_fat):

    lbm = weight * (1 - body_fat / 100)

    return round(lbm, 1)


# --------------------------------------------------------
# Macronutrients
# --------------------------------------------------------

def macro_split(calories):

    protein_calories = calories * 0.30

    carbs_calories = calories * 0.45

    fat_calories = calories * 0.25

    protein = protein_calories / 4

    carbs = carbs_calories / 4

    fats = fat_calories / 9

    return {

        "Protein": round(protein),

        "Carbs": round(carbs),

        "Fats": round(fats)
    }


# --------------------------------------------------------
# Health Score
# --------------------------------------------------------

def health_score(
        bmi,
        activity,
        water,
        sleep=8):

    score = 100

    # BMI

    if bmi < 18.5:

        score -= 20

    elif bmi >= 25 and bmi < 30:

        score -= 15

    elif bmi >= 30:

        score -= 30

    # Activity

    if activity == "Sedentary":

        score -= 15

    elif activity == "Lightly Active":

        score -= 8

    elif activity == "Moderately Active":

        score -= 3

    # Water

    if water < 2:

        score -= 8

    # Sleep

    if sleep < 7:

        score -= 10

    return max(score, 0)


# --------------------------------------------------------
# Health Summary
# --------------------------------------------------------

def health_summary(category):

    summaries = {

        "Underweight":
        "You are below the recommended weight range. Consider eating a balanced diet rich in protein and strength training.",

        "Healthy":
        "Excellent! Your BMI falls within the healthy range. Maintain your current lifestyle.",

        "Overweight":
        "Your BMI is slightly above the healthy range. Regular exercise and mindful eating can help improve it.",

        "Obese":
        "Your BMI is significantly above the healthy range. Consider gradual lifestyle changes and consult a healthcare professional if needed."
    }

    return summaries.get(category)