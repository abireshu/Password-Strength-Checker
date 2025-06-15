import re
from breach_check import check_pwned

def pwd_checker(password):
    feedback = []
    score = 0

    if len(password) < 8:
        feedback.append("Password must be at least 8 characters long.")
    else:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    max_score = 5
    strength_percent = int((score / max_score) * 100)
    
    breached, breach_msg = check_pwned(password)

    if not feedback:
        result = "✅ Strong password!\n" + breach_msg
        return result, "green", strength_percent
    else:
           result = "\n".join(feedback) + "\n" + breach_msg
    return result, "red", strength_percent
