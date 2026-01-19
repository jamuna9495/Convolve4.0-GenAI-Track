import re

def clean_text(text):
    """தேவையற்ற குறியீடுகளை நீக்கி டெக்ஸ்டை சுத்தம் செய்ய"""
    return " ".join(text.split())

def extract_numeric_value(text):
    """Cost மற்றும் HP போன்ற எண்களை மட்டும் எடுக்க"""
    # ரூ. 5,00,000 -> 500000 என மாற்றும்
    numbers = re.findall(r'\d+', text.replace(',', '').replace(' ', ''))
    return int(numbers[0]) if numbers else 0
