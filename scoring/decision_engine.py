def final_decision(score):
    if score >= 15:
        return "Selected"
    elif score >= 5:
        return "Hold"
    else:
        return "Rejected"