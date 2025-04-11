import google.generativeai as genai

genai.configure(api_key="AIzaSyD0qoHqe60nmuoDbdd_jhkztILsBSpLqW8")

def getResponse(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')  # modelo gratuito
    response = model.generate_content(prompt)
    return response.text