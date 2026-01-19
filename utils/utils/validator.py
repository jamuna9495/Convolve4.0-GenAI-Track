from rapidfuzz import process, fuzz

def get_best_match(extracted_name, master_list):
    """Dealer name-ஐ Master list உடன் ஒப்பிட்டு சரியானதை எடுக்க"""
    match = process.extractOne(extracted_name, master_list, scorer=fuzz.token_sort_ratio)
    if match and match[1] > 70: # 70% மேல் மேட்ச் ஆனால் மட்டும் ஏற்கவும்
        return match[0]
    return "Unknown Dealer"
