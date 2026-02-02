# engine.py
def calculate_patient_risk(days_since_appt, days_since_refill, activity_drop):
    # 1. Base Scores
    # Appointments: Normal gap is 90 days. Risk grows after that.
    appt_overdue = max(0, days_since_appt - 90)
    appt_score = (min(appt_overdue, 60) / 60) * 100
    
    # Pharmacy: Normal refill is 30 days.
    refill_overdue = max(0, days_since_refill - 30)
    refill_score = (min(refill_overdue, 30) / 30) * 100

    # 2. Compounding Factor (The "Silent Drop-off")
    # If a patient misses BOTH an appointment AND a refill, risk multiplies
    multiplier = 1.0
    if appt_overdue > 0 and refill_overdue > 0:
        multiplier = 1.2 

    total_risk = ((appt_score * 0.4) + (refill_score * 0.4) + (activity_drop * 0.2)) * multiplier
    
    return min(100, round(total_risk, 1))