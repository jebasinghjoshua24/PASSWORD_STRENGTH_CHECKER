import re

password = input("Enter your password: ")

score = 0
remarks = ""

length_criteria = len(password) >= 8
lower_criteria = bool(re.search(r"[a-z]", password))
upper_criteria = bool(re.search(r"[A-Z]", password))
digit_criteria = bool(re.search(r"[0-9]", password))
symbol_criteria = bool(re.search(r"[^a-zA-Z0-9]", password))

score = 0
if length_criteria:
    score += 1
if lower_criteria:
    score += 1
if upper_criteria:
    score += 1
if digit_criteria:
    score += 1
if symbol_criteria:
    score += 1

if score == 5:
    remarks = "Very Strong"
elif score == 4:
    remarks = "Strong"
elif score == 3:
    remarks = "Medium"
elif score == 2:
    remarks = "Weak"
else:
    remarks = "Very Weak"

print(f"Password Strength: {remarks}")

if not length_criteria:
    print("- Password should be at least 8 characters long.")
if not lower_criteria:
    print("- Password should include lowercase letters.")
if not upper_criteria:
    print("- Password should include uppercase letters.")
if not digit_criteria:
    print("- Password should include digits.")
if not symbol_criteria:
    print("- Password should include special characters.")