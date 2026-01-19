import cv2
import numpy as np
from pdf2image import convert_from_path

def pdf_to_image(pdf_path):
    """PDF-ன் முதல் பக்கத்தை இமேஜாக மாற்ற"""
    pages = convert_from_path(pdf_path, dpi=300)
    return np.array(pages[0])

def enhance_image(image):
    """OCR துல்லியமாக இருக்க இமேஜை Gray scale-க்கு மாற்ற"""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray
