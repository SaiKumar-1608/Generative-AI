from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
 
load_dotenv()
 
prompt = PromptTemplate(

    template='Generate 5 interesting facts about {topic}',

    input_variables=['topic']

)
 
model = ChatOpenAI()
 
parser = StrOutputParser()
 
chain = prompt | model | parser
#invoke function is a runnable function, it can be used multiple number of times 
#simply it awakens the data or collects the data
result = chain.invoke({'topic':'cricket'})
#here that data will be given as output.
print(result)
 
chain.get_graph().print_ascii()  # To visualize the chain
 