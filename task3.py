import getpass
import re

def check_common_patterns(password):
    # Check for sequences or common patterns
    common_patterns = ['123', 'abc', 'password', 'qwerty', 'letmein', 'admin']
    for pattern in common_patterns:
        if pattern in password.lower():
            return True
    return False

def check_personal_info(password):
    # Example personal information patterns (expand as needed)
    personal_info_patterns = ['yourname', 'birthday', 'username']
    for pattern in personal_info_patterns:
        if pattern in password.lower():
            return True
    return False

print("----------------------Password Complexity Checker----------------")
print("\n")
print("--------------------------NOTICE----------------------------------")
print("Passwords must be at least 8 characters long.")
print("Passwords must include at least one lowercase letter.")
print("Passwords must include at least one uppercase letter.")
print("Passwords must include at least one numeric digit.")
print("Passwords must include at least one special character (e.g., !, @, #, $, %, etc.).")
print("Passwords should not include easily guessable personal information, such as your name, birthday, or username.")
print("\n")

password = getpass.getpass("Enter Password :")
score = 0
feedback = []

# Check password length
if len(password) >= 12:
    score += 30
elif len(password) >= 8:
    score += 20
    feedback.append("Consider using a longer password (12+ characters) for better security.")
else:
    feedback.append("Password length must be at least 8 characters.")

# Check for lowercase, uppercase, digit, and special characters
if any(c.islower() for c in password):
    score += 20
else:
    feedback.append("Password must include at least one lowercase letter.")

if any(c.isupper() for c in password):
    score += 20
else:
    feedback.append("Password must include at least one uppercase letter.")

if any(c.isdigit() for c in password):
    score += 20
else:
    feedback.append("Password must include at least one numeric digit.")

if any(not c.isalnum() for c in password):
    score += 20
else:
    feedback.append("Password must include at least one special character (e.g., !, @, #, $, %, etc.).")

# Check for common patterns and personal information
if check_common_patterns(password):
    score -= 10
    feedback.append("Password contains common patterns or sequences that are easily guessable (e.g., '123', 'abc'). Avoid these.")

if check_personal_info(password):
    score -= 10
    feedback.append("Password contains personal information that could be easily guessed (e.g., name, birthday, username).")

# Provide feedback and final score
print("\nPassword Feedback:")
for item in feedback:
    print("- " + item)

if score < 50:
    strength = "Weak"
elif score < 70:
    strength = "Moderate"
elif score < 90:
    strength = "Strong"
else:
    strength = "Very Strong"

print("\nYour password score:", score)
print("Password Strength:", strength)