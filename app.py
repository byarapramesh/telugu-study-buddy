# Telugu AI Study Buddy - Final Project
# Team: Ramesh, Kubeer, Nirmal
# SIH 2025 - For Rural Telangana Students

import pytesseract
from PIL import Image
import google.generativeai as genai
from gtts import gTTS
import os

# 1. Gemini API Setup
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

def telugu_study_buddy(image_path):
    print("--- Bot Started ---")
    
    # Step 1: OCR - Photo nundi English chadavada
    try:
        img = Image.open(image_path)
        english_text = pytesseract.image_to_string(img)
        print(f"Student Doubt (English): {english_text}")
    except Exception as e:
        return f"Image read error: {e}"

    if not english_text.strip():
        return "Photo lo text kanipinchaledu, clear ga photo teeyandi"

    # Step 2: AI - Simple Telugu loki marchadam
    prompt = f"""
    You are a friendly Telugu teacher for rural Telangana degree students.
    Explain this topic in very simple, easy Telugu (Telangana slang).
    Use short sentences and examples.
    Topic: {english_text}
    
    Give answer in Telugu only.
    """
    
    try:
        response = model.generate_content(prompt)
        telugu_answer = response.text
        print(f"Telugu Answer: {telugu_answer}")
    except Exception as e:
        return f"AI Error: {e}"

    # Step 3: Voice - Telugu Voice cheyadam
    try:
        tts = gTTS(text=telugu_answer, lang='te', slow=False)
        tts.save("telugu_answer.mp3")
        print("Voice saved as telugu_answer.mp3")
    except Exception as e:
        print(f"Voice Error: {e}")

    return telugu_answer

if __name__ == "__main__":
    print("Telugu Study Buddy Bot is Ready for WhatsApp!")
