from langchain_openai import ChatOpenAI
from langgraph_project_1_dir.structured_output.parsed_query_class import parsed_query

llm_2 = ChatOpenAI(model = "gpt-4o-mini", temperature = 0) 

llm_structured = llm_2.with_structured_output(parsed_query)