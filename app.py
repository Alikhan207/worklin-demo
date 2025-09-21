# app.py
# Worklin demo: Google Cloud NLP API

from google.cloud import language_v1

def analyze_text(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    try:
        response = client.classify_text(request={'document': document})
    except Exception as e:
        print("Error calling Google Cloud NLP API:", e)
        print("Make sure your GOOGLE_APPLICATION_CREDENTIALS env var points to a valid JSON key.")
        return

    print("Categories detected:")
    for category in response.categories:
        print(f"- {category.name} (confidence: {category.confidence:.2f})")

if _name_ == "_main_":
    sample_text = "I am a class 12 student, confused between engineering and medical."
    print("Input text:\n", sample_text, "\n")
    analyze_text(sample_text)