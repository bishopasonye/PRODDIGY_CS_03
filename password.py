# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:18:53 2024

@author: HP
"""

import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should have at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should have at least one lowercase letter.")

    # Number check
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Special character check
    if re.search(r'[@#$%^&+=]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Assess overall strength
    if strength == 5:
        return "Strong password!", feedback
    elif 3 <= strength < 5:
        return "Moderate password!", feedback
    else:
        return "Weak password!", feedback


# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for suggestion in feedback:
        print(f"- {suggestion}")
