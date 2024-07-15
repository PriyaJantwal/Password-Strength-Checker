#Password Strength Checker
import re
def check_password_strength(password):
    # Criteria definitions
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Feedback initialization
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")

    # Strength assessment
    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

    if strength == 5:
        feedback.append("Password strength: Strong")
    elif 3 <= strength < 5:
        feedback.append("Password strength: Medium")
    else:
        feedback.append("Password strength: Weak")

    return feedback

# Example usage
password = input("Enter a password to check: ")
feedback = check_password_strength(password)
for line in feedback:
    print(line)

