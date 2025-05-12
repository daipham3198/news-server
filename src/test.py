from google import genai

client = genai.Client(api_key="AIzaSyAEOkMlETxJ7iEQwK__5KYQLzulRdRdnCo")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Get news as url and title as json from https://vnexpress.net/tin-tuc-24h",
)

print(response.text)