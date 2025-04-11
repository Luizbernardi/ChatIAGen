from google import genai

def getResponse(prompt):
    client = genai.Client(api_key="")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return(response.text)