from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llm  =  ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature= 0,
    api_key = os.getenv("GOOGLE_API_KEY")
)
response = llm.invoke("Expalin RX100 Company In Yamaha")
print(response.content)
print()
