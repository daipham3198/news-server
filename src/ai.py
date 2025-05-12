from google import genai
import utils

client = genai.Client(api_key="AIzaSyAEOkMlETxJ7iEQwK__5KYQLzulRdRdnCo")
model = "gemini-2.0-flash"

def summarize_article(url):
    response = client.models.generate_content(
        model=model,
        contents="Tóm tắt bài viết sau: " + url,
    )
    return response.text

def get_news(page, tag):
    content = utils.get_page_listing_content(page, tag)

    response = client.models.generate_content(
        model=model,
        contents="Get news as url and title as json from " + str(content),
    )

    return utils.content_to_json(response.text)