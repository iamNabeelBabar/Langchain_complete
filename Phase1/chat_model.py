from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",streaming=True)

# response = llm.invoke('what is ai?')
# print(response.content)


for chunk in llm.stream('what is ai?'):
    print(chunk.content,end="", flush=True)