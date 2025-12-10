from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt_template = PromptTemplate(
    input_variables=['topic'],
    template="Write a 10 bullet points on {topic}"
)

llm = ChatOpenAI(model='gpt-4o-mini')

formatted_prompt = prompt_template.format(topic="Human Rights violation in gaza")

response = llm.invoke(formatted_prompt)

print(response.content)