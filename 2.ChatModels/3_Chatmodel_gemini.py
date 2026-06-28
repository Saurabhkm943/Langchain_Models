from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro-preview-tts")
result = model.invoke("what is the capital of France?")
print(result.content)