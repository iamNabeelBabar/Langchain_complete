from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini', temperature=1, max_completion_tokens=10)

memory_dict = {}
num = 1

question = ''

while question != 'exit':
    
    question = input('Enter Question: ')
    
    if question != 'exit':
        
        system_msg = SystemMessage(f'Your are a helpful assitant this is previous conservation:{memory_dict}')
        human_msg = HumanMessage(question)
        
        messages = [system_msg, human_msg]
        
        key = f'question {num}'

        response = llm.invoke(messages)
        
        memory_dict[key] = question
        memory_dict[f'answer{num}'] = response.content

        num += 1

        print(response.content) 
        
        if len(memory_dict) == 12:
            
            first_key = next(iter(memory_dict))
            del memory_dict[first_key] 
            
            second_key = next(iter(memory_dict))
            del memory_dict[second_key] 
            
    
print(memory_dict)
print(len(memory_dict))