from langchain_openai import ChatOpenAI
from langgraph_project_1_dir.nodes.exa_search_node_unused import exa_search_node

llm_with_tools = ChatOpenAI(model = "gpt-4o-mini", temperature = 0).bind_tools([exa_search_node])