import google.generativeai as genai
import time
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# --- CONFIGURATION ---
# Now we fetch the key securely from the environment
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("⚠️ Error: GOOGLE_API_KEY not found in .env file!")
else:
    try:
        genai.configure(api_key=API_KEY)
    except Exception as e:
        print(f"⚠️ Warning: API Key invalid. {e}")

# Note: 'gemini-2.5-flash' does not exist yet. Using 'gemini-1.5-flash' for stability.
MODEL_NAME = "gemini-2.5-flash"

def generate_with_retry(prompt):
    """
    Connects to Google Gemini API to generate content.
    Includes retry logic for stability.
    """
    print(f"   🚀 Contacting Google AI for: {prompt[:30]}...")
    
    # Check if key loaded before trying
    if not API_KEY:
        return "Error: No API Key found."

    model = genai.GenerativeModel(MODEL_NAME)
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            # The actual API call
            response = model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            error_msg = str(e)
            
            # Handle Rate Limiting (Quota Exceeded)
            if "429" in error_msg:
                print(f"   ⚠️ Quota hit (Attempt {attempt+1}/{max_retries}). Waiting 60s...")
                time.sleep(60)
                continue
            
            # Handle other errors
            return f"API Error: {error_msg}"
            
    return "Failed: Service is currently busy. Please try again later."
